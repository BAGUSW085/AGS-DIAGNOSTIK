"""
Inventory ORM models: Sparepart and StockMovement.
"""

from datetime import datetime, timezone

from sqlalchemy import Boolean, DateTime, Float, ForeignKey, Integer, String, Text
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.database import Base


class Sparepart(Base):
    """Spare part / consumable tracked in workshop inventory."""

    __tablename__ = "spareparts"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    part_number: Mapped[str] = mapped_column(
        String(50), unique=True, index=True, nullable=False,
    )
    name: Mapped[str] = mapped_column(String(150), index=True, nullable=False)
    brand: Mapped[str | None] = mapped_column(String(50), nullable=True)
    category: Mapped[str] = mapped_column(
        String(30), nullable=False,
        comment="filter, brake, electrical, engine, body, etc.",
    )
    compatible_vehicles: Mapped[str | None] = mapped_column(
        Text, nullable=True,
        comment="JSON array of {brand, model, year_from, year_to}",
    )
    buy_price: Mapped[float] = mapped_column(Float, nullable=False)
    sell_price: Mapped[float] = mapped_column(Float, nullable=False)
    stock_quantity: Mapped[int] = mapped_column(Integer, default=0, nullable=False)
    min_stock: Mapped[int] = mapped_column(
        Integer, default=2, nullable=False, comment="Alert threshold",
    )
    location: Mapped[str | None] = mapped_column(
        String(50), nullable=True, comment="Shelf/rack location in workshop",
    )
    supplier: Mapped[str | None] = mapped_column(String(100), nullable=True)
    unit: Mapped[str] = mapped_column(
        String(10), default="pcs", nullable=False, comment="pcs, liter, set, meter",
    )
    is_active: Mapped[bool] = mapped_column(Boolean, default=True, nullable=False)
    created_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True), default=lambda: datetime.now(timezone.utc), nullable=False,
    )
    updated_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        default=lambda: datetime.now(timezone.utc),
        onupdate=lambda: datetime.now(timezone.utc),
        nullable=False,
    )

    # Relationships
    movements: Mapped[list["StockMovement"]] = relationship(
        "StockMovement", back_populates="sparepart",
    )

    def __repr__(self) -> str:
        return f"<Sparepart(id={self.id}, part='{self.part_number}', stock={self.stock_quantity})>"


class StockMovement(Base):
    """Tracks every inbound, outbound, adjustment, or return of inventory."""

    __tablename__ = "stock_movements"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    sparepart_id: Mapped[int] = mapped_column(
        Integer, ForeignKey("spareparts.id"), nullable=False,
    )
    movement_type: Mapped[str] = mapped_column(
        String(15), nullable=False, comment="in, out, adjustment, return",
    )
    quantity: Mapped[int] = mapped_column(Integer, nullable=False)
    reference_type: Mapped[str | None] = mapped_column(
        String(20), nullable=True, comment="purchase, work_order, manual",
    )
    reference_id: Mapped[int | None] = mapped_column(
        Integer, nullable=True, comment="ID of related work_order or purchase",
    )
    notes: Mapped[str | None] = mapped_column(String(255), nullable=True)
    user_id: Mapped[int] = mapped_column(
        Integer, ForeignKey("users.id"), nullable=False,
    )
    created_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True), default=lambda: datetime.now(timezone.utc), nullable=False,
    )

    # Relationships
    sparepart: Mapped["Sparepart"] = relationship("Sparepart", back_populates="movements")

    def __repr__(self) -> str:
        return (
            f"<StockMovement(id={self.id}, type='{self.movement_type}', "
            f"qty={self.quantity}, part_id={self.sparepart_id})>"
        )
