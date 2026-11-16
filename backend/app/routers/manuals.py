"""
Repair Manual, Wiring Diagram, DTC Codes, and Sensor Specs router.
"""

from fastapi import APIRouter, Depends, HTTPException, Query, status
from sqlalchemy import select, or_
from sqlalchemy.ext.asyncio import AsyncSession

from app.database import get_db
from app.models.user import User
from app.models.manual import RepairManual, WiringDiagram, DTCCode, SensorSpec
from app.schemas.manual import (
    RepairManualCreate, RepairManualResponse,
    WiringDiagramCreate, WiringDiagramResponse,
    DTCCodeCreate, DTCCodeResponse,
    SensorSpecCreate, SensorSpecResponse,
)
from app.utils.deps import get_current_user

router = APIRouter(prefix="/manuals", tags=["Manuals & Wiring"])


# ── Repair Manuals ───────────────────────────────────────────────────────────

@router.get("/", response_model=list[RepairManualResponse])
async def list_manuals(
    search: str | None = Query(None, description="Cari judul atau konten manual"),
    brand: str | None = Query(None),
    model: str | None = Query(None),
    category: str | None = Query(None),
    db: AsyncSession = Depends(get_db),
    _user: User = Depends(get_current_user),
):
    """Search and list repair manuals."""
    stmt = select(RepairManual).order_by(RepairManual.brand, RepairManual.model)
    if search:
        stmt = stmt.where(
            or_(
                RepairManual.title.ilike(f"%{search}%"),
                RepairManual.content.ilike(f"%{search}%"),
            )
        )
    if brand:
        stmt = stmt.where(RepairManual.brand.ilike(f"%{brand}%"))
    if model:
        stmt = stmt.where(RepairManual.model.ilike(f"%{model}%"))
    if category:
        stmt = stmt.where(RepairManual.category == category)
    result = await db.execute(stmt)
    return result.scalars().all()


@router.post("/", response_model=RepairManualResponse, status_code=201)
async def create_manual(
    data: RepairManualCreate,
    db: AsyncSession = Depends(get_db),
    _user: User = Depends(get_current_user),
):
    """Add a new repair manual entry."""
    manual = RepairManual(**data.model_dump())
    db.add(manual)
    await db.flush()
    await db.refresh(manual)
    return manual


# ── Wiring Diagrams ──────────────────────────────────────────────────────────

@router.get("/wiring", response_model=list[WiringDiagramResponse])
async def list_wiring_diagrams(
    brand: str | None = Query(None),
    model: str | None = Query(None),
    system_name: str | None = Query(None, description="Nama sistem: ECU Main, ABS, AC, dll"),
    db: AsyncSession = Depends(get_db),
    _user: User = Depends(get_current_user),
):
    """List wiring diagrams with filters."""
    stmt = select(WiringDiagram).order_by(WiringDiagram.brand, WiringDiagram.system_name)
    if brand:
        stmt = stmt.where(WiringDiagram.brand.ilike(f"%{brand}%"))
    if model:
        stmt = stmt.where(WiringDiagram.model.ilike(f"%{model}%"))
    if system_name:
        stmt = stmt.where(WiringDiagram.system_name.ilike(f"%{system_name}%"))
    result = await db.execute(stmt)
    return result.scalars().all()


@router.post("/wiring", response_model=WiringDiagramResponse, status_code=201)
async def create_wiring_diagram(
    data: WiringDiagramCreate,
    db: AsyncSession = Depends(get_db),
    _user: User = Depends(get_current_user),
):
    """Add a new wiring diagram entry."""
    wd = WiringDiagram(**data.model_dump())
    db.add(wd)
    await db.flush()
    await db.refresh(wd)
    return wd


# ── DTC Codes ────────────────────────────────────────────────────────────────

@router.get("/dtc", response_model=list[DTCCodeResponse])
async def list_dtc_codes(
    search: str | None = Query(None, description="Cari kode DTC atau deskripsi"),
    severity: str | None = Query(None),
    system_category: str | None = Query(None),
    db: AsyncSession = Depends(get_db),
    _user: User = Depends(get_current_user),
):
    """Search DTC codes."""
    stmt = select(DTCCode).order_by(DTCCode.code)
    if search:
        stmt = stmt.where(
            or_(
                DTCCode.code.ilike(f"%{search}%"),
                DTCCode.description_en.ilike(f"%{search}%"),
                DTCCode.description_id.ilike(f"%{search}%"),
            )
        )
    if severity:
        stmt = stmt.where(DTCCode.severity == severity)
    if system_category:
        stmt = stmt.where(DTCCode.system_category == system_category)
    result = await db.execute(stmt)
    return result.scalars().all()


@router.get("/dtc/{code}", response_model=DTCCodeResponse)
async def get_dtc_code(
    code: str,
    db: AsyncSession = Depends(get_db),
    _user: User = Depends(get_current_user),
):
    """Get detailed info for a specific DTC code."""
    result = await db.execute(
        select(DTCCode).where(DTCCode.code == code.upper())
    )
    dtc = result.scalar_one_or_none()
    if not dtc:
        raise HTTPException(status_code=404, detail=f"Kode DTC '{code}' tidak ditemukan")
    return dtc


@router.post("/dtc", response_model=DTCCodeResponse, status_code=201)
async def create_dtc_code(
    data: DTCCodeCreate,
    db: AsyncSession = Depends(get_db),
    _user: User = Depends(get_current_user),
):
    """Add a new DTC code entry."""
    dtc = DTCCode(**data.model_dump())
    dtc.code = dtc.code.upper()
    db.add(dtc)
    await db.flush()
    await db.refresh(dtc)
    return dtc


# ── Sensor Specs ─────────────────────────────────────────────────────────────

@router.get("/sensors", response_model=list[SensorSpecResponse])
async def list_sensor_specs(
    brand: str | None = Query(None),
    model: str | None = Query(None),
    sensor_name: str | None = Query(None),
    db: AsyncSession = Depends(get_db),
    _user: User = Depends(get_current_user),
):
    """List sensor specifications."""
    stmt = select(SensorSpec).order_by(SensorSpec.brand, SensorSpec.sensor_name)
    if brand:
        stmt = stmt.where(SensorSpec.brand.ilike(f"%{brand}%"))
    if model:
        stmt = stmt.where(SensorSpec.model.ilike(f"%{model}%"))
    if sensor_name:
        stmt = stmt.where(SensorSpec.sensor_name.ilike(f"%{sensor_name}%"))
    result = await db.execute(stmt)
    return result.scalars().all()


@router.post("/sensors", response_model=SensorSpecResponse, status_code=201)
async def create_sensor_spec(
    data: SensorSpecCreate,
    db: AsyncSession = Depends(get_db),
    _user: User = Depends(get_current_user),
):
    """Add a new sensor specification."""
    spec = SensorSpec(**data.model_dump())
    db.add(spec)
    await db.flush()
    await db.refresh(spec)
    return spec
