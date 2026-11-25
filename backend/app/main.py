"""
FastAPI Main Application Entrypoint - Project Bengkel Masa Depan
================================================================
Menyatukan seluruh router:
- Auth, Vehicles & Admin Ingest (`core_auth_deps.py` / `auth_vehicle_router.py`)
- Pilar 1: Smart Fault Diagnostic & EMA Self-Learning (`diagnostic_router.py`)
- Pilar 2: AI Repair Manual, 189 DTC JB420, Sensor Spec & Pinout ECU (`manual_wiring_service.py`)
- Pilar 3: POS Kasir (PPN 11%) & Work Order Auto Stock Deduction (`pos_workorder_service.py`)

Cara menjalankan server dev lokal:
    uvicorn app.main:app --reload --host 0.0.0.0 --port 8000
"""

from contextlib import asynccontextmanager
import logging
from pathlib import Path

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import FileResponse
from fastapi.staticfiles import StaticFiles
from sqlalchemy import func, select
from sqlalchemy.ext.asyncio import AsyncSession, async_sessionmaker, create_async_engine

from app.api.v1.endpoints.diagnostic_router import router as diagnostic_router
from app.core.config import settings
from app.models import Base, DTCCode, HistoricalCase, User
from app.services.admin_guard import router as admin_guard_router
from app.services.manual_wiring_service import router as manual_wiring_router
from app.services.ewd_viewer_service import router as ewd_viewer_router

try:
    from app.api.v1.endpoints.auth_vehicle_router import router as auth_vehicle_router
except ImportError:
    from core_auth_deps import router as auth_vehicle_router  # type: ignore[no-redef]

logging.basicConfig(level=logging.INFO, format="%(levelname)s: %(message)s")
logger = logging.getLogger(__name__)


@asynccontextmanager
async def lifespan(app: FastAPI):
    """
    Inisialisasi skema 16 tabel ORM otomatis saat server dinyalakan,
    serta memuat data referensi Suzuki Grand Vitara JB420 (`Vol 1.pdf`, `Vol 2.pdf`,
    dan `jb420_extracted_catalog.json`) jika sudah tersedia.
    """
    engine = create_async_engine(settings.DATABASE_URL, echo=False)
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)

    # Otomatis suntikkan referensi terstruktur JB420 & Kasus Historis Excel (K001 - K012)
    # Fast-path untuk Vercel/Serverless jika DB pre-seeded sudah terisi lengkap
    try:
        session_factory = async_sessionmaker(
            engine, expire_on_commit=False, class_=AsyncSession
        )
        already_populated = False
        async with session_factory() as check_session:
            dtc_cnt = (await check_session.execute(select(func.count(DTCCode.id)))).scalar() or 0
            hc_cnt = (await check_session.execute(select(func.count(HistoricalCase.id)))).scalar() or 0
            usr_cnt = (await check_session.execute(select(func.count(User.id)))).scalar() or 0
            if dtc_cnt >= 180 and hc_cnt >= 1 and usr_cnt >= 1:
                already_populated = True

        if not already_populated:
            from app.db.ingest_vitara_manuals import seed_jb420_structured_reference_data
            from app.db.seed_historical_cases import seed_historical_cases

            async with session_factory() as session:
                try:
                    async with session.begin():
                        await seed_jb420_structured_reference_data(session)
                except Exception as e_jb:
                    logger.warning("Auto-seed JB420 referensi dilewati: %s", e_jb)

                try:
                    async with session.begin():
                        await seed_historical_cases(session)
                except Exception as e_hc:
                    logger.warning("Auto-seed kasus historis dilewati: %s", e_hc)

                try:
                    from app.db.seed_data import (
                        is_already_seeded,
                        seed_customers_and_vehicles,
                        seed_diagnostic_knowledge_base,
                        seed_inventory_and_sample_work_order,
                        seed_manuals_dtc_and_wiring,
                        seed_users,
                    )

                    async with session.begin():
                        if not await is_already_seeded(session):
                            u_map = await seed_users(session)
                            v_map = await seed_customers_and_vehicles(session)
                            await seed_diagnostic_knowledge_base(session, v_map)
                            await seed_manuals_dtc_and_wiring(session)
                            await seed_inventory_and_sample_work_order(
                                session, u_map, v_map
                            )
                except Exception as e_seed:
                    logger.warning("Auto-seed data umum dilewati: %s", e_seed)

        logger.info(
            "Data referensi Suzuki Grand Vitara JB420 & Kasus Historis siap (fast_path=%s).",
            already_populated,
        )
    except Exception as exc:
        logger.warning("Auto-seed referensi dilewati saat startup: %s", exc)

    logger.info("Database schema AGOS SMART DIAGNOSTIK by Agos Corporation siap digunakan.")
    yield
    await engine.dispose()


app = FastAPI(
    title="AGOS SMART DIAGNOSTIK by Agos Corporation API",
    description=(
        "Backend REST API & AI Engine untuk Smart Fault Diagnostic Multi-Merek (Asia, Eropa, China), "
        "RAG Repair Manual & Wiring Assistant Multi-Buku (Suzuki Grand Vitara JB420, Suzuki Ertiga Gen 1, "
        "Toyota Avanza/Xenia, Fortuner, Innova, Hilux/HiAce, Yaris/Vios, Corolla/Camry/Alphard), "
        "serta Katalog Modern Diesel Common-Rail, Turbo, VVT, Hybrid & EV."
    ),
    version="2.2.0",
    lifespan=lifespan,
)

# Izinkan akses dari Flutter Android APK / Web
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Registrasi Router Auth/Kendaraan, Diagnostik, Manual Multi-Merek & Admin Security/Backup
app.include_router(auth_vehicle_router)
app.include_router(diagnostic_router)
app.include_router(manual_wiring_router)
app.include_router(ewd_viewer_router)
app.include_router(admin_guard_router)

# Mount Web Dashboard SPA & Static Assets
STATIC_DIR = Path(__file__).parent / "static"
if STATIC_DIR.exists():
    app.mount("/static", StaticFiles(directory=str(STATIC_DIR)), name="static")


@app.get("/", include_in_schema=False)
async def serve_web_dashboard():
    """Melayani Web Dashboard Interaktif AGOS SMART DIAGNOSTIK by Agos Corporation."""
    index_file = STATIC_DIR / "index.html"
    if index_file.exists():
        return FileResponse(index_file, headers={"Cache-Control": "no-cache, must-revalidate"})
    return {"message": "AGOS SMART DIAGNOSTIK by Agos Corporation API running. Static index.html not found."}


@app.get("/manifest.json", include_in_schema=False)
async def serve_pwa_manifest():
    """Melayani Web App Manifest untuk instalasi Aplikasi Android (PWA / WebAPK)."""
    manifest_file = STATIC_DIR / "manifest.json"
    if manifest_file.exists():
        return FileResponse(manifest_file, media_type="application/manifest+json")
    return {"error": "manifest.json not found"}


@app.get("/sw.js", include_in_schema=False)
async def serve_service_worker():
    """Melayani Service Worker di root scope agar aplikasi dapat diinstal di HP Android."""
    sw_file = STATIC_DIR / "sw.js"
    if sw_file.exists():
        return FileResponse(
            sw_file,
            media_type="application/javascript",
            headers={"Service-Worker-Allowed": "/", "Cache-Control": "no-cache, must-revalidate"},
        )
    return {"error": "sw.js not found"}


@app.get("/health", tags=["System Health"])
async def health_check() -> dict:
    from app.services.vehicle_applicability import list_all_manual_pack_summaries

    catalog_path = Path(__file__).with_name("jb420_extracted_catalog.json")
    packs = list_all_manual_pack_summaries()
    total_dtcs = sum(p.dtc_count for p in packs)
    total_pins = sum(p.pinout_count for p in packs)
    return {
        "status": "healthy",
        "service": "AGOS SMART DIAGNOSTIK by Agos Corporation",
        "version": "2.2.0",
        "jb420_catalog_loaded": catalog_path.exists(),
        "active_manuals_count": len(packs),
        "total_mapped_dtcs": total_dtcs,
        "total_mapped_pinouts": total_pins,
        "pillars": [
            "1. Smart Fault Diagnostic Multi-Merek (66 Generasi · 174 Kode Mesin Asia/Eropa/China · Bensin/Diesel/Hybrid/EV)",
            f"2. AI Repair Manual & Wiring Assistant ({len(packs)} Buku Manual Resmi · {total_dtcs}+ DTC · {total_pins}+ Pinout)",
            "3. Workshop Tech Suite (Fuel Trim, MAP Vakum, Voltage Drop, DLC 16-Pin & Quick DTC Decoder Terikat Manual)",
        ],
    }