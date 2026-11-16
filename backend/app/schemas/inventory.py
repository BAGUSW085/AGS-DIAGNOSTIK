"""
Pydantic schemas for Sparepart and StockMovement models.
"""

from datetime import datetime

from pydantic import BaseModel, ConfigDict, Field


# ── Sparepart ─────────────────────────────────────────────────────────────────

class SparepartBase(BaseModel):
    """Shared sparepart fields."""
    part_number: str = Field(..., max_length=50)
    name: str = Field(..., max_length=150)
    brand: str | None = Field(default=None, max_length=50)
    category: str = Field(
        ..., max_length=30,
        description="filter, brake, electrical, engine, body, etc.",
    )
    compatible_vehicles: str | None = Field(
        default=None,
        description="JSON array of {brand, model, year_from, year_to}",
    )
    buy_price: float = Field(..., ge=0)
    sell_price: float = Field(..., ge=0)
    stock_quantity: int = Field(default=0, ge=0)
    min_stock: int = Field(default=2, ge=0, description="Alert threshold")
    location: str | None = Field(default=None, max_length=50, description="Shelf/rack location")
    supplier: str | None = Field(default=None, max_length=100)
    unit: str = Field(default="pcs", max_length=10, description="pcs, liter, set, meter")
    is_active: bool = True


class SparepartCreate(SparepartBase):
    """Schema for creating a sparepart."""
    pass


class SparepartUpdate(BaseModel):
    """Schema for updating a sparepart — all optional."""
    part_number: str | None = Field(default=None, max_length=50)
    name: str | None = Field(default=None, max_length=150)
    brand: str | None = None
    category: str | None = Field(default=None, max_length=30)
    compatible_vehicles: str | None = None
    buy_price: float | None = Field(default=None, ge=0)
    sell_price: float | None = Field(default=None, ge=0)
    stock_quantity: int | None = Field(default=None, ge=0)
    min_stock: int | None = Field(default=None, ge=0)
    location: str | None = None
    supplier: str | None = None
    unit: str | None = Field(default=None, max_length=10)
    is_active: bool | None = None


class SparepartResponse(SparepartBase):
    """Sparepart returned to the client."""
    id: int
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)


# ── StockMovement ─────────────────────────────────────────────────────────────

class StockMovementBase(BaseModel):
    """Shared stock movement fields."""
    sparepart_id: int
    movement_type: str = Field(
        ..., pattern="^(in|out|adjustment|return)$",
        description="in, out, adjustment, return",
    )
    quantity: int = Field(..., ge=1, description="Quantity to move")
    reference_type: str | None = Field(
        default=None, max_length=20,
        description="purchase, work_order, manual",
    )
    reference_id: int | None = None
    notes: str | None = Field(default=None, max_length=255)


class StockMovementCreate(StockMovementBase):
    """Schema for creating a stock movement (user_id set from JWT)."""
    pass


class StockMovementResponse(StockMovementBase):
    """Stock movement returned to the client."""
    id: int
    user_id: int
    created_at: datetime

    model_config = ConfigDict(from_attributes=True)
