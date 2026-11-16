"""
POS / Transaction router — invoice generation, payment processing.
"""

from fastapi import APIRouter, Depends, HTTPException, Query, status
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import selectinload

from app.database import get_db
from app.models.user import User
from app.models.workshop import WorkOrder, WorkOrderItem
from app.models.inventory import Sparepart, StockMovement
from app.models.transaction import Transaction, TransactionItem
from app.schemas.transaction import (
    TransactionCreate, TransactionResponse, TransactionPayment,
)
from app.utils.deps import get_current_user, require_roles
from app.utils.helpers import generate_order_number

router = APIRouter(prefix="/transactions", tags=["Transactions / POS"])


@router.get("/", response_model=list[TransactionResponse])
async def list_transactions(
    payment_status: str | None = Query(None),
    customer_id: int | None = Query(None),
    limit: int = Query(50, le=200),
    db: AsyncSession = Depends(get_db),
    _user: User = Depends(get_current_user),
):
    """List transactions with optional filters."""
    stmt = (
        select(Transaction)
        .options(selectinload(Transaction.items))
        .order_by(Transaction.created_at.desc())
        .limit(limit)
    )
    if payment_status:
        stmt = stmt.where(Transaction.payment_status == payment_status)
    if customer_id:
        stmt = stmt.where(Transaction.customer_id == customer_id)
    result = await db.execute(stmt)
    return result.scalars().unique().all()


@router.post("/from-work-order/{wo_id}", response_model=TransactionResponse, status_code=201)
async def create_transaction_from_wo(
    wo_id: int,
    tax_percent: float = Query(11.0, description="PPN percentage"),
    discount_amount: float = Query(0.0, description="Diskon total (Rp)"),
    db: AsyncSession = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    """
    Generate an invoice/transaction from a completed Work Order.
    Auto-creates TransactionItems from WorkOrderItems and deducts sparepart stock.
    """
    # Fetch work order with items
    result = await db.execute(
        select(WorkOrder)
        .options(selectinload(WorkOrder.items))
        .where(WorkOrder.id == wo_id)
    )
    wo = result.scalar_one_or_none()
    if not wo:
        raise HTTPException(status_code=404, detail="Work Order tidak ditemukan")

    if wo.status not in ("completed", "in_progress"):
        raise HTTPException(
            status_code=400,
            detail=f"Work Order status '{wo.status}' belum bisa di-invoice. Selesaikan terlebih dahulu.",
        )

    # Check if already invoiced
    existing_tx = await db.execute(
        select(Transaction).where(Transaction.work_order_id == wo_id)
    )
    if existing_tx.scalar_one_or_none():
        raise HTTPException(status_code=409, detail="Work Order sudah memiliki invoice")

    # Calculate totals
    subtotal = sum(item.subtotal for item in wo.items)
    tax_amount = subtotal * tax_percent / 100
    grand_total = subtotal + tax_amount - discount_amount

    invoice_number = await generate_order_number(db, "INV", Transaction)

    # Create transaction
    tx = Transaction(
        invoice_number=invoice_number,
        work_order_id=wo.id,
        customer_id=wo.customer_id,
        subtotal=round(subtotal, 0),
        tax_percent=tax_percent,
        tax_amount=round(tax_amount, 0),
        discount_amount=round(discount_amount, 0),
        grand_total=round(grand_total, 0),
        payment_method="cash",
        payment_status="unpaid",
        cashier_id=current_user.id,
    )
    db.add(tx)
    await db.flush()

    # Create transaction items from work order items
    for wo_item in wo.items:
        tx_item = TransactionItem(
            transaction_id=tx.id,
            item_type=wo_item.item_type,
            description=wo_item.description,
            sparepart_id=wo_item.sparepart_id,
            quantity=wo_item.quantity,
            unit_price=wo_item.unit_price,
            discount_percent=wo_item.discount_percent,
            subtotal=wo_item.subtotal,
        )
        db.add(tx_item)

        # Auto-deduct sparepart stock
        if wo_item.sparepart_id:
            part_result = await db.execute(
                select(Sparepart).where(Sparepart.id == wo_item.sparepart_id)
            )
            part = part_result.scalar_one_or_none()
            if part:
                part.stock_quantity = max(0, part.stock_quantity - int(wo_item.quantity))
                # Log stock movement
                movement = StockMovement(
                    sparepart_id=part.id,
                    movement_type="out",
                    quantity=int(wo_item.quantity),
                    reference_type="work_order",
                    reference_id=wo.id,
                    notes=f"Auto-deduct dari WO {wo.order_number}",
                    user_id=current_user.id,
                )
                db.add(movement)

    # Update work order status
    wo.status = "invoiced"

    await db.flush()
    await db.refresh(tx, attribute_names=["items"])
    return tx


@router.post("/{tx_id}/pay", response_model=TransactionResponse)
async def process_payment(
    tx_id: int,
    payment: TransactionPayment,
    db: AsyncSession = Depends(get_db),
    _user: User = Depends(require_roles("admin", "kasir")),
):
    """Process payment for a transaction."""
    result = await db.execute(
        select(Transaction)
        .options(selectinload(Transaction.items))
        .where(Transaction.id == tx_id)
    )
    tx = result.scalar_one_or_none()
    if not tx:
        raise HTTPException(status_code=404, detail="Transaksi tidak ditemukan")

    if tx.payment_status == "paid":
        raise HTTPException(status_code=400, detail="Transaksi sudah lunas")

    tx.payment_method = payment.payment_method
    tx.paid_amount = payment.paid_amount
    tx.change_amount = max(0, payment.paid_amount - tx.grand_total)
    tx.payment_status = "paid" if payment.paid_amount >= tx.grand_total else "partial"
    if payment.notes:
        tx.notes = payment.notes

    await db.flush()
    await db.refresh(tx, attribute_names=["items"])
    return tx


@router.get("/{tx_id}", response_model=TransactionResponse)
async def get_transaction(
    tx_id: int,
    db: AsyncSession = Depends(get_db),
    _user: User = Depends(get_current_user),
):
    """Get transaction/invoice details."""
    result = await db.execute(
        select(Transaction)
        .options(selectinload(Transaction.items))
        .where(Transaction.id == tx_id)
    )
    tx = result.scalar_one_or_none()
    if not tx:
        raise HTTPException(status_code=404, detail="Transaksi tidak ditemukan")
    return tx
