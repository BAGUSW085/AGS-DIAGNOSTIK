"""
FastAPI Router - Smart Diagnostic & Self-Learning Endpoints
===========================================================
Menghubungkan SmartDiagnosticEngine ke REST API endpoint untuk dikonsumsi oleh
aplikasi Flutter (Android APK) dan Web Dashboard.
"""

import re

from fastapi import APIRouter, Depends, HTTPException, Query, status
from pydantic import BaseModel, Field
from sqlalchemy import func, select
from sqlalchemy.ext.asyncio import AsyncSession

from app.api.deps import get_current_active_user, get_db
from app.models import HistoricalCase, User
from app.services.admin_guard import require_workshop_pin
from app.services.diagnostic_service import (
    DiagnosticRequest,
    DiagnosticResponse,
    ManualRepairAdvice,
    SelfLearningFeedbackRequest,
    SmartDiagnosticEngine,
    WeightedCaseSearchRequest,
    WeightedCaseSearchResponse,
    WeightedDiagnosticEngine,
    split_dtc_codes,
)

router = APIRouter(prefix="/api/v1/diagnostics", tags=["Smart Fault Diagnostic"])


class SaveCaseRequest(BaseModel):
    brand: str = Field(..., examples=["Toyota"])
    model: str = Field(..., examples=["Avanza"])
    year: int | None = Field(default=2016)
    engine_capacity: str | None = Field(default="1.3")
    complaint: str = Field(..., examples=["Mesin brebet"])
    symptom: str = Field(..., examples=["Idle tidak stabil"])
    dtc: str | None = Field(default="P0171")
    stft: float | None = Field(default=None)
    ltft: float | None = Field(default=None)
    rpm: float | None = Field(default=None)
    o2_voltage: str | None = Field(default=None)
    map_kpa: float | None = Field(default=None)
    maf_gps: float | None = Field(default=None)
    ect_c: float | None = Field(default=None)
    inspection_findings: str = Field(..., examples=["Selang intake retak"])
    final_diagnosis: str = Field(..., examples=["Kebocoran intake"])
    repair_action: str = Field(..., examples=["Ganti selang intake"])
    system_category: str = Field(default="Udara", examples=["Udara"])
    affected_system: str | None = Field(default=None)


@router.post(
    "/search-case",
    response_model=WeightedCaseSearchResponse,
    status_code=status.HTTP_200_OK,
    summary="Pencarian Kasus Diagnosis Berbobot (Formula Excel) + Solusi Manual Repair",
)
async def search_weighted_case(
    payload: WeightedCaseSearchRequest,
    db: AsyncSession = Depends(get_db),
    current_user: User = Depends(get_current_active_user),
) -> WeightedCaseSearchResponse:
    """
    Menghitung skor kemiripan kasus historis berdasarkan input teks & live data scanner,
    menampilkan ringkasan ranking sistem, serta menyajikan panduan manual repair book langsung!
    """
    return await WeightedDiagnosticEngine.search_weighted_cases(session=db, req=payload)


@router.get(
    "/cases",
    summary="Daftar Seluruh Kasus Historis Database (Dataset Excel K001 - K012+)",
)
async def list_historical_cases(
    system_filter: str | None = Query(None, description="Filter nama sistem"),
    search: str | None = Query(None, description="Pencarian bebas keluhan/gejala/model"),
    db: AsyncSession = Depends(get_db),
    current_user: User = Depends(get_current_active_user),
) -> list[dict]:
    query = select(HistoricalCase).order_by(HistoricalCase.case_code.asc())
    if system_filter and system_filter.strip().lower() not in {"", "semua", "all"}:
        query = query.where(HistoricalCase.system_category.ilike(f"%{system_filter.strip()}%"))
    if search and search.strip():
        term = f"%{search.strip()}%"
        query = query.where(
            (HistoricalCase.complaint.ilike(term))
            | (HistoricalCase.symptom.ilike(term))
            | (HistoricalCase.model.ilike(term))
            | (HistoricalCase.final_diagnosis.ilike(term))
            | (HistoricalCase.dtc.ilike(term))
        )
    cases = (await db.execute(query)).scalars().all()
    return [
        {
            "id": c.id,
            "case_code": c.case_code,
            "brand": c.brand,
            "model": c.model,
            "year": c.year,
            "engine_capacity": c.engine_capacity,
            "complaint": c.complaint,
            "symptom": c.symptom,
            "dtc": c.dtc or "Tidak ada",
            "stft": c.stft,
            "ltft": c.ltft,
            "rpm": c.rpm,
            "o2_voltage": c.o2_voltage or "-",
            "map_kpa": c.map_kpa,
            "maf_gps": c.maf_gps,
            "ect_c": c.ect_c,
            "inspection_findings": c.inspection_findings,
            "final_diagnosis": c.final_diagnosis,
            "repair_action": c.repair_action,
            "system_category": c.system_category,
            "affected_system": c.affected_system or "-",
            "group_category": c.group_category,
            "manual_book_ref": c.manual_book_ref,
        }
        for c in cases
    ]


@router.post(
    "/cases",
    status_code=status.HTTP_201_CREATED,
    summary="Simpan Kasus Selesai Baru ke Database (SIMPAN_KASUS)",
)
async def create_historical_case(
    payload: SaveCaseRequest,
    db: AsyncSession = Depends(get_db),
    current_user: User = Depends(get_current_active_user),
) -> dict:
    """Menyimpan kasus perbaikan baru dengan auto-generate case_code K0xx bebas bentrok."""
    existing_codes = set(
        (await db.execute(select(HistoricalCase.case_code))).scalars().all()
    )
    max_num = len(existing_codes)
    for code in existing_codes:
        m = re.match(r"^K(\d+)$", (code or "").strip(), re.IGNORECASE)
        if m:
            max_num = max(max_num, int(m.group(1)))

    next_num = max_num + 1
    new_code = f"K{str(next_num).zfill(3)}"
    while new_code in existing_codes:
        next_num += 1
        new_code = f"K{str(next_num).zfill(3)}"

    brand_clean = payload.brand.strip()
    if brand_clean.islower():
        brand_clean = brand_clean.title()
    model_clean = payload.model.strip()
    if model_clean.islower():
        model_clean = model_clean.title()
    # Simpan SEMUA kode DTC (dipisah koma/spasi/titik koma), tanpa duplikat, urutan terjaga
    dtc_list = split_dtc_codes(payload.dtc)
    dtc_stored = ", ".join(dtc_list) if dtc_list else "Tidak ada"

    # Generate manual book guidance (memakai seluruh kode DTC)
    advice = WeightedDiagnosticEngine.get_repair_manual_guidance(
        payload.final_diagnosis, ", ".join(dtc_list) if dtc_list else None
    )
    manual_ref = f"{advice.manual_book_section}. Tindakan: {payload.repair_action}"

    new_case = HistoricalCase(
        case_code=new_code,
        brand=brand_clean,
        model=model_clean,
        year=payload.year,
        engine_capacity=payload.engine_capacity or "-",
        complaint=payload.complaint.strip(),
        symptom=payload.symptom.strip(),
        dtc=dtc_stored,
        stft=payload.stft,
        ltft=payload.ltft,
        rpm=payload.rpm,
        o2_voltage=payload.o2_voltage,
        map_kpa=payload.map_kpa,
        maf_gps=payload.maf_gps,
        ect_c=payload.ect_c,
        inspection_findings=payload.inspection_findings.strip(),
        final_diagnosis=payload.final_diagnosis.strip(),
        repair_action=payload.repair_action.strip(),
        system_category=payload.system_category,
        affected_system=payload.affected_system,
        group_category="Pendukung" if payload.system_category in {"Pendingin", "Pelumasan", "Kelistrikan", "Emisi"} else "Pembakaran",
        manual_book_ref=manual_ref,
    )
    db.add(new_case)
    await db.commit()
    await db.refresh(new_case)

    return {
        "status": "success",
        "message": f"Kasus berhasil disimpan dengan kode {new_case.case_code}",
        "case_code": new_case.case_code,
        "id": new_case.id,
    }


@router.delete(
    "/cases/{case_id}",
    summary="Hapus Kasus Historis dari Database (Dilindungi PIN Kepala Bengkel)",
)
async def delete_historical_case(
    case_id: int,
    _pin_ok: str = Depends(require_workshop_pin),
    db: AsyncSession = Depends(get_db),
    current_user: User = Depends(get_current_active_user),
) -> dict:
    case_obj = (
        await db.execute(select(HistoricalCase).where(HistoricalCase.id == case_id))
    ).scalar_one_or_none()
    if not case_obj:
        raise HTTPException(status_code=404, detail="Data kasus tidak ditemukan.")
    code = case_obj.case_code
    await db.delete(case_obj)
    await db.commit()
    return {"status": "deleted", "case_code": code, "message": f"Kasus {code} dihapus."}


@router.get(
    "/repair-manual-advice",
    response_model=ManualRepairAdvice,
    summary="Dapatkan Saran Penyelesaian Masalah Langsung dari Manual Repair Book",
)
async def get_repair_advice(
    diagnosis: str = Query(..., description="Diagnosis akhir kerusakan"),
    dtc: str | None = Query(None, description="Kode DTC (opsional)"),
    current_user: User = Depends(get_current_active_user),
) -> ManualRepairAdvice:
    return WeightedDiagnosticEngine.get_repair_manual_guidance(diagnosis=diagnosis, dtc=dtc)


@router.post(
    "/analyze",
    response_model=DiagnosticResponse,
    status_code=status.HTTP_200_OK,
    summary="Analisa Gejala & Kode DTC untuk Rekomendasi Titik Cek Mekanik",
)
async def analyze_vehicle_fault(
    payload: DiagnosticRequest,
    db: AsyncSession = Depends(get_db),
    current_user: User = Depends(get_current_active_user),
) -> DiagnosticResponse:
    """
    Menerima input merk, model, keluhan gejala pelanggan, dan kode DTC OBD-II,
    lalu mengembalikan daftar ranking `FaultCheckpoint` dengan persentase probabilitas (0-100%).
    """
    return await SmartDiagnosticEngine.diagnose(session=db, payload=payload)


@router.post(
    "/feedback-learn",
    status_code=status.HTTP_201_CREATED,
    summary="Simpan Hasil Perbaikan & Latih Ulang Bobot Diagnosa (Self-Learning Loop)",
)
async def submit_diagnostic_feedback(
    payload: SelfLearningFeedbackRequest,
    db: AsyncSession = Depends(get_db),
    current_user: User = Depends(get_current_active_user),
) -> dict:
    """
    Dipanggil saat Mekanik atau Service Advisor menyelesaikan Work Order (PKB).
    Menyimpan riwayat ke `fault_histories` dan meng-update bobot `symptom_checkpoint_links`.
    """
    if current_user.role not in {"admin", "mekanik", "service_advisor"}:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Hanya Mekanik, Service Advisor, atau Admin yang dapat memverifikasi hasil diagnosa.",
        )

    history = await SmartDiagnosticEngine.record_resolution_and_learn(
        session=db, feedback=payload
    )
    await db.commit()

    return {
        "status": "success",
        "message": "Data perbaikan berhasil disimpan dan bobot Smart Diagnostic telah diperbarui.",
        "fault_history_id": history.id,
    }
