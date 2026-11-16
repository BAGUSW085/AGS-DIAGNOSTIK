"""
Pydantic schemas for diagnostic-related models.
"""

from datetime import datetime

from pydantic import BaseModel, ConfigDict, Field


# ── FaultCategory ─────────────────────────────────────────────────────────────

class FaultCategoryBase(BaseModel):
    """Shared fault category fields."""
    name: str = Field(..., min_length=1, max_length=50)
    description: str | None = Field(default=None, max_length=255)


class FaultCategoryCreate(FaultCategoryBase):
    """Schema for creating a fault category."""
    pass


class FaultCategoryResponse(FaultCategoryBase):
    """Fault category returned to the client."""
    id: int

    model_config = ConfigDict(from_attributes=True)


# ── FaultHistory ──────────────────────────────────────────────────────────────

class FaultHistoryBase(BaseModel):
    """Shared fault history fields."""
    vehicle_id: int
    category_id: int
    reported_symptoms: str = Field(..., min_length=1, description="Gejala yang dilaporkan customer")
    diagnosed_cause: str = Field(..., min_length=1, description="Penyebab sebenarnya")
    solution: str = Field(..., min_length=1, description="Solusi / perbaikan yang dilakukan")
    checkpoint_sequence: str | None = Field(
        default=None, description="JSON array of checkpoint steps taken",
    )
    mechanic_id: int | None = None
    mileage_km: int | None = Field(default=None, ge=0)
    repair_cost: float | None = Field(default=None, ge=0)
    resolved: bool = True


class FaultHistoryCreate(FaultHistoryBase):
    """Schema for recording a new fault history."""
    pass


class FaultHistoryUpdate(BaseModel):
    """Schema for updating fault history — all optional."""
    category_id: int | None = None
    reported_symptoms: str | None = None
    diagnosed_cause: str | None = None
    solution: str | None = None
    checkpoint_sequence: str | None = None
    mechanic_id: int | None = None
    mileage_km: int | None = None
    repair_cost: float | None = None
    resolved: bool | None = None


class FaultHistoryResponse(FaultHistoryBase):
    """Fault history returned to the client."""
    id: int
    created_at: datetime

    model_config = ConfigDict(from_attributes=True)


# ── FaultCheckpoint ───────────────────────────────────────────────────────────

class FaultCheckpointBase(BaseModel):
    """Shared fault checkpoint fields."""
    category_id: int
    name: str = Field(..., min_length=1, max_length=100)
    description: str = Field(..., min_length=1)
    order_priority: int = Field(..., ge=0, description="Default check order")


class FaultCheckpointCreate(FaultCheckpointBase):
    """Schema for creating a fault checkpoint."""
    pass


class FaultCheckpointResponse(FaultCheckpointBase):
    """Fault checkpoint returned to the client."""
    id: int

    model_config = ConfigDict(from_attributes=True)


# ── SymptomCheckpointLink ────────────────────────────────────────────────────

class SymptomCheckpointLinkBase(BaseModel):
    """Shared symptom-checkpoint link fields."""
    fault_history_id: int
    checkpoint_id: int
    was_cause: bool = Field(..., description="True if this checkpoint found the actual cause")
    notes: str | None = None


class SymptomCheckpointLinkCreate(SymptomCheckpointLinkBase):
    """Schema for creating a symptom-checkpoint link."""
    pass


class SymptomCheckpointLinkResponse(SymptomCheckpointLinkBase):
    """Symptom-checkpoint link returned to the client."""
    id: int

    model_config = ConfigDict(from_attributes=True)
