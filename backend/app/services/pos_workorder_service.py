"""
POS Kasir, Work Order (PKB), & Otomatisasi Gudang Sparepart (Pilar 3)
=====================================================================
Project Bengkel Masa Depan (FastAPI + Async SQLAlchemy 2.0)

Fitur Utama:
1. Pembuatan & Manajemen Work Order / PKB (`WorkOrder` & `WorkOrderItem`):
   - Menghitung estimasi biaya sparepart + jasa pengerjaan secara otomatis.
   - Validasi ketersediaan stok gudang sebelum item sparepart dimasukkan ke PKB.
2. Otomatisasi Pemotongan Stok Gudang (`Sparepart` & `StockMovement`):
   - Saat status PKB diubah menjadi `COMPLETED`, stok fisik berkurang secara atomik
     (menggunakan row-level locking `with_for_update`) dan riwayat `StockMovement` tercatat.
   - Terintegrasi langsung dengan `SmartDiagnosticEngine.record_resolution_and_learn()`
     sehingga penyelesaian PKB otomatis memperkaya database `FaultHistory` (Self-Learning Loop).
3. Invoicing Kasir & Cetak Nota (`Transaction` & `TransactionItem`):
   - Perhitungan DPP, diskon, dan PPN 11% otomatis.
   - Mendukung metode pembayaran Tunai (`CASH`), Transfer Bank (`TRANSFER`), dan `QRIS`.
"""

from datetime import datetime, timezone
from decimal import Decimal
from typing import Literal

from fastapi import APIRouter, Depends, HTTPException, Query, status
from pydantic import BaseModel, Field
from sqlalchemy import func, select
from sqlalchemy.ext.asyncio import AsyncSession

from app.api.deps import get_current_active_user, get_db
from app.models import (
    Customer,
    Sparepart,
    StockMovement,
    Transaction,
    TransactionItem,
    User,
    Vehicle,
    WorkOrder,
    WorkOrderItem,
)
from app.services.diagnostic_service import (
    SelfLearningFeedbackRequest,
    SmartDiagnosticEngine,
    split_dtc_codes,
)

# ---------------------------------------------------------------------------
# 1. PYDANTIC V2 SCHEMAS
# ---------------------------------------------------------------------------


class SparepartOut(BaseModel):
    id: int
    sku: str
    name: str
    category: str
    sell_price: float
    buy_price: float
    stock_qty: int
    unit: str
    min_stock_alert: int


class WorkOrderListItem(BaseModel):
    id: int
    wo_number: str
    customer_name: str
    license_plate: str
    vehicle_model: str
    complaint: str
    status: str
    total_estimated_cost: float
    created_at: str | None = None
    invoice_number: str | None = None
    vehicle_brand: str = ""
    vehicle_model_name: str = ""
    vehicle_year: int | None = None
    dtc_codes: str = ""
    vehicle_engine_code: str = ""
    repair_summary: str = ""


class WorkOrderItemCreate(BaseModel):
    item_type: Literal["SPAREPART", "SERVICE_LABOR"]
    sparepart_id: int | None = Field(
        default=None, description="Wajib diisi jika item_type == SPAREPART"
    )
    description: str = Field(..., examples=["Penggantian Ignition Coil #2"])
    qty: int = Field(..., ge=1, examples=[1])
    unit_price: Decimal | None = Field(
        default=None,
        description="Opsional untuk SPAREPART (otomatis ambil sell_price gudang jika kosong)",
    )


class WorkOrderCreateRequest(BaseModel):
    vehicle_id: int
    mechanic_id: int | None = None
    customer_complaint: str = Field(..., min_length=5)
    initial_dtc_codes: list[str] = Field(default_factory=list)
    items: list[WorkOrderItemCreate] = Field(default_factory=list)


class CompleteWorkOrderRequest(BaseModel):
    resolved_checkpoint_id: int | None = Field(
        default=None,
        description="Jika diisi, otomatis memicu Self-Learning Loop pada Smart Diagnostic Engine",
    )
    resolution_notes: str = Field(
        default="Perbaikan selesai sesuai SOP PKB.",
        description="Catatan penyelesaian mekanik",
    )


class WorkOrderOut(BaseModel):
    id: int
    wo_number: str
    vehicle_id: int
    status: str
    customer_complaint: str
    initial_dtc_codes: str
    estimated_total: Decimal
    items_count: int


class CheckoutInvoiceRequest(BaseModel):
    work_order_id: int
    payment_method: Literal["CASH", "TRANSFER", "QRIS"] = "QRIS"
    discount_amount: Decimal = Field(default=Decimal("0.00"), ge=Decimal("0.00"))
    apply_ppn_11: bool = Field(default=True, description="Terapkan PPN 11%")


class InvoiceReceiptOut(BaseModel):
    transaction_id: int
    invoice_number: str
    wo_number: str
    customer_name: str
    vehicle_plate: str
    vehicle_model: str
    subtotal_dpp: Decimal
    discount_amount: Decimal
    tax_ppn_rate: Decimal
    tax_ppn_amount: Decimal
    grand_total: Decimal
    payment_method: str
    payment_status: str
    paid_at: datetime
    line_items: list[dict]


# ---------------------------------------------------------------------------
# 2. SERVICE LAYER: WORK ORDER, INVENTORY, & POS KASIR
# ---------------------------------------------------------------------------


class WorkshopPOSService:
    """Service terpadu untuk siklus hidup PKB, pemotongan stok otomatis, dan kasir PPN 11%."""

    PPN_RATE = Decimal("11.00")

    @staticmethod
    async def _generate_number(session: AsyncSession, model_cls, prefix: str) -> str:
        now = datetime.now(timezone.utc)
        ym = now.strftime("%Y%m")
        max_stmt = select(func.max(model_cls.id))
        max_id = (await session.execute(max_stmt)).scalar_one() or 0
        num_col = (
            model_cls.wo_number
            if hasattr(model_cls, "wo_number")
            else model_cls.invoice_number
        )
        seq = max_id + 1
        while True:
            candidate = f"{prefix}-{ym}-{seq:04d}"
            exists = (
                await session.execute(select(model_cls.id).where(num_col == candidate))
            ).scalar_one_or_none()
            if not exists:
                return candidate
            seq += 1

    @classmethod
    async def create_work_order(
        cls,
        session: AsyncSession,
        payload: WorkOrderCreateRequest,
        current_user: User,
    ) -> WorkOrderOut:
        """Membuat PKB baru beserta rincian estimasi sparepart dan jasa servis."""
        veh = (
            await session.execute(select(Vehicle).where(Vehicle.id == payload.vehicle_id))
        ).scalar_one_or_none()
        if not veh:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Data kendaraan tidak ditemukan.",
            )

        wo_number = await cls._generate_number(session, WorkOrder, "PKB")
        dtc_str = ",".join(split_dtc_codes(",".join(payload.initial_dtc_codes)))

        wo = WorkOrder(
            wo_number=wo_number,
            vehicle_id=payload.vehicle_id,
            service_advisor_id=current_user.id,
            mechanic_id=payload.mechanic_id,
            customer_complaint=payload.customer_complaint.strip(),
            initial_dtc_codes=dtc_str,
            status="IN_PROGRESS",
            estimated_total=Decimal("0.00"),
            created_at=datetime.now(timezone.utc),
        )
        session.add(wo)
        await session.flush()

        running_total = Decimal("0.00")
        for item_in in payload.items:
            unit_price = item_in.unit_price
            if item_in.item_type == "SPAREPART":
                if not item_in.sparepart_id:
                    raise HTTPException(
                        status_code=status.HTTP_400_BAD_REQUEST,
                        detail=f"Item sparepart '{item_in.description}' wajib menyertakan sparepart_id.",
                    )
                sp = (
                    await session.execute(
                        select(Sparepart).where(Sparepart.id == item_in.sparepart_id)
                    )
                ).scalar_one_or_none()
                if not sp:
                    raise HTTPException(
                        status_code=status.HTTP_404_NOT_FOUND,
                        detail=f"Sparepart ID {item_in.sparepart_id} tidak ditemukan di gudang.",
                    )
                if sp.stock_qty < item_in.qty:
                    raise HTTPException(
                        status_code=status.HTTP_400_BAD_REQUEST,
                        detail=(
                            f"Stok '{sp.name}' tidak mencukupi (Tersedia: {sp.stock_qty} {sp.unit}, "
                            f"Diminta: {item_in.qty} {sp.unit})."
                        ),
                    )
                if unit_price is None:
                    unit_price = Decimal(str(sp.sell_price))
            else:
                if unit_price is None:
                    raise HTTPException(
                        status_code=status.HTTP_400_BAD_REQUEST,
                        detail=f"Item jasa '{item_in.description}' wajib mencantumkan unit_price.",
                    )

            subtotal = (unit_price * Decimal(item_in.qty)).quantize(Decimal("0.01"))
            running_total += subtotal

            session.add(
                WorkOrderItem(
                    work_order_id=wo.id,
                    item_type=item_in.item_type,
                    sparepart_id=item_in.sparepart_id,
                    description=item_in.description,
                    qty=item_in.qty,
                    unit_price=unit_price,
                    subtotal=subtotal,
                )
            )

        wo.estimated_total = running_total
        await session.flush()

        return WorkOrderOut(
            id=wo.id,
            wo_number=wo.wo_number,
            vehicle_id=wo.vehicle_id,
            status=wo.status,
            customer_complaint=wo.customer_complaint,
            initial_dtc_codes=wo.initial_dtc_codes or "",
            estimated_total=wo.estimated_total,
            items_count=len(payload.items),
        )

    @classmethod
    async def complete_work_order_and_deduct_stock(
        cls,
        session: AsyncSession,
        work_order_id: int,
        payload: CompleteWorkOrderRequest,
        current_user: User,
    ) -> dict:
        """
        Menyelesaikan PKB (`COMPLETED`), memotong stok sparepart secara otomatis,
        mencatat `StockMovement`, dan memicu `SmartDiagnosticEngine` Self-Learning Loop.
        """
        wo = (
            await session.execute(select(WorkOrder).where(WorkOrder.id == work_order_id))
        ).scalar_one_or_none()
        if not wo:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Work Order (PKB) tidak ditemukan.",
            )
        if wo.status == "COMPLETED":
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="Work Order ini sudah berstatus COMPLETED sebelumnya.",
            )

        items = (
            await session.execute(
                select(WorkOrderItem).where(WorkOrderItem.work_order_id == wo.id)
            )
        ).scalars().all()

        low_stock_warnings: list[str] = []

        # Potong stok untuk setiap item bertipe SPAREPART
        for item in items:
            if item.item_type == "SPAREPART" and item.sparepart_id:
                sp_stmt = (
                    select(Sparepart)
                    .where(Sparepart.id == item.sparepart_id)
                    .with_for_update()
                )
                sp = (await session.execute(sp_stmt)).scalar_one_or_none()
                if not sp:
                    continue
                if sp.stock_qty < item.qty:
                    raise HTTPException(
                        status_code=status.HTTP_400_BAD_REQUEST,
                        detail=f"Gagal menyelesaikan PKB: Stok '{sp.name}' kurang (Sisa: {sp.stock_qty}).",
                    )

                sp.stock_qty -= item.qty
                session.add(
                    StockMovement(
                        sparepart_id=sp.id,
                        movement_type="PKB_OUT",
                        qty_change=-item.qty,
                        balance_after=sp.stock_qty,
                        reference_note=f"Pemakaian PKB {wo.wo_number}",
                        created_by_id=current_user.id,
                    )
                )

                if sp.stock_qty <= sp.min_stock_alert:
                    low_stock_warnings.append(
                        f"Stok '{sp.name}' ({sp.sku}) menipis: sisa {sp.stock_qty} {sp.unit} (batas minimum: {sp.min_stock_alert})."
                    )

        wo.status = "COMPLETED"

        # Jika ada titik cek yang dikonfirmasi menyelesaikan masalah, jalankan Self-Learning Loop!
        learned_history_id: int | None = None
        if payload.resolved_checkpoint_id:
            dtc_list = [
                c.strip() for c in (wo.initial_dtc_codes or "").split(",") if c.strip()
            ]
            feedback = SelfLearningFeedbackRequest(
                work_order_id=wo.id,
                vehicle_id=wo.vehicle_id,
                resolved_checkpoint_id=payload.resolved_checkpoint_id,
                symptom_text=wo.customer_complaint,
                dtc_codes=dtc_list,
                resolution_notes=payload.resolution_notes,
            )
            new_hist = await SmartDiagnosticEngine.record_resolution_and_learn(
                session=session, feedback=feedback
            )
            learned_history_id = new_hist.id

        await session.flush()
        return {
            "wo_number": wo.wo_number,
            "new_status": wo.status,
            "learned_fault_history_id": learned_history_id,
            "low_stock_alerts": low_stock_warnings,
        }

    @classmethod
    async def checkout_and_generate_invoice(
        cls,
        session: AsyncSession,
        payload: CheckoutInvoiceRequest,
        current_user: User,
    ) -> InvoiceReceiptOut:
        """
        Menerbitkan Invoice Kasir (`Transaction` & `TransactionItem`) dari PKB yang telah selesai,
        menghitung PPN 11%, dan menghasilkan struktur data siap cetak nota thermal/PDF.
        """
        wo = (
            await session.execute(
                select(WorkOrder).where(WorkOrder.id == payload.work_order_id)
            )
        ).scalar_one_or_none()
        if not wo:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Work Order (PKB) tidak ditemukan.",
            )
        if wo.status != "COMPLETED":
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="PKB harus diselesaikan (status COMPLETED) sebelum diproses di kasir.",
            )

        existing_trx = (
            await session.execute(
                select(Transaction).where(Transaction.work_order_id == wo.id)
            )
        ).scalar_one_or_none()
        if existing_trx:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail=f"PKB {wo.wo_number} sudah memiliki invoice ({existing_trx.invoice_number}).",
            )

        wo_items = (
            await session.execute(
                select(WorkOrderItem).where(WorkOrderItem.work_order_id == wo.id)
            )
        ).scalars().all()

        veh = (
            await session.execute(select(Vehicle).where(Vehicle.id == wo.vehicle_id))
        ).scalar_one()
        cust = (
            await session.execute(select(Customer).where(Customer.id == veh.customer_id))
        ).scalar_one()

        subtotal_dpp = sum(
            (Decimal(str(i.subtotal)) for i in wo_items), Decimal("0.00")
        ).quantize(Decimal("0.01"))
        discount = min(payload.discount_amount, subtotal_dpp).quantize(Decimal("0.01"))
        taxable_base = subtotal_dpp - discount

        ppn_rate = cls.PPN_RATE if payload.apply_ppn_11 else Decimal("0.00")
        ppn_amount = ((taxable_base * ppn_rate) / Decimal("100.00")).quantize(
            Decimal("0.01")
        )
        grand_total = (taxable_base + ppn_amount).quantize(Decimal("0.01"))

        inv_number = await cls._generate_number(session, Transaction, "INV")
        paid_time = datetime.now(timezone.utc)

        trx = Transaction(
            invoice_number=inv_number,
            work_order_id=wo.id,
            cashier_id=current_user.id,
            subtotal=subtotal_dpp,
            tax_ppn_rate=ppn_rate,
            tax_ppn_amount=ppn_amount,
            discount_amount=discount,
            grand_total=grand_total,
            payment_method=payload.payment_method,
            payment_status="PAID",
            paid_at=paid_time,
        )
        session.add(trx)
        await session.flush()

        receipt_items: list[dict] = []
        for wi in wo_items:
            session.add(
                TransactionItem(
                    transaction_id=trx.id,
                    description=wi.description,
                    item_type=wi.item_type,
                    qty=wi.qty,
                    unit_price=wi.unit_price,
                    subtotal=wi.subtotal,
                )
            )
            receipt_items.append(
                {
                    "description": wi.description,
                    "item_type": wi.item_type,
                    "qty": wi.qty,
                    "unit_price": float(wi.unit_price),
                    "subtotal": float(wi.subtotal),
                }
            )

        await session.flush()
        return InvoiceReceiptOut(
            transaction_id=trx.id,
            invoice_number=trx.invoice_number,
            wo_number=wo.wo_number,
            customer_name=cust.name,
            vehicle_plate=veh.license_plate,
            vehicle_model=f"{veh.brand} {veh.model} ({veh.year})",
            subtotal_dpp=subtotal_dpp,
            discount_amount=discount,
            tax_ppn_rate=ppn_rate,
            tax_ppn_amount=ppn_amount,
            grand_total=grand_total,
            payment_method=trx.payment_method,
            payment_status=trx.payment_status,
            paid_at=paid_time,
            line_items=receipt_items,
        )


# ---------------------------------------------------------------------------
# 3. FASTAPI ROUTER ENDPOINTS
# ---------------------------------------------------------------------------

router = APIRouter(prefix="/api/v1/pos", tags=["POS Kasir, PKB & Gudang Sparepart"])


@router.post(
    "/work-orders",
    response_model=WorkOrderOut,
    status_code=status.HTTP_201_CREATED,
    summary="Buat Work Order (PKB) Baru & Validasi Stok Gudang",
)
async def create_new_work_order(
    payload: WorkOrderCreateRequest,
    db: AsyncSession = Depends(get_db),
    current_user: User = Depends(get_current_active_user),
) -> WorkOrderOut:
    wo_out = await WorkshopPOSService.create_work_order(db, payload, current_user)
    await db.commit()
    return wo_out


@router.post(
    "/work-orders/{work_order_id}/complete",
    summary="Selesaikan PKB, Potong Stok Sparepart Otomatis, & Trigger Self-Learning",
)
async def complete_work_order_endpoint(
    work_order_id: int,
    payload: CompleteWorkOrderRequest,
    db: AsyncSession = Depends(get_db),
    current_user: User = Depends(get_current_active_user),
) -> dict:
    result = await WorkshopPOSService.complete_work_order_and_deduct_stock(
        db, work_order_id, payload, current_user
    )
    await db.commit()
    return result


@router.post(
    "/checkout-invoice",
    response_model=InvoiceReceiptOut,
    status_code=status.HTTP_201_CREATED,
    summary="Proses Pembayaran Kasir (PPN 11%, Tunai/Transfer/QRIS) & Cetak Nota",
)
async def checkout_invoice_endpoint(
    payload: CheckoutInvoiceRequest,
    db: AsyncSession = Depends(get_db),
    current_user: User = Depends(get_current_active_user),
) -> InvoiceReceiptOut:
    receipt = await WorkshopPOSService.checkout_and_generate_invoice(
        db, payload, current_user
    )
    await db.commit()
    return receipt


@router.get(
    "/spareparts",
    response_model=list[SparepartOut],
    summary="Daftar Sparepart Gudang & Stok Terkini",
)
async def list_spareparts_endpoint(
    category: str | None = Query(None),
    search: str | None = Query(None),
    db: AsyncSession = Depends(get_db),
    current_user: User = Depends(get_current_active_user),
) -> list[SparepartOut]:
    stmt = select(Sparepart).order_by(Sparepart.name.asc())
    if category:
        stmt = stmt.where(Sparepart.category == category)
    if search:
        stmt = stmt.where(
            (Sparepart.name.ilike(f"%{search}%")) | (Sparepart.sku.ilike(f"%{search}%"))
        )
    rows = (await db.execute(stmt)).scalars().all()
    return [
        SparepartOut(
            id=r.id,
            sku=r.sku,
            name=r.name,
            category=r.category,
            sell_price=float(r.sell_price),
            buy_price=float(r.buy_price),
            stock_qty=r.stock_qty,
            unit=r.unit,
            min_stock_alert=r.min_stock_alert,
        )
        for r in rows
    ]


@router.get(
    "/work-orders",
    response_model=list[WorkOrderListItem],
    summary="Daftar Seluruh Work Order (PKB) Bengkel",
)
async def list_work_orders_endpoint(
    status_filter: str | None = Query(None),
    db: AsyncSession = Depends(get_db),
    current_user: User = Depends(get_current_active_user),
) -> list[WorkOrderListItem]:
    stmt = (
        select(WorkOrder, Vehicle, Customer)
        .join(Vehicle, WorkOrder.vehicle_id == Vehicle.id)
        .join(Customer, Vehicle.customer_id == Customer.id)
        .order_by(WorkOrder.id.desc())
    )
    if status_filter:
        stmt = stmt.where(WorkOrder.status == status_filter)
    results = (await db.execute(stmt)).all()
    inv_map = {
        t.work_order_id: t.invoice_number
        for t in (await db.execute(select(Transaction))).scalars().all()
    }
    items_by_wo: dict[int, list[str]] = {}
    for it in (await db.execute(select(WorkOrderItem))).scalars().all():
        items_by_wo.setdefault(it.work_order_id, []).append(it.description)
    out = []
    for wo, veh, cust in results:
        out.append(
            WorkOrderListItem(
                id=wo.id,
                wo_number=wo.wo_number,
                customer_name=cust.name,
                license_plate=veh.license_plate,
                vehicle_model=f"{veh.brand} {veh.model} ({veh.year})",
                complaint=wo.customer_complaint,
                status=wo.status,
                total_estimated_cost=float(wo.estimated_total or 0),
                created_at=wo.created_at.strftime("%Y-%m-%d %H:%M") if wo.created_at else None,
                invoice_number=inv_map.get(wo.id),
                vehicle_brand=veh.brand,
                vehicle_model_name=veh.model,
                vehicle_year=veh.year,
                dtc_codes=wo.initial_dtc_codes or "",
                vehicle_engine_code=veh.engine_code or "",
                repair_summary="; ".join(items_by_wo.get(wo.id, [])),
            )
        )
    return out


@router.get(
    "/work-orders/{work_order_id}/receipt",
    response_model=InvoiceReceiptOut,
    summary="Ambil Ulang Nota/Invoice PKB yang Sudah Dibayar (Cetak Ulang)",
)
async def get_receipt_endpoint(
    work_order_id: int,
    db: AsyncSession = Depends(get_db),
    current_user: User = Depends(get_current_active_user),
) -> InvoiceReceiptOut:
    trx = (
        await db.execute(select(Transaction).where(Transaction.work_order_id == work_order_id))
    ).scalar_one_or_none()
    if not trx:
        raise HTTPException(status_code=404, detail="PKB ini belum memiliki invoice.")
    wo = (await db.execute(select(WorkOrder).where(WorkOrder.id == work_order_id))).scalar_one()
    veh = (await db.execute(select(Vehicle).where(Vehicle.id == wo.vehicle_id))).scalar_one()
    cust = (await db.execute(select(Customer).where(Customer.id == veh.customer_id))).scalar_one()
    items = (
        await db.execute(select(TransactionItem).where(TransactionItem.transaction_id == trx.id))
    ).scalars().all()
    return InvoiceReceiptOut(
        transaction_id=trx.id,
        invoice_number=trx.invoice_number,
        wo_number=wo.wo_number,
        customer_name=cust.name,
        vehicle_plate=veh.license_plate,
        vehicle_model=f"{veh.brand} {veh.model} ({veh.year})",
        subtotal_dpp=trx.subtotal,
        discount_amount=trx.discount_amount,
        tax_ppn_rate=trx.tax_ppn_rate,
        tax_ppn_amount=trx.tax_ppn_amount,
        grand_total=trx.grand_total,
        payment_method=trx.payment_method,
        payment_status=trx.payment_status,
        paid_at=trx.paid_at,
        line_items=[
            {
                "description": i.description,
                "item_type": i.item_type,
                "qty": i.qty,
                "unit_price": float(i.unit_price),
                "subtotal": float(i.subtotal),
            }
            for i in items
        ],
    )
