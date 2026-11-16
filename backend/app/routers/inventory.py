"""
Inventory / Sparepart management CRUD router.
"""

from fastapi import APIRouter, Depends, HTTPException, Query, status
from sqlalchemy import select, or_
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import selectinload

from app.database import get_db
from app.models.user import User
from app.models.inventory import Sparepart, StockMovement
from app.schemas.inventory import (
    SparepartCreate, SparepartResponse, SparepartUpdate,
    StockMovementCreate, StockMovementResponse,
)
from app.utils.deps import get_current_user

router = APIRouter(prefix="/inventory", tags=["Inventory"])


# ── Sparepart CRUD ───────────────────────────────────────────────────────────

@router.get("/", response_model=list[SparepartResponse])
async def list_spareparts(
    search: str | None = Query(None, description="Cari nama atau part number"),
    category: str | None = Query(None),
    low_stock: bool = Query(False, description="Hanya tampilkan stok menipis"),
    db: AsyncSession = Depends(get_db),
    _user: User = Depends(get_current_user),
):
    """List spareparts with optional search and filters."""
    stmt = select(Sparepart).where(Sparepart.is_active == True).order_by(Sparepart.name)
    if search:
        stmt = stmt.where(
            or_(
                Sparepart.name.ilike(f"%{search}%"),
                Sparepart.part_number.ilike(f"%{search}%"),
            )
        )
    if category:
        stmt = stmt.where(Sparepart.category == category)
    if low_stock:
        stmt = stmt.where(Sparepart.stock_quantity <= Sparepart.min_stock)
    result = await db.execute(stmt)
    return result.scalars().all()


@router.post("/", response_model=SparepartResponse, status_code=201)
async def create_sparepart(
    data: SparepartCreate,
    db: AsyncSession = Depends(get_db),
    _user: User = Depends(get_current_user),
):
    """Add a new sparepart to inventory."""
    # Check duplicate part number
    existing = await db.execute(
        select(Sparepart).where(Sparepart.part_number == data.part_number)
    )
    if existing.scalar_one_or_none():
        raise HTTPException(status_code=409, detail="Part number sudah ada")

    part = Sparepart(**data.model_dump())
    db.add(part)
    await db.flush()
    await db.refresh(part)
    return part


@router.get("/{part_id}", response_model=SparepartResponse)
async def get_sparepart(
    part_id: int,
    db: AsyncSession = Depends(get_db),
    _user: User = Depends(get_current_user),
):
    """Get sparepart details."""
    result = await db.execute(select(Sparepart).where(Sparepart.id == part_id))
    part = result.scalar_one_or_none()
    if not part:
        raise HTTPException(status_code=404, detail="Sparepart tidak ditemukan")
    return part


@router.put("/{part_id}", response_model=SparepartResponse)
async def update_sparepart(
    part_id: int,
    data: SparepartUpdate,
    db: AsyncSession = Depends(get_db),
    _user: User = Depends(get_current_user),
):
    """Update sparepart info."""
    result = await db.execute(select(Sparepart).where(Sparepart.id == part_id))
    part = result.scalar_one_or_none()
    if not part:
        raise HTTPException(status_code=404, detail="Sparepart tidak ditemukan")

    for field, value in data.model_dump(exclude_unset=True).items():
        setattr(part, field, value)
    await db.flush()
    await db.refresh(part)
    return part


# ── Stock Movements ──────────────────────────────────────────────────────────

@router.get("/{part_id}/movements", response_model=list[StockMovementResponse])
async def list_stock_movements(
    part_id: int,
    limit: int = Query(50, le=200),
    db: AsyncSession = Depends(get_db),
    _user: User = Depends(get_current_user),
):
    """List stock movements for a sparepart."""
    stmt = (
        select(StockMovement)
        .where(StockMovement.sparepart_id == part_id)
        .order_by(StockMovement.created_at.desc())
        .limit(limit)
    )
    result = await db.execute(stmt)
    return result.scalars().all()


@router.post("/movements", response_model=StockMovementResponse, status_code=201)
async def create_stock_movement(
    data: StockMovementCreate,
    db: AsyncSession = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    """
    Record a stock movement and auto-update sparepart quantity.
    - 'in' / 'return': adds to stock
    - 'out': subtracts from stock
    - 'adjustment': sets stock to the given quantity (absolute)
    """
    result = await db.execute(
        select(Sparepart).where(Sparepart.id == data.sparepart_id)
    )
    part = result.scalar_one_or_none()
    if not part:
        raise HTTPException(status_code=404, detail="Sparepart tidak ditemukan")

    # Update stock quantity
    if data.movement_type in ("in", "return"):
        part.stock_quantity += data.quantity
    elif data.movement_type == "out":
        if part.stock_quantity < data.quantity:
            raise HTTPException(
                status_code=400,
                detail=f"Stok tidak cukup. Stok saat ini: {part.stock_quantity}",
            )
        part.stock_quantity -= data.quantity
    elif data.movement_type == "adjustment":
        part.stock_quantity = data.quantity

    movement = StockMovement(
        **data.model_dump(),
        user_id=current_user.id,
    )
    db.add(movement)
    await db.flush()
    await db.refresh(movement)
    return movement
