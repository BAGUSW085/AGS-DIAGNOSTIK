"""
Pydantic schemas for manual-related models: RepairManual, WiringDiagram, DTCCode, SensorSpec.
"""

from datetime import datetime

from pydantic import BaseModel, ConfigDict, Field


# ── RepairManual ──────────────────────────────────────────────────────────────

class RepairManualBase(BaseModel):
    """Shared repair manual fields."""
    brand: str = Field(..., max_length=50)
    model: str = Field(..., max_length=50)
    year_from: int = Field(..., ge=1900, le=2100)
    year_to: int | None = Field(default=None, ge=1900, le=2100)
    category: str = Field(..., max_length=30, description="engine, electrical, body, transmission, etc.")
    title: str = Field(..., max_length=255)
    content: str = Field(..., min_length=1, description="Full text content for RAG")
    file_path: str | None = Field(default=None, max_length=500)


class RepairManualCreate(RepairManualBase):
    """Schema for creating a repair manual entry."""
    pass


class RepairManualUpdate(BaseModel):
    """Schema for updating a repair manual — all optional."""
    brand: str | None = Field(default=None, max_length=50)
    model: str | None = Field(default=None, max_length=50)
    year_from: int | None = Field(default=None, ge=1900, le=2100)
    year_to: int | None = Field(default=None, ge=1900, le=2100)
    category: str | None = Field(default=None, max_length=30)
    title: str | None = Field(default=None, max_length=255)
    content: str | None = None
    file_path: str | None = None


class RepairManualResponse(RepairManualBase):
    """Repair manual returned to the client."""
    id: int
    created_at: datetime

    model_config = ConfigDict(from_attributes=True)


# ── WiringDiagram ─────────────────────────────────────────────────────────────

class WiringDiagramBase(BaseModel):
    """Shared wiring diagram fields."""
    brand: str = Field(..., max_length=50)
    model: str = Field(..., max_length=50)
    year_from: int = Field(..., ge=1900, le=2100)
    year_to: int | None = Field(default=None, ge=1900, le=2100)
    system_name: str = Field(..., max_length=100, description="ECU Main, ABS, Airbag, AC, Power Window")
    ecu_pinout: str = Field(..., description="JSON: {pin_number, signal_name, wire_color, description}")
    connector_info: str | None = None
    ground_points: str | None = None
    power_sources: str | None = None
    diagram_image_path: str | None = Field(default=None, max_length=500)
    notes: str | None = None


class WiringDiagramCreate(WiringDiagramBase):
    """Schema for creating a wiring diagram entry."""
    pass


class WiringDiagramResponse(WiringDiagramBase):
    """Wiring diagram returned to the client."""
    id: int
    created_at: datetime

    model_config = ConfigDict(from_attributes=True)


# ── DTCCode ───────────────────────────────────────────────────────────────────

class DTCCodeBase(BaseModel):
    """Shared DTC code fields."""
    code: str = Field(..., max_length=10, description="e.g. P0300, P0171, B1234")
    brand: str | None = Field(default=None, max_length=50, description="NULL = generic OBD-II")
    description_en: str = Field(..., max_length=255)
    description_id: str = Field(..., max_length=255, description="Indonesian description")
    possible_causes: str = Field(..., description="JSON array")
    diagnostic_steps: str = Field(..., description="JSON array of steps")
    sensor_specs: str | None = Field(default=None, description="JSON: standard sensor values")
    severity: str = Field(
        ..., pattern="^(low|medium|high|critical)$",
        description="low, medium, high, critical",
    )
    system_category: str = Field(
        ..., pattern="^(powertrain|body|chassis|network)$",
        description="powertrain, body, chassis, network",
    )


class DTCCodeCreate(DTCCodeBase):
    """Schema for creating a DTC code entry."""
    pass


class DTCCodeResponse(DTCCodeBase):
    """DTC code returned to the client."""
    id: int
    created_at: datetime

    model_config = ConfigDict(from_attributes=True)


# ── SensorSpec ────────────────────────────────────────────────────────────────

class SensorSpecBase(BaseModel):
    """Shared sensor spec fields."""
    brand: str = Field(..., max_length=50)
    model: str = Field(..., max_length=50)
    sensor_name: str = Field(..., max_length=100, description="TPS, MAP, O2 Sensor, Coolant Temp")
    normal_value_range: str = Field(..., max_length=50, description="e.g. 0.5V - 4.5V")
    unit: str = Field(..., max_length=10, description="V, kPa, Ω, °C")
    location: str | None = Field(default=None, max_length=200)
    notes: str | None = None


class SensorSpecCreate(SensorSpecBase):
    """Schema for creating a sensor spec entry."""
    pass


class SensorSpecResponse(SensorSpecBase):
    """Sensor spec returned to the client."""
    id: int

    model_config = ConfigDict(from_attributes=True)
