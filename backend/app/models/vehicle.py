"""
Customer and Vehicle ORM models.
"""

from datetime import datetime, timezone

from sqlalchemy import DateTime, ForeignKey, Integer, String, Text
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.database import Base


class Customer(Base):
    """Workshop customer record."""

    __tablename__ = "customers"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    name: Mapped[str] = mapped_column(String(100), nullable=False)
    phone: Mapped[str] = mapped_column(String(20), index=True, nullable=False)
    email: Mapped[str | None] = mapped_column(String(100), nullable=True)
    address: Mapped[str | None] = mapped_column(Text, nullable=True)
    created_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True), default=lambda: datetime.now(timezone.utc), nullable=False,
    )

    # Relationships
    vehicles: Mapped[list["Vehicle"]] = relationship("Vehicle", back_populates="customer")

    def __repr__(self) -> str:
        return f"<Customer(id={self.id}, name='{self.name}', phone='{self.phone}')>"


class Vehicle(Base):
    """Vehicle registered for service at the workshop."""

    __tablename__ = "vehicles"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    customer_id: Mapped[int] = mapped_column(
        Integer, ForeignKey("customers.id"), nullable=False,
    )
    plate_number: Mapped[str] = mapped_column(
        String(15), unique=True, index=True, nullable=False, comment="Nomor polisi",
    )
    brand: Mapped[str] = mapped_column(
        String(50), index=True, nullable=False, comment="Toyota, Honda, Suzuki, etc.",
    )
    model: Mapped[str] = mapped_column(
        String(50), nullable=False, comment="Avanza, Jazz, Ertiga, etc.",
    )
    year: Mapped[int] = mapped_column(Integer, nullable=False)
    engine_code: Mapped[str | None] = mapped_column(String(20), nullable=True)
    vin: Mapped[str | None] = mapped_column(String(17), unique=True, nullable=True)
    transmission: Mapped[str] = mapped_column(
        String(15), nullable=False, comment="manual, automatic, cvt",
    )
    fuel_type: Mapped[str] = mapped_column(
        String(15), nullable=False, comment="bensin, diesel, hybrid, electric",
    )
    notes: Mapped[str | None] = mapped_column(Text, nullable=True)
    created_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True), default=lambda: datetime.now(timezone.utc), nullable=False,
    )

    # Relationships
    customer: Mapped["Customer"] = relationship("Customer", back_populates="vehicles")

    def __repr__(self) -> str:
        return f"<Vehicle(id={self.id}, plate='{self.plate_number}', brand='{self.brand}', model='{self.model}')>"
