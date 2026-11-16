"""
Pydantic schemas for Transaction and TransactionItem models.
"""

from datetime import datetime

from pydantic import BaseModel, ConfigDict, Field


# ── Transaction ───────────────────────────────────────────────────────────────

class TransactionBase(BaseModel):
    """Shared transaction fields."""
    work_order_id: int | None = None
    customer_id: int
    subtotal: float = Field(..., ge=0)
    tax_percent: float = Field(default=11, ge=0, le=100, description="PPN 11%")
    tax_amount: float = Field(..., ge=0)
    discount_amount: float = Field(default=0, ge=0)
    grand_total: float = Field(..., ge=0)
    payment_method: str = Field(
        ..., pattern="^(cash|transfer|debit|credit|qris)$",
        description="cash, transfer, debit, credit, qris",
    )
    payment_status: str = Field(
        default="unpaid", pattern="^(unpaid|partial|paid)$",
        description="unpaid, partial, paid",
    )
    paid_amount: float = Field(default=0, ge=0)
    change_amount: float = Field(default=0, ge=0)
    cashier_id: int
    notes: str | None = None


class TransactionCreate(TransactionBase):
    """Schema for creating a transaction."""
    items: list["TransactionItemCreate"] = Field(
        ..., min_length=1, description="At least one transaction item required",
    )


class TransactionPayment(BaseModel):
    """Schema for processing a payment on an existing transaction."""
    payment_method: str = Field(
        ..., pattern="^(cash|transfer|debit|credit|qris)$",
        description="cash, transfer, debit, credit, qris",
    )
    paid_amount: float = Field(..., ge=0, description="Jumlah yang dibayar")
    notes: str | None = None


class TransactionResponse(TransactionBase):
    """Transaction returned to the client."""
    id: int
    invoice_number: str
    created_at: datetime
    items: list["TransactionItemResponse"] = []

    model_config = ConfigDict(from_attributes=True)


# ── TransactionItem ───────────────────────────────────────────────────────────

class TransactionItemBase(BaseModel):
    """Shared transaction item fields."""
    item_type: str = Field(
        ..., pattern="^(service|sparepart)$", description="service or sparepart",
    )
    description: str = Field(..., max_length=255)
    sparepart_id: int | None = None
    quantity: float = Field(..., ge=0)
    unit_price: float = Field(..., ge=0)
    discount_percent: float = Field(default=0, ge=0, le=100)
    subtotal: float = Field(..., ge=0)


class TransactionItemCreate(TransactionItemBase):
    """Schema for creating a transaction item."""
    pass


class TransactionItemResponse(TransactionItemBase):
    """Transaction item returned to the client."""
    id: int
    transaction_id: int

    model_config = ConfigDict(from_attributes=True)
