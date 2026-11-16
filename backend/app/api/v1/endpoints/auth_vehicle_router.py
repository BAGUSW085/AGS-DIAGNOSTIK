"""
Endpoint Login JWT, Manajemen Kendaraan, & Trigger Ingest Manual PDF
====================================================================
Lokasi: app/api/v1/endpoints/auth_vehicle_router.py
"""

from __future__ import annotations

from pathlib import Path
from typing import Optional

from fastapi import APIRouter, Depends, HTTPException, Query, status
from pydantic import BaseModel, Field
from sqlalchemy import or_, select
from sqlalchemy.ext.asyncio import AsyncSession

from app.api.deps import get_current_active_user, get_db
from app.core.config import settings
from app.core.security import create_access_token, verify_password
from app.models import Customer, User, Vehicle


class LoginRequest(BaseModel):
    username: str = Field(..., examples=["mekanik_agus"])
    password: str = Field(..., examples=["Bengkel2026!"])


class TokenResponse(BaseModel):
    access_token: str
    token_type: str = "bearer"
    user_id: int
    username: str
    full_name: str
    role: str


class VehicleRegisterRequest(BaseModel):
    customer_name: str = Field(default="Pelanggan Bengkel", examples=["Bapak Hendra Wijaya"])
    customer_phone: str = Field(default="081200000000", examples=["081234567890"])
    customer_address: Optional[str] = Field(default="Surabaya, Jawa Timur")
    license_plate: str = Field(..., examples=["L 1420 GV"])
    brand: str = Field(..., examples=["Suzuki"])
    model: str = Field(..., examples=["Grand Vitara JB420 (2.0L J20A)"])
    year: int = Field(default=2018, ge=1980, le=2030)
    transmission: str = Field(default="AT", pattern="^(AT|MT|CVT)$")
    vin: Optional[str] = Field(default=None)
    engine_code: Optional[str] = Field(default=None)


router = APIRouter(prefix="/api/v1", tags=["Auth, Vehicles & Admin Ingest"])


@router.post(
    "/auth/login",
    response_model=TokenResponse,
    summary="Login Staf Bengkel (Admin, Service Advisor, Mekanik, Kasir)",
)
async def login_staff(
    payload: LoginRequest,
    db: AsyncSession = Depends(get_db),
) -> TokenResponse:
    stmt = select(User).where(User.username == payload.username)
    user = (await db.execute(stmt)).scalar_one_or_none()
    if user is None or not verify_password(payload.password, user.password_hash):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Username atau password salah.",
        )
    token = create_access_token(subject=user.username, role=user.role)
    return TokenResponse(
        access_token=token,
        user_id=user.id,
        username=user.username,
        full_name=user.full_name,
        role=user.role,
    )


@router.get(
    "/vehicles",
    summary="Cari Data Kendaraan Berdasarkan Plat Nomor, Merk, atau Nama Pemilik",
)
async def list_or_search_vehicles(
    q: Optional[str] = Query(
        default=None, description="Kata kunci plat nomor / model / nama pelanggan"
    ),
    db: AsyncSession = Depends(get_db),
) -> list[dict]:
    stmt = select(Vehicle, Customer).join(Customer, Vehicle.customer_id == Customer.id)
    if q:
        pattern = f"%{q.strip()}%"
        stmt = stmt.where(
            or_(
                Vehicle.license_plate.ilike(pattern),
                Vehicle.brand.ilike(pattern),
                Vehicle.model.ilike(pattern),
                Customer.name.ilike(pattern),
            )
        )
    rows = (await db.execute(stmt.order_by(Vehicle.id.desc()).limit(30))).all()
    return [
        {
            "vehicle_id": veh.id,
            "license_plate": veh.license_plate,
            "brand": veh.brand,
            "model": veh.model,
            "year": veh.year,
            "transmission": veh.transmission,
            "engine_code": veh.engine_code,
            "vin": veh.vin,
            "customer_id": cust.id,
            "customer_name": cust.name,
            "customer_phone": cust.phone,
        }
        for veh, cust in rows
    ]


@router.post(
    "/vehicles",
    status_code=status.HTTP_201_CREATED,
    summary="Daftarkan Pelanggan & Kendaraan Baru ke Bengkel",
)
async def register_customer_vehicle(
    payload: VehicleRegisterRequest,
    db: AsyncSession = Depends(get_db),
    current_user: User = Depends(get_current_active_user),
) -> dict:
    import re as _re

    plate_clean = payload.license_plate.strip().upper()
    engine_clean = (payload.engine_code or "").strip()
    if not engine_clean:
        m_cap = _re.search(r"\b(\d\.\d)\b", payload.model or "")
        engine_clean = m_cap.group(1) if m_cap else "-"

    existing_veh = (
        await db.execute(select(Vehicle).where(Vehicle.license_plate == plate_clean))
    ).scalar_one_or_none()
    if existing_veh is not None:
        if payload.brand:
            existing_veh.brand = payload.brand.strip()
        if payload.model:
            existing_veh.model = payload.model.strip()
        if payload.year:
            existing_veh.year = payload.year
        if engine_clean and engine_clean != "-":
            existing_veh.engine_code = engine_clean
        await db.commit()
        await db.refresh(existing_veh)
        return {
            "status": "updated",
            "vehicle_id": existing_veh.id,
            "customer_id": existing_veh.customer_id,
            "license_plate": existing_veh.license_plate,
            "model": existing_veh.model,
        }

    customer = (
        await db.execute(
            select(Customer).where(Customer.phone == payload.customer_phone.strip())
        )
    ).scalar_one_or_none()
    if customer is None:
        customer = Customer(
            name=payload.customer_name,
            phone=payload.customer_phone.strip(),
            address=payload.customer_address,
        )
        db.add(customer)
        await db.flush()

    vehicle = Vehicle(
        customer_id=customer.id,
        license_plate=plate_clean,
        brand=payload.brand.strip(),
        model=payload.model.strip(),
        year=payload.year,
        transmission=payload.transmission,
        vin=payload.vin,
        engine_code=engine_clean,
    )
    db.add(vehicle)
    await db.commit()
    await db.refresh(vehicle)

    return {
        "status": "created",
        "vehicle_id": vehicle.id,
        "customer_id": customer.id,
        "license_plate": vehicle.license_plate,
        "vehicle_summary": f"{vehicle.brand} {vehicle.model} ({vehicle.year} - {vehicle.transmission})",
    }


@router.post(
    "/admin/ingest-vitara-manuals",
    summary="Trigger Ekstraksi & Ingest Manual Suzuki Grand Vitara JB420 (Vol 1.pdf & Vol 2.pdf)",
)
async def trigger_vitara_manuals_ingest(
    folder_path: str = Query(
        default=settings.VITARA_MANUAL_DIR,
        description="Path ke sub-folder manual repair suzuki vitara",
    ),
    db: AsyncSession = Depends(get_db),
    current_user: User = Depends(get_current_active_user),
) -> dict:
    from app.db.ingest_vitara_manuals import ingest_vitara_folder

    chunks_count = await ingest_vitara_folder(
        session=db, folder_path=Path(folder_path)
    )
    await db.commit()
    return {
        "status": "success",
        "folder_scanned": str(Path(folder_path).resolve()),
        "indexed_rag_chunks": chunks_count,
        "message": (
            f"Berhasil mengindeks {chunks_count} bagian buku manual Suzuki Grand Vitara JB420 "
            "beserta katalog 189 kode DTC, spesifikasi voltase sensor, dan pinout C37/E23/E92/E93/G30-G32."
        ),
    }
