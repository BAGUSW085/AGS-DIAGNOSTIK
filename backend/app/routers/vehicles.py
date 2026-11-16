"""
Vehicles and Customers CRUD router.
"""

from fastapi import APIRouter, Depends, HTTPException, Query, status
from sqlalchemy import select, or_
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import selectinload

from app.database import get_db
from app.models.vehicle import Customer, Vehicle
from app.models.user import User
from app.schemas.vehicle import (
    CustomerCreate, CustomerResponse, CustomerUpdate,
    VehicleCreate, VehicleResponse, VehicleUpdate,
)
from app.utils.deps import get_current_user

router = APIRouter(prefix="/vehicles", tags=["Vehicles"])


# ── Customers ─────────────────────────────────────────────────────────────────

@router.get("/customers", response_model=list[CustomerResponse])
async def list_customers(
    search: str | None = Query(None, description="Cari nama atau telepon"),
    db: AsyncSession = Depends(get_db),
    _user: User = Depends(get_current_user),
):
    """List all customers with optional search."""
    stmt = select(Customer).order_by(Customer.name)
    if search:
        stmt = stmt.where(
            or_(
                Customer.name.ilike(f"%{search}%"),
                Customer.phone.ilike(f"%{search}%"),
            )
        )
    result = await db.execute(stmt)
    return result.scalars().all()


@router.post("/customers", response_model=CustomerResponse, status_code=status.HTTP_201_CREATED)
async def create_customer(
    data: CustomerCreate,
    db: AsyncSession = Depends(get_db),
    _user: User = Depends(get_current_user),
):
    """Create a new customer."""
    customer = Customer(**data.model_dump())
    db.add(customer)
    await db.flush()
    await db.refresh(customer)
    return customer


@router.get("/customers/{customer_id}", response_model=CustomerResponse)
async def get_customer(
    customer_id: int,
    db: AsyncSession = Depends(get_db),
    _user: User = Depends(get_current_user),
):
    """Get a customer by ID."""
    result = await db.execute(select(Customer).where(Customer.id == customer_id))
    customer = result.scalar_one_or_none()
    if not customer:
        raise HTTPException(status_code=404, detail="Customer tidak ditemukan")
    return customer


@router.put("/customers/{customer_id}", response_model=CustomerResponse)
async def update_customer(
    customer_id: int,
    data: CustomerUpdate,
    db: AsyncSession = Depends(get_db),
    _user: User = Depends(get_current_user),
):
    """Update a customer."""
    result = await db.execute(select(Customer).where(Customer.id == customer_id))
    customer = result.scalar_one_or_none()
    if not customer:
        raise HTTPException(status_code=404, detail="Customer tidak ditemukan")

    for field, value in data.model_dump(exclude_unset=True).items():
        setattr(customer, field, value)
    await db.flush()
    await db.refresh(customer)
    return customer


# ── Vehicles ──────────────────────────────────────────────────────────────────

@router.get("/", response_model=list[VehicleResponse])
async def list_vehicles(
    search: str | None = Query(None, description="Cari nomor polisi, merk, atau model"),
    customer_id: int | None = Query(None),
    db: AsyncSession = Depends(get_db),
    _user: User = Depends(get_current_user),
):
    """List all vehicles with optional search and filter."""
    stmt = select(Vehicle).order_by(Vehicle.plate_number)
    if search:
        stmt = stmt.where(
            or_(
                Vehicle.plate_number.ilike(f"%{search}%"),
                Vehicle.brand.ilike(f"%{search}%"),
                Vehicle.model.ilike(f"%{search}%"),
            )
        )
    if customer_id:
        stmt = stmt.where(Vehicle.customer_id == customer_id)
    result = await db.execute(stmt)
    return result.scalars().all()


@router.post("/", response_model=VehicleResponse, status_code=status.HTTP_201_CREATED)
async def create_vehicle(
    data: VehicleCreate,
    db: AsyncSession = Depends(get_db),
    _user: User = Depends(get_current_user),
):
    """Register a new vehicle."""
    # Verify customer exists
    cust = await db.execute(select(Customer).where(Customer.id == data.customer_id))
    if not cust.scalar_one_or_none():
        raise HTTPException(status_code=404, detail="Customer tidak ditemukan")

    # Check duplicate plate number
    existing = await db.execute(
        select(Vehicle).where(Vehicle.plate_number == data.plate_number.upper())
    )
    if existing.scalar_one_or_none():
        raise HTTPException(status_code=409, detail="Nomor polisi sudah terdaftar")

    vehicle = Vehicle(**data.model_dump())
    vehicle.plate_number = vehicle.plate_number.upper()
    db.add(vehicle)
    await db.flush()
    await db.refresh(vehicle)
    return vehicle


@router.get("/{vehicle_id}", response_model=VehicleResponse)
async def get_vehicle(
    vehicle_id: int,
    db: AsyncSession = Depends(get_db),
    _user: User = Depends(get_current_user),
):
    """Get vehicle details by ID."""
    result = await db.execute(select(Vehicle).where(Vehicle.id == vehicle_id))
    vehicle = result.scalar_one_or_none()
    if not vehicle:
        raise HTTPException(status_code=404, detail="Kendaraan tidak ditemukan")
    return vehicle


@router.get("/plate/{plate_number}", response_model=VehicleResponse)
async def get_vehicle_by_plate(
    plate_number: str,
    db: AsyncSession = Depends(get_db),
    _user: User = Depends(get_current_user),
):
    """Get vehicle details by plate number (nomor polisi)."""
    result = await db.execute(
        select(Vehicle).where(Vehicle.plate_number == plate_number.upper())
    )
    vehicle = result.scalar_one_or_none()
    if not vehicle:
        raise HTTPException(status_code=404, detail="Kendaraan tidak ditemukan")
    return vehicle


@router.put("/{vehicle_id}", response_model=VehicleResponse)
async def update_vehicle(
    vehicle_id: int,
    data: VehicleUpdate,
    db: AsyncSession = Depends(get_db),
    _user: User = Depends(get_current_user),
):
    """Update vehicle information."""
    result = await db.execute(select(Vehicle).where(Vehicle.id == vehicle_id))
    vehicle = result.scalar_one_or_none()
    if not vehicle:
        raise HTTPException(status_code=404, detail="Kendaraan tidak ditemukan")

    for field, value in data.model_dump(exclude_unset=True).items():
        if field == "plate_number" and value:
            value = value.upper()
        setattr(vehicle, field, value)
    await db.flush()
    await db.refresh(vehicle)
    return vehicle
