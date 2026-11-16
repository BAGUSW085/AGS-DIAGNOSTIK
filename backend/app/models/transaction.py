"""
Transaction / POS ORM models: Transaction and TransactionItem.
"""

from datetime import datetime, timezone

from sqlalchemy import DateTime, Float, ForeignKey, Integer, String, Text
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.database import Base


class Transaction(Base):
    """Point-of-sale invoice / transaction record."""

    __tablename__ = "transactions"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    invoice_number: Mapped[str] = mapped_column(
        String(25), unique=True, index=True, nullable=False,
        comment="Auto: INV-YYYYMMDD-XXX",
    )
    work_order_id: Mapped[int | None] = mapped_column(
        Integer, ForeignKey("work_orders.id"), nullable=True,
    )
    customer_id: Mapped[int] = mapped_column(
        Integer, ForeignKey("customers.id"), nullable=False,
    )
    subtotal: Mapped[float] = mapped_column(Float, nullable=False)
    tax_percent: Mapped[float] = mapped_column(
        Float, default=11, nullable=False, comment="PPN 11%",
    )
    tax_amount: Mapped[float] = mapped_column(Float, nullable=False)
    discount_amount: Mapped[float] = mapped_column(Float, default=0, nullable=False)
    grand_total: Mapped[float] = mapped_column(Float, nullable=False)
    payment_method: Mapped[str] = mapped_column(
        String(15), nullable=False, comment="cash, transfer, debit, credit, qris",
    )
    payment_status: Mapped[str] = mapped_column(
        String(10), nullable=False, default="unpaid",
        comment="unpaid, partial, paid",
    )
    paid_amount: Mapped[float] = mapped_column(Float, default=0, nullable=False)
    change_amount: Mapped[float] = mapped_column(Float, default=0, nullable=False)
    cashier_id: Mapped[int] = mapped_column(
        Integer, ForeignKey("users.id"), nullable=False,
    )
    notes: Mapped[str | None] = mapped_column(Text, nullable=True)
    created_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True), default=lambda: datetime.now(timezone.utc), nullable=False,
    )

    # Relationships
    items: Mapped[list["TransactionItem"]] = relationship(
        "TransactionItem", back_populates="transaction", cascade="all, delete-orphan",
    )

    def __repr__(self) -> str:
        return f"<Transaction(id={self.id}, invoice='{self.invoice_number}', total={self.grand_total})>"


class TransactionItem(Base):
    """Line item on a POS transaction."""

    __tablename__ = "transaction_items"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    transaction_id: Mapped[int] = mapped_column(
        Integer, ForeignKey("transactions.id"), nullable=False,
    )
    item_type: Mapped[str] = mapped_column(
        String(15), nullable=False, comment="service or sparepart",
    )
    description: Mapped[str] = mapped_column(String(255), nullable=False)
    sparepart_id: Mapped[int | None] = mapped_column(
        Integer, ForeignKey("spareparts.id"), nullable=True,
    )
    quantity: Mapped[float] = mapped_column(Float, nullable=False)
    unit_price: Mapped[float] = mapped_column(Float, nullable=False)
    discount_percent: Mapped[float] = mapped_column(Float, default=0, nullable=False)
    subtotal: Mapped[float] = mapped_column(Float, nullable=False)

    # Relationships
    transaction: Mapped["Transaction"] = relationship("Transaction", back_populates="items")

    def __repr__(self) -> str:
        return f"<TransactionItem(id={self.id}, type='{self.item_type}', desc='{self.description}')>"
