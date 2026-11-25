"""
SQLAlchemy 2.0 ORM Models (16 Tabel Utama) - Project Bengkel Masa Depan
=======================================================================
Mencakup seluruh 16 tabel inti sesuai arsitektur:
1. User & Auth (1 tabel):
   - `User` (role: admin, mekanik, kasir, service_advisor)
2. Kendaraan & Pelanggan (2 tabel):
   - `Customer`, `Vehicle`
3. Pilar 1 - Smart Fault Diagnostic (4 tabel):
   - `FaultCategory`, `FaultCheckpoint`, `SymptomCheckpointLink`, `FaultHistory`
4. Pilar 2 - AI Repair Manual & Wiring Assistant / RAG (4 tabel):
   - `RepairManual`, `WiringDiagram`, `DTCCode`, `SensorSpec`
5. Pilar 3 - Bengkel PKB, Gudang Sparepart, & POS Kasir (5 tabel):
   - `WorkOrder`, `WorkOrderItem`, `Sparepart`, `StockMovement`, `Transaction`, `TransactionItem`
   (Total = 16 Tabel ORM)
"""

from datetime import datetime, timezone
from decimal import Decimal
from typing import Any

from sqlalchemy import (
    Boolean,
    DateTime,
    Float,
    ForeignKey,
    Integer,
    JSON,
    Numeric,
    String,
    Text,
)
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, relationship


def utc_now() -> datetime:
    return datetime.now(timezone.utc)


class Base(DeclarativeBase):
    pass


# ===========================================================================
# 1. USER & AUTH (Tabel #1)
# ===========================================================================


class User(Base):
    __tablename__ = "users"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True)
    username: Mapped[str] = mapped_column(String(64), unique=True, index=True, nullable=False)
    full_name: Mapped[str] = mapped_column(String(120), nullable=False)
    email: Mapped[str] = mapped_column(String(120), unique=True, index=True, nullable=False)
    role: Mapped[str] = mapped_column(
        String(32),
        nullable=False,
        default="mekanik",
         doc="Role: admin | mekanik | kasir | service_advisor",
    )
    password_hash: Mapped[str] = mapped_column(String(255), nullable=False)
    is_active: Mapped[bool] = mapped_column(Boolean, default=True, nullable=False)
    created_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), default=utc_now)


# ===========================================================================
# 2. PELANGGAN & KENDARAAN (Tabel #2 & #3)
# ===========================================================================


class Customer(Base):
    __tablename__ = "customers"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True)
    name: Mapped[str] = mapped_column(String(120), nullable=False, index=True)
    phone: Mapped[str] = mapped_column(String(32), nullable=False, index=True)
    address: Mapped[str | None] = mapped_column(Text, nullable=True)
    created_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), default=utc_now)

    vehicles: Mapped[list["Vehicle"]] = relationship(
        "Vehicle", back_populates="customer", cascade="all, delete-orphan"
    )


class Vehicle(Base):
    __tablename__ = "vehicles"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True)
    customer_id: Mapped[int] = mapped_column(
        ForeignKey("customers.id", ondelete="CASCADE"), nullable=False, index=True
    )
    license_plate: Mapped[str] = mapped_column(String(20), unique=True, index=True, nullable=False)
    brand: Mapped[str] = mapped_column(String(64), index=True, nullable=False)
    model: Mapped[str] = mapped_column(String(100), index=True, nullable=False)
    year: Mapped[int | None] = mapped_column(Integer, nullable=True)
    transmission: Mapped[str] = mapped_column(String(20), default="AT")
    engine_code: Mapped[str | None] = mapped_column(String(50), nullable=True)
    vin: Mapped[str | None] = mapped_column(String(64), unique=True, nullable=True)
    current_km: Mapped[int] = mapped_column(Integer, default=0)
    created_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), default=utc_now)

    customer: Mapped["Customer"] = relationship("Customer", back_populates="vehicles")


# ===========================================================================
# 3. PILAR 1: SMART FAULT DIAGNOSTIC (Tabel #4, #5, #6, #7)
# ===========================================================================


class FaultCategory(Base):
    __tablename__ = "fault_categories"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True)
    name: Mapped[str] = mapped_column(String(100), unique=True, nullable=False)
    description: Mapped[str | None] = mapped_column(Text, nullable=True)

    checkpoints: Mapped[list["FaultCheckpoint"]] = relationship(
        "FaultCheckpoint", back_populates="category", cascade="all, delete-orphan"
    )


class FaultCheckpoint(Base):
    __tablename__ = "fault_checkpoints"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True)
    category_id: Mapped[int] = mapped_column(
        ForeignKey("fault_categories.id", ondelete="CASCADE"), nullable=False, index=True
    )
    code: Mapped[str] = mapped_column(String(32), unique=True, index=True, nullable=False)
    name: Mapped[str] = mapped_column(String(150), nullable=False)
    inspection_steps: Mapped[str] = mapped_column(Text, nullable=False)
    estimated_check_minutes: Mapped[int] = mapped_column(Integer, default=15)

    category: Mapped["FaultCategory"] = relationship("FaultCategory", back_populates="checkpoints")


class SymptomCheckpointLink(Base):
    __tablename__ = "symptom_checkpoint_links"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True)
    checkpoint_id: Mapped[int] = mapped_column(
        ForeignKey("fault_checkpoints.id", ondelete="CASCADE"), nullable=False, index=True
    )
    symptom_keyword: Mapped[str] = mapped_column(Text, nullable=False)
    dtc_code: Mapped[str | None] = mapped_column(String(32), index=True, nullable=True)
    base_weight: Mapped[float] = mapped_column(Float, default=0.75, nullable=False)


class FaultHistory(Base):
    __tablename__ = "fault_histories"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True)
    vehicle_id: Mapped[int | None] = mapped_column(
        ForeignKey("vehicles.id", ondelete="SET NULL"), nullable=True, index=True
    )
    brand: Mapped[str] = mapped_column(String(64), index=True, nullable=False)
    model: Mapped[str] = mapped_column(String(100), index=True, nullable=False)
    symptom_text: Mapped[str] = mapped_column(Text, nullable=False)
    dtc_codes: Mapped[str | None] = mapped_column(String(120), nullable=True)
    resolved_checkpoint_id: Mapped[int] = mapped_column(
        ForeignKey("fault_checkpoints.id", ondelete="CASCADE"), nullable=False, index=True
    )
    resolution_notes: Mapped[str] = mapped_column(Text, nullable=False)
    is_verified: Mapped[bool] = mapped_column(Boolean, default=True, nullable=False)
    created_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), default=utc_now)


class HistoricalCase(Base):
    """
    Tabel Data Kasus Historis (Dataset Excel Pencarian Kasus Diagnosis Berbobot).
    Menampung seluruh parameter live data scanner, gejala, keluhan, DTC, dan solusi perbaikan.
    """
    __tablename__ = "historical_cases"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True)
    case_code: Mapped[str] = mapped_column(String(32), unique=True, index=True, nullable=False)  # K001, K002...
    brand: Mapped[str] = mapped_column(String(64), index=True, nullable=False)
    model: Mapped[str] = mapped_column(String(100), index=True, nullable=False)
    year: Mapped[int | None] = mapped_column(Integer, nullable=True)
    engine_capacity: Mapped[str | None] = mapped_column(String(32), nullable=True)  # 1.2, 1.3, 1.5, 2.0
    engine_code: Mapped[str | None] = mapped_column(String(64), index=True, nullable=True)  # 1NR-VE, K14B, J20A, 2KD-FTV
    odometer_km: Mapped[int | None] = mapped_column(Integer, nullable=True)  # Jarak tempuh (km murni)
    license_plate: Mapped[str | None] = mapped_column(String(32), index=True, nullable=True)  # Nomor Polisi (opsional)
    mechanic_name: Mapped[str | None] = mapped_column(String(100), nullable=True)  # Nama Mekanik (opsional)
    verification_status: Mapped[str] = mapped_column(
        String(32), default="TERVERIFIKASI", nullable=False, doc="TERVERIFIKASI | DRAFT"
    )
    complaint: Mapped[str] = mapped_column(Text, nullable=False)  # Keluhan
    symptom: Mapped[str] = mapped_column(Text, nullable=False)  # Gejala
    dtc: Mapped[str | None] = mapped_column(String(64), index=True, nullable=True)  # P0171, P0131, dll.
    stft: Mapped[float | None] = mapped_column(Float, nullable=True)  # Short Term Fuel Trim (%)
    ltft: Mapped[float | None] = mapped_column(Float, nullable=True)  # Long Term Fuel Trim (%)
    rpm: Mapped[float | None] = mapped_column(Float, nullable=True)  # RPM Idle
    o2_voltage: Mapped[str | None] = mapped_column(String(64), nullable=True)  # Rentang tegangan O2 (V)
    map_kpa: Mapped[float | None] = mapped_column(Float, nullable=True)  # MAP (kPa)
    maf_gps: Mapped[float | None] = mapped_column(Float, nullable=True)  # MAF (g/s)
    ect_c: Mapped[float | None] = mapped_column(Float, nullable=True)  # ECT (°C)
    inspection_findings: Mapped[str] = mapped_column(Text, nullable=False)  # Pemeriksaan fisik/sensor
    final_diagnosis: Mapped[str] = mapped_column(String(255), index=True, nullable=False)  # Diagnosis Akhir
    repair_action: Mapped[str] = mapped_column(Text, nullable=False)  # Tindakan Perbaikan
    system_category: Mapped[str] = mapped_column(String(64), index=True, nullable=False)  # Sistem: Udara, Bahan Bakar...
    affected_system: Mapped[str | None] = mapped_column(String(64), nullable=True)  # Sistem Terdampak
    group_category: Mapped[str] = mapped_column(String(64), default="Pembakaran")  # Pembakaran / Pendukung
    manual_book_ref: Mapped[str | None] = mapped_column(Text, nullable=True)  # Referensi bab manual book & pinout
    created_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), default=utc_now)


# ===========================================================================
# 4. PILAR 2: AI REPAIR MANUAL & WIRING ASSISTANT / RAG (Tabel #8, #9, #10, #11)
# ===========================================================================


class RepairManual(Base):
    __tablename__ = "repair_manuals"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True)
    brand: Mapped[str] = mapped_column(String(64), index=True, nullable=False)
    model: Mapped[str] = mapped_column(String(100), index=True, nullable=False)
    section_title: Mapped[str] = mapped_column(String(200), nullable=False)
    content_text: Mapped[str] = mapped_column(Text, nullable=False)
    tags: Mapped[str | None] = mapped_column(String(255), index=True, nullable=True)
    source_file_path: Mapped[str | None] = mapped_column(String(255), nullable=True)
    created_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), default=utc_now)


class WiringDiagram(Base):
    __tablename__ = "wiring_diagrams"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True)
    brand: Mapped[str] = mapped_column(String(64), index=True, nullable=False)
    model: Mapped[str] = mapped_column(String(100), index=True, nullable=False)
    year_range: Mapped[str] = mapped_column(String(32), default="All Years")
    system_name: Mapped[str] = mapped_column(String(150), nullable=False)
    ecu_connector_code: Mapped[str] = mapped_column(String(100), nullable=False)
    pinout_json: Mapped[dict[str, Any]] = mapped_column(JSON, default=dict)
    ground_locations: Mapped[str] = mapped_column(Text, nullable=False)
    diagram_image_url: Mapped[str | None] = mapped_column(String(255), nullable=True)


class DTCCode(Base):
    __tablename__ = "dtc_codes"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True)
    code: Mapped[str] = mapped_column(String(16), unique=True, index=True, nullable=False)
    system: Mapped[str] = mapped_column(String(100), default="", nullable=False)
    description_id: Mapped[str] = mapped_column(Text, nullable=False)
    possible_causes: Mapped[str] = mapped_column(Text, default="", nullable=False)
    severity_level: Mapped[str] = mapped_column(String(20), default="MEDIUM")

    # Kolom kompatibilitas untuk katalog JB420 & SOP Perbaikan
    system_category: Mapped[str | None] = mapped_column(String(150), nullable=True)
    common_causes: Mapped[str | None] = mapped_column(Text, nullable=True)
    recommended_fix: Mapped[str | None] = mapped_column(Text, nullable=True)

    def __init__(self, **kwargs):
        if "system_category" in kwargs and "system" not in kwargs:
            kwargs["system"] = kwargs["system_category"]
        if "common_causes" in kwargs and "possible_causes" not in kwargs:
            kwargs["possible_causes"] = kwargs["common_causes"]
        if "possible_causes" in kwargs and "common_causes" not in kwargs:
            kwargs["common_causes"] = kwargs["possible_causes"]
        if "system" in kwargs and "system_category" not in kwargs:
            kwargs["system_category"] = kwargs["system"]
        super().__init__(**kwargs)


class SensorSpec(Base):
    __tablename__ = "sensor_specs"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True)
    brand: Mapped[str] = mapped_column(String(64), index=True, nullable=False)
    model: Mapped[str] = mapped_column(String(100), index=True, nullable=False)
    sensor_name: Mapped[str] = mapped_column(String(120), index=True, nullable=False)
    pin_configuration: Mapped[str] = mapped_column(Text, nullable=False)
    voltage_idle: Mapped[str] = mapped_column(String(120), nullable=False)
    voltage_wot: Mapped[str] = mapped_column(String(120), nullable=False)
    resistance_ohm: Mapped[str] = mapped_column(String(150), nullable=False)
    testing_notes: Mapped[str] = mapped_column(Text, nullable=False)


# ===========================================================================
# 5. PILAR 3: WORK ORDER (PKB), GUDANG, & KASIR (Tabel #12, #13, #14, #15, #16, #17)
# ===========================================================================


class Sparepart(Base):
    __tablename__ = "spareparts"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True)
    sku: Mapped[str] = mapped_column(String(64), unique=True, index=True, nullable=False)
    name: Mapped[str] = mapped_column(String(150), index=True, nullable=False)
    category: Mapped[str] = mapped_column(String(64), index=True, nullable=False)
    buy_price: Mapped[Decimal] = mapped_column(Numeric(14, 2), nullable=False)
    sell_price: Mapped[Decimal] = mapped_column(Numeric(14, 2), nullable=False)
    stock_qty: Mapped[int] = mapped_column(Integer, default=0, nullable=False)
    min_stock_alert: Mapped[int] = mapped_column(Integer, default=3, nullable=False)
    unit: Mapped[str] = mapped_column(String(20), default="pcs")


class StockMovement(Base):
    __tablename__ = "stock_movements"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True)
    sparepart_id: Mapped[int] = mapped_column(
        ForeignKey("spareparts.id", ondelete="CASCADE"), nullable=False, index=True
    )
    movement_type: Mapped[str] = mapped_column(
        String(32), nullable=False, doc="INITIAL_IN | RESTOCK_IN | PKB_OUT | ADJUSTMENT"
    )
    qty_change: Mapped[int] = mapped_column(Integer, nullable=False)
    balance_after: Mapped[int] = mapped_column(Integer, nullable=False)
    reference_note: Mapped[str | None] = mapped_column(String(200), nullable=True)
    created_by_id: Mapped[int | None] = mapped_column(
        ForeignKey("users.id", ondelete="SET NULL"), nullable=True
    )
    created_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), default=utc_now)


class WorkOrder(Base):
    __tablename__ = "work_orders"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True)
    wo_number: Mapped[str] = mapped_column(String(32), unique=True, index=True, nullable=False)
    vehicle_id: Mapped[int] = mapped_column(
        ForeignKey("vehicles.id", ondelete="RESTRICT"), nullable=False, index=True
    )
    service_advisor_id: Mapped[int | None] = mapped_column(
        ForeignKey("users.id", ondelete="SET NULL"), nullable=True
    )
    mechanic_id: Mapped[int | None] = mapped_column(
        ForeignKey("users.id", ondelete="SET NULL"), nullable=True
    )
    customer_complaint: Mapped[str] = mapped_column(Text, nullable=False)
    initial_dtc_codes: Mapped[str | None] = mapped_column(String(120), nullable=True)
    status: Mapped[str] = mapped_column(
        String(24), default="PENDING", doc="PENDING | IN_PROGRESS | COMPLETED | CANCELLED"
    )
    estimated_total: Mapped[Decimal] = mapped_column(
        Numeric(14, 2), default=Decimal("0.00"), nullable=False
    )
    created_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), default=utc_now)


class WorkOrderItem(Base):
    __tablename__ = "work_order_items"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True)
    work_order_id: Mapped[int] = mapped_column(
        ForeignKey("work_orders.id", ondelete="CASCADE"), nullable=False, index=True
    )
    item_type: Mapped[str] = mapped_column(
        String(24), nullable=False, doc="SPAREPART | SERVICE_LABOR"
    )
    sparepart_id: Mapped[int | None] = mapped_column(
        ForeignKey("spareparts.id", ondelete="SET NULL"), nullable=True
    )
    description: Mapped[str] = mapped_column(String(200), nullable=False)
    qty: Mapped[int] = mapped_column(Integer, default=1, nullable=False)
    unit_price: Mapped[Decimal] = mapped_column(Numeric(14, 2), nullable=False)
    subtotal: Mapped[Decimal] = mapped_column(Numeric(14, 2), nullable=False)


class Transaction(Base):
    __tablename__ = "transactions"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True)
    invoice_number: Mapped[str] = mapped_column(String(32), unique=True, index=True, nullable=False)
    work_order_id: Mapped[int] = mapped_column(
        ForeignKey("work_orders.id", ondelete="RESTRICT"), unique=True, nullable=False
    )
    cashier_id: Mapped[int | None] = mapped_column(
        ForeignKey("users.id", ondelete="SET NULL"), nullable=True
    )
    subtotal: Mapped[Decimal] = mapped_column(Numeric(14, 2), nullable=False)
    tax_ppn_rate: Mapped[Decimal] = mapped_column(Numeric(5, 2), default=Decimal("11.00"))
    tax_ppn_amount: Mapped[Decimal] = mapped_column(Numeric(14, 2), nullable=False)
    discount_amount: Mapped[Decimal] = mapped_column(Numeric(14, 2), default=Decimal("0.00"))
    grand_total: Mapped[Decimal] = mapped_column(Numeric(14, 2), nullable=False)
    payment_method: Mapped[str] = mapped_column(
        String(24), default="QRIS", doc="CASH | TRANSFER | QRIS"
    )
    payment_status: Mapped[str] = mapped_column(String(24), default="PAID")
    paid_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), default=utc_now)


class TransactionItem(Base):
    __tablename__ = "transaction_items"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True)
    transaction_id: Mapped[int] = mapped_column(
        ForeignKey("transactions.id", ondelete="CASCADE"), nullable=False, index=True
    )
    description: Mapped[str] = mapped_column(String(200), nullable=False)
    item_type: Mapped[str] = mapped_column(String(24), nullable=False)
    qty: Mapped[int] = mapped_column(Integer, default=1, nullable=False)
    unit_price: Mapped[Decimal] = mapped_column(Numeric(14, 2), nullable=False)
    subtotal: Mapped[Decimal] = mapped_column(Numeric(14, 2), nullable=False)
