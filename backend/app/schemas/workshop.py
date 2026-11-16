"""
Pydantic schemas for WorkOrder and WorkOrderItem models.
"""

from datetime import datetime

from pydantic import BaseModel, ConfigDict, Field


# ── WorkOrder ─────────────────────────────────────────────────────────────────

class WorkOrderBase(BaseModel):
    """Shared work order fields."""
    vehicle_id: int
    customer_id: int
    service_advisor_id: int | None = None
    mechanic_id: int | None = None
    complaint: str = Field(..., min_length=1, description="Keluhan customer")
    diagnosis: str | None = None
    status: str = Field(
        default="pending",
        pattern="^(pending|in_progress|waiting_parts|completed|invoiced|cancelled)$",
        description="Work order status",
    )
    estimated_completion: datetime | None = None
    actual_completion: datetime | None = None
    mileage_km: int | None = Field(default=None, ge=0)
    notes: str | None = None


class WorkOrderCreate(WorkOrderBase):
    """Schema for creating a work order."""
    pass


class WorkOrderUpdate(BaseModel):
    """Schema for updating a work order — all optional."""
    vehicle_id: int | None = None
    customer_id: int | None = None
    service_advisor_id: int | None = None
    mechanic_id: int | None = None
    complaint: str | None = None
    diagnosis: str | None = None
    status: str | None = Field(
        default=None,
        pattern="^(pending|in_progress|waiting_parts|completed|invoiced|cancelled)$",
    )
    estimated_completion: datetime | None = None
    actual_completion: datetime | None = None
    mileage_km: int | None = None
    notes: str | None = None


class WorkOrderResponse(WorkOrderBase):
    """Work order returned to the client."""
    id: int
    order_number: str
    created_at: datetime
    updated_at: datetime
    items: list[WorkOrderItemResponse] = []

    model_config = ConfigDict(from_attributes=True)


# ── WorkOrderItem ─────────────────────────────────────────────────────────────

class WorkOrderItemBase(BaseModel):
    """Shared work order item fields."""
    item_type: str = Field(
        ..., pattern="^(service|sparepart)$", description="service or sparepart",
    )
    description: str = Field(..., max_length=255)
    sparepart_id: int | None = None
    quantity: float = Field(default=1, ge=0)
    unit_price: float = Field(..., ge=0)
    discount_percent: float = Field(default=0, ge=0, le=100)
    notes: str | None = Field(default=None, max_length=255)


class WorkOrderItemCreate(WorkOrderItemBase):
    """Schema for creating a work order item."""
    pass


class WorkOrderItemResponse(WorkOrderItemBase):
    """Work order item returned to the client."""
    id: int
    work_order_id: int
    subtotal: float

    model_config = ConfigDict(from_attributes=True)
