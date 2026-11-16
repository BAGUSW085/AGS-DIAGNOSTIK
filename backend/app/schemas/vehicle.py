"""
Pydantic schemas for Customer and Vehicle models.
"""

from datetime import datetime

from pydantic import BaseModel, ConfigDict, Field


# ── Customer ──────────────────────────────────────────────────────────────────

class CustomerBase(BaseModel):
    """Shared customer fields."""
    name: str = Field(..., min_length=1, max_length=100)
    phone: str = Field(..., min_length=5, max_length=20)
    email: str | None = Field(default=None, max_length=100)
    address: str | None = None


class CustomerCreate(CustomerBase):
    """Schema for creating a new customer."""
    pass


class CustomerUpdate(BaseModel):
    """Schema for updating customer fields — all optional."""
    name: str | None = Field(default=None, min_length=1, max_length=100)
    phone: str | None = Field(default=None, min_length=5, max_length=20)
    email: str | None = Field(default=None, max_length=100)
    address: str | None = None


class CustomerResponse(CustomerBase):
    """Customer data returned to the client."""
    id: int
    created_at: datetime

    model_config = ConfigDict(from_attributes=True)


# ── Vehicle ───────────────────────────────────────────────────────────────────

class VehicleBase(BaseModel):
    """Shared vehicle fields."""
    customer_id: int
    plate_number: str = Field(..., min_length=1, max_length=15, description="Nomor polisi")
    brand: str = Field(..., min_length=1, max_length=50)
    model: str = Field(..., min_length=1, max_length=50)
    year: int = Field(..., ge=1900, le=2100)
    engine_code: str | None = Field(default=None, max_length=20)
    vin: str | None = Field(default=None, max_length=17)
    transmission: str = Field(
        ..., pattern="^(manual|automatic|cvt)$",
        description="manual, automatic, cvt",
    )
    fuel_type: str = Field(
        ..., pattern="^(bensin|diesel|hybrid|electric)$",
        description="bensin, diesel, hybrid, electric",
    )
    notes: str | None = None


class VehicleCreate(VehicleBase):
    """Schema for creating a new vehicle."""
    pass


class VehicleUpdate(BaseModel):
    """Schema for updating vehicle fields — all optional."""
    customer_id: int | None = None
    plate_number: str | None = Field(default=None, min_length=1, max_length=15)
    brand: str | None = Field(default=None, min_length=1, max_length=50)
    model: str | None = Field(default=None, min_length=1, max_length=50)
    year: int | None = Field(default=None, ge=1900, le=2100)
    engine_code: str | None = None
    vin: str | None = None
    transmission: str | None = Field(default=None, pattern="^(manual|automatic|cvt)$")
    fuel_type: str | None = Field(default=None, pattern="^(bensin|diesel|hybrid|electric)$")
    notes: str | None = None


class VehicleResponse(VehicleBase):
    """Vehicle data returned to the client."""
    id: int
    created_at: datetime

    model_config = ConfigDict(from_attributes=True)
