"""
Repair-manual-related ORM models: RepairManual, WiringDiagram, DTCCode, SensorSpec.
"""

from datetime import datetime, timezone

from sqlalchemy import DateTime, Integer, String, Text
from sqlalchemy.orm import Mapped, mapped_column

from app.database import Base


class RepairManual(Base):
    """Full-text repair manual entry used for RAG retrieval."""

    __tablename__ = "repair_manuals"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    brand: Mapped[str] = mapped_column(String(50), index=True, nullable=False)
    model: Mapped[str] = mapped_column(String(50), index=True, nullable=False)
    year_from: Mapped[int] = mapped_column(Integer, nullable=False)
    year_to: Mapped[int | None] = mapped_column(Integer, nullable=True)
    category: Mapped[str] = mapped_column(
        String(30), nullable=False, comment="engine, electrical, body, transmission, etc.",
    )
    title: Mapped[str] = mapped_column(String(255), nullable=False)
    content: Mapped[str] = mapped_column(
        Text, nullable=False, comment="Full text content for RAG",
    )
    file_path: Mapped[str | None] = mapped_column(
        String(500), nullable=True, comment="Path to PDF if available",
    )
    created_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True), default=lambda: datetime.now(timezone.utc), nullable=False,
    )

    def __repr__(self) -> str:
        return f"<RepairManual(id={self.id}, brand='{self.brand}', model='{self.model}', title='{self.title}')>"


class WiringDiagram(Base):
    """Wiring diagram and ECU pinout data for a specific vehicle system."""

    __tablename__ = "wiring_diagrams"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    brand: Mapped[str] = mapped_column(String(50), index=True, nullable=False)
    model: Mapped[str] = mapped_column(String(50), index=True, nullable=False)
    year_from: Mapped[int] = mapped_column(Integer, nullable=False)
    year_to: Mapped[int | None] = mapped_column(Integer, nullable=True)
    system_name: Mapped[str] = mapped_column(
        String(100), nullable=False,
        comment="ECU Main, ABS, Airbag, AC, Power Window, etc.",
    )
    ecu_pinout: Mapped[str] = mapped_column(
        Text, nullable=False,
        comment="JSON: {pin_number, signal_name, wire_color, description}",
    )
    connector_info: Mapped[str | None] = mapped_column(
        Text, nullable=True, comment="JSON connector details",
    )
    ground_points: Mapped[str | None] = mapped_column(
        Text, nullable=True, comment="JSON ground point locations",
    )
    power_sources: Mapped[str | None] = mapped_column(
        Text, nullable=True, comment="JSON power source details",
    )
    diagram_image_path: Mapped[str | None] = mapped_column(String(500), nullable=True)
    notes: Mapped[str | None] = mapped_column(Text, nullable=True)
    created_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True), default=lambda: datetime.now(timezone.utc), nullable=False,
    )

    def __repr__(self) -> str:
        return f"<WiringDiagram(id={self.id}, brand='{self.brand}', system='{self.system_name}')>"


class DTCCode(Base):
    """Diagnostic Trouble Code (DTC) reference with causes and repair steps."""

    __tablename__ = "dtc_codes"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    code: Mapped[str] = mapped_column(
        String(10), unique=True, index=True, nullable=False,
        comment="e.g. P0300, P0171, B1234",
    )
    brand: Mapped[str | None] = mapped_column(
        String(50), nullable=True, comment="NULL = generic OBD-II",
    )
    description_en: Mapped[str] = mapped_column(String(255), nullable=False)
    description_id: Mapped[str] = mapped_column(
        String(255), nullable=False, comment="Indonesian description",
    )
    possible_causes: Mapped[str] = mapped_column(
        Text, nullable=False, comment="JSON array",
    )
    diagnostic_steps: Mapped[str] = mapped_column(
        Text, nullable=False, comment="JSON array of steps",
    )
    sensor_specs: Mapped[str | None] = mapped_column(
        Text, nullable=True, comment="JSON: standard sensor values",
    )
    severity: Mapped[str] = mapped_column(
        String(10), nullable=False, comment="low, medium, high, critical",
    )
    system_category: Mapped[str] = mapped_column(
        String(20), nullable=False, comment="powertrain, body, chassis, network",
    )
    created_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True), default=lambda: datetime.now(timezone.utc), nullable=False,
    )

    def __repr__(self) -> str:
        return f"<DTCCode(id={self.id}, code='{self.code}', severity='{self.severity}')>"


class SensorSpec(Base):
    """Reference specification for vehicle sensors with normal value ranges."""

    __tablename__ = "sensor_specs"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    brand: Mapped[str] = mapped_column(String(50), nullable=False)
    model: Mapped[str] = mapped_column(String(50), nullable=False)
    sensor_name: Mapped[str] = mapped_column(
        String(100), nullable=False, comment="TPS, MAP, O2 Sensor, Coolant Temp",
    )
    normal_value_range: Mapped[str] = mapped_column(
        String(50), nullable=False, comment="e.g. 0.5V - 4.5V",
    )
    unit: Mapped[str] = mapped_column(
        String(10), nullable=False, comment="V, kPa, Ω, °C",
    )
    location: Mapped[str | None] = mapped_column(String(200), nullable=True)
    notes: Mapped[str | None] = mapped_column(Text, nullable=True)

    def __repr__(self) -> str:
        return f"<SensorSpec(id={self.id}, sensor='{self.sensor_name}', range='{self.normal_value_range}')>"
