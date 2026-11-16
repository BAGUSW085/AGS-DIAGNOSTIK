"""
Workshop ORM models: WorkOrder (PKB) and WorkOrderItem.
"""

from datetime import datetime, timezone

from sqlalchemy import DateTime, Float, ForeignKey, Integer, String, Text
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.database import Base


class WorkOrder(Base):
    """Perintah Kerja Bengkel (PKB) — the core work order entity."""

    __tablename__ = "work_orders"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    order_number: Mapped[str] = mapped_column(
        String(20), unique=True, index=True, nullable=False,
        comment="Auto-generated: WO-YYYYMMDD-XXX",
    )
    vehicle_id: Mapped[int] = mapped_column(
        Integer, ForeignKey("vehicles.id"), nullable=False,
    )
    customer_id: Mapped[int] = mapped_column(
        Integer, ForeignKey("customers.id"), nullable=False,
    )
    service_advisor_id: Mapped[int | None] = mapped_column(
        Integer, ForeignKey("users.id"), nullable=True,
    )
    mechanic_id: Mapped[int | None] = mapped_column(
        Integer, ForeignKey("users.id"), nullable=True,
    )
    complaint: Mapped[str] = mapped_column(
        Text, nullable=False, comment="Keluhan customer",
    )
    diagnosis: Mapped[str | None] = mapped_column(Text, nullable=True)
    status: Mapped[str] = mapped_column(
        String(20), nullable=False, default="pending",
        comment="pending, in_progress, waiting_parts, completed, invoiced, cancelled",
    )
    estimated_completion: Mapped[datetime | None] = mapped_column(
        DateTime(timezone=True), nullable=True,
    )
    actual_completion: Mapped[datetime | None] = mapped_column(
        DateTime(timezone=True), nullable=True,
    )
    mileage_km: Mapped[int | None] = mapped_column(Integer, nullable=True)
    notes: Mapped[str | None] = mapped_column(Text, nullable=True)
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
    items: Mapped[list["WorkOrderItem"]] = relationship(
        "WorkOrderItem", back_populates="work_order", cascade="all, delete-orphan",
    )

    def __repr__(self) -> str:
        return f"<WorkOrder(id={self.id}, number='{self.order_number}', status='{self.status}')>"


class WorkOrderItem(Base):
    """Line item (service or sparepart) on a work order."""

    __tablename__ = "work_order_items"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    work_order_id: Mapped[int] = mapped_column(
        Integer, ForeignKey("work_orders.id"), nullable=False,
    )
    item_type: Mapped[str] = mapped_column(
        String(15), nullable=False, comment="service or sparepart",
    )
    description: Mapped[str] = mapped_column(String(255), nullable=False)
    sparepart_id: Mapped[int | None] = mapped_column(
        Integer, ForeignKey("spareparts.id"), nullable=True,
    )
    quantity: Mapped[float] = mapped_column(Float, default=1, nullable=False)
    unit_price: Mapped[float] = mapped_column(Float, nullable=False)
    discount_percent: Mapped[float] = mapped_column(Float, default=0, nullable=False)
    subtotal: Mapped[float] = mapped_column(Float, nullable=False)
    notes: Mapped[str | None] = mapped_column(String(255), nullable=True)

    # Relationships
    work_order: Mapped["WorkOrder"] = relationship("WorkOrder", back_populates="items")

    def __repr__(self) -> str:
        return f"<WorkOrderItem(id={self.id}, type='{self.item_type}', desc='{self.description}')>"
