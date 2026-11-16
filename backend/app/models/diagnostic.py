"""
Diagnostic-related ORM models: FaultCategory, FaultHistory, FaultCheckpoint, SymptomCheckpointLink.
"""

from datetime import datetime, timezone

from sqlalchemy import Boolean, DateTime, Float, ForeignKey, Integer, String, Text
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.database import Base


class FaultCategory(Base):
    """Top-level fault category such as Engine, Electrical, Transmission, AC, Brake."""

    __tablename__ = "fault_categories"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    name: Mapped[str] = mapped_column(String(50), unique=True, nullable=False)
    description: Mapped[str | None] = mapped_column(String(255), nullable=True)

    # Relationships
    histories: Mapped[list["FaultHistory"]] = relationship("FaultHistory", back_populates="category")
    checkpoints: Mapped[list["FaultCheckpoint"]] = relationship("FaultCheckpoint", back_populates="category")

    def __repr__(self) -> str:
        return f"<FaultCategory(id={self.id}, name='{self.name}')>"


class FaultHistory(Base):
    """Historical record of a diagnosed and resolved fault on a vehicle."""

    __tablename__ = "fault_histories"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    vehicle_id: Mapped[int] = mapped_column(
        Integer, ForeignKey("vehicles.id"), nullable=False,
    )
    category_id: Mapped[int] = mapped_column(
        Integer, ForeignKey("fault_categories.id"), nullable=False,
    )
    reported_symptoms: Mapped[str] = mapped_column(
        Text, nullable=False, comment="Gejala yang dilaporkan customer",
    )
    diagnosed_cause: Mapped[str] = mapped_column(
        Text, nullable=False, comment="Penyebab sebenarnya",
    )
    solution: Mapped[str] = mapped_column(
        Text, nullable=False, comment="Solusi / perbaikan yang dilakukan",
    )
    checkpoint_sequence: Mapped[str | None] = mapped_column(
        Text, nullable=True, comment="JSON array of checkpoint steps taken",
    )
    mechanic_id: Mapped[int | None] = mapped_column(
        Integer, ForeignKey("users.id"), nullable=True,
    )
    mileage_km: Mapped[int | None] = mapped_column(Integer, nullable=True)
    repair_cost: Mapped[float | None] = mapped_column(Float, nullable=True)
    resolved: Mapped[bool] = mapped_column(Boolean, default=True, nullable=False)
    created_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True), default=lambda: datetime.now(timezone.utc), nullable=False,
    )

    # Relationships
    category: Mapped["FaultCategory"] = relationship("FaultCategory", back_populates="histories")
    symptom_links: Mapped[list["SymptomCheckpointLink"]] = relationship(
        "SymptomCheckpointLink", back_populates="fault_history",
    )

    def __repr__(self) -> str:
        return f"<FaultHistory(id={self.id}, vehicle_id={self.vehicle_id}, resolved={self.resolved})>"


class FaultCheckpoint(Base):
    """A single diagnostic checkpoint step belonging to a fault category."""

    __tablename__ = "fault_checkpoints"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    category_id: Mapped[int] = mapped_column(
        Integer, ForeignKey("fault_categories.id"), nullable=False,
    )
    name: Mapped[str] = mapped_column(
        String(100), nullable=False, comment="e.g. Cek Busi, Cek Koil, Cek Fuel Pump",
    )
    description: Mapped[str] = mapped_column(Text, nullable=False)
    order_priority: Mapped[int] = mapped_column(
        Integer, nullable=False, comment="Default check order",
    )

    # Relationships
    category: Mapped["FaultCategory"] = relationship("FaultCategory", back_populates="checkpoints")
    symptom_links: Mapped[list["SymptomCheckpointLink"]] = relationship(
        "SymptomCheckpointLink", back_populates="checkpoint",
    )

    def __repr__(self) -> str:
        return f"<FaultCheckpoint(id={self.id}, name='{self.name}', priority={self.order_priority})>"


class SymptomCheckpointLink(Base):
    """Links a fault history entry to the checkpoint that was tested."""

    __tablename__ = "symptom_checkpoint_links"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    fault_history_id: Mapped[int] = mapped_column(
        Integer, ForeignKey("fault_histories.id"), nullable=False,
    )
    checkpoint_id: Mapped[int] = mapped_column(
        Integer, ForeignKey("fault_checkpoints.id"), nullable=False,
    )
    was_cause: Mapped[bool] = mapped_column(
        Boolean, nullable=False, comment="True if this checkpoint found the actual cause",
    )
    notes: Mapped[str | None] = mapped_column(Text, nullable=True)

    # Relationships
    fault_history: Mapped["FaultHistory"] = relationship(
        "FaultHistory", back_populates="symptom_links",
    )
    checkpoint: Mapped["FaultCheckpoint"] = relationship(
        "FaultCheckpoint", back_populates="symptom_links",
    )

    def __repr__(self) -> str:
        return (
            f"<SymptomCheckpointLink(id={self.id}, "
            f"history={self.fault_history_id}, checkpoint={self.checkpoint_id}, "
            f"was_cause={self.was_cause})>"
        )
