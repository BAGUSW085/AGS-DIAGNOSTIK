"""
Work Orders (PKB) CRUD router.
"""

from fastapi import APIRouter, Depends, HTTPException, Query, status
from sqlalchemy import select, or_
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import selectinload

from app.database import get_db
from app.models.user import User
from app.models.vehicle import Vehicle, Customer
from app.models.workshop import WorkOrder, WorkOrderItem
from app.schemas.workshop import (
    WorkOrderCreate, WorkOrderResponse, WorkOrderUpdate,
    WorkOrderItemCreate, WorkOrderItemResponse,
)
from app.utils.deps import get_current_user
from app.utils.helpers import generate_order_number

router = APIRouter(prefix="/work-orders", tags=["Work Orders"])


@router.get("/", response_model=list[WorkOrderResponse])
async def list_work_orders(
    status_filter: str | None = Query(None, alias="status", description="Filter by status"),
    vehicle_id: int | None = Query(None),
    limit: int = Query(50, le=200),
    db: AsyncSession = Depends(get_db),
    _user: User = Depends(get_current_user),
):
    """List work orders with optional filters."""
    stmt = (
        select(WorkOrder)
        .options(selectinload(WorkOrder.items))
        .order_by(WorkOrder.created_at.desc())
        .limit(limit)
    )
    if status_filter:
        stmt = stmt.where(WorkOrder.status == status_filter)
    if vehicle_id:
        stmt = stmt.where(WorkOrder.vehicle_id == vehicle_id)
    result = await db.execute(stmt)
    return result.scalars().unique().all()


@router.post("/", response_model=WorkOrderResponse, status_code=201)
async def create_work_order(
    data: WorkOrderCreate,
    db: AsyncSession = Depends(get_db),
    _user: User = Depends(get_current_user),
):
    """Create a new work order (PKB)."""
    # Verify vehicle exists
    v = await db.execute(select(Vehicle).where(Vehicle.id == data.vehicle_id))
    if not v.scalar_one_or_none():
        raise HTTPException(status_code=404, detail="Kendaraan tidak ditemukan")

    order_number = await generate_order_number(db, "WO", WorkOrder)

    wo = WorkOrder(
        order_number=order_number,
        **data.model_dump(),
    )
    db.add(wo)
    await db.flush()
    await db.refresh(wo, attribute_names=["items"])
    return wo


@router.get("/{wo_id}", response_model=WorkOrderResponse)
async def get_work_order(
    wo_id: int,
    db: AsyncSession = Depends(get_db),
    _user: User = Depends(get_current_user),
):
    """Get work order details by ID."""
    result = await db.execute(
        select(WorkOrder)
        .options(selectinload(WorkOrder.items))
        .where(WorkOrder.id == wo_id)
    )
    wo = result.scalar_one_or_none()
    if not wo:
        raise HTTPException(status_code=404, detail="Work Order tidak ditemukan")
    return wo


@router.put("/{wo_id}", response_model=WorkOrderResponse)
async def update_work_order(
    wo_id: int,
    data: WorkOrderUpdate,
    db: AsyncSession = Depends(get_db),
    _user: User = Depends(get_current_user),
):
    """Update work order status and details."""
    result = await db.execute(
        select(WorkOrder)
        .options(selectinload(WorkOrder.items))
        .where(WorkOrder.id == wo_id)
    )
    wo = result.scalar_one_or_none()
    if not wo:
        raise HTTPException(status_code=404, detail="Work Order tidak ditemukan")

    for field, value in data.model_dump(exclude_unset=True).items():
        setattr(wo, field, value)
    await db.flush()
    await db.refresh(wo, attribute_names=["items"])
    return wo


# ── Work Order Items ─────────────────────────────────────────────────────────

@router.post("/{wo_id}/items", response_model=WorkOrderItemResponse, status_code=201)
async def add_work_order_item(
    wo_id: int,
    data: WorkOrderItemCreate,
    db: AsyncSession = Depends(get_db),
    _user: User = Depends(get_current_user),
):
    """Add a service or sparepart line item to a work order."""
    result = await db.execute(select(WorkOrder).where(WorkOrder.id == wo_id))
    if not result.scalar_one_or_none():
        raise HTTPException(status_code=404, detail="Work Order tidak ditemukan")

    # Calculate subtotal
    subtotal = data.quantity * data.unit_price * (1 - data.discount_percent / 100)

    item = WorkOrderItem(
        work_order_id=wo_id,
        **data.model_dump(),
        subtotal=subtotal,
    )
    db.add(item)
    await db.flush()
    await db.refresh(item)
    return item


@router.delete("/{wo_id}/items/{item_id}", status_code=204)
async def delete_work_order_item(
    wo_id: int,
    item_id: int,
    db: AsyncSession = Depends(get_db),
    _user: User = Depends(get_current_user),
):
    """Remove a line item from a work order."""
    result = await db.execute(
        select(WorkOrderItem).where(
            WorkOrderItem.id == item_id,
            WorkOrderItem.work_order_id == wo_id,
        )
    )
    item = result.scalar_one_or_none()
    if not item:
        raise HTTPException(status_code=404, detail="Item tidak ditemukan")
    await db.delete(item)
