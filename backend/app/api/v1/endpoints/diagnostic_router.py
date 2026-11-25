"""
FastAPI Router - Smart Diagnostic & Self-Learning Endpoints
===========================================================
Menghubungkan SmartDiagnosticEngine ke REST API endpoint untuk dikonsumsi oleh
aplikasi Flutter (Android APK) dan Web Dashboard.
"""

import re

from fastapi import APIRouter, Depends, File, HTTPException, Query, Response, UploadFile, status
from pydantic import BaseModel, Field
from sqlalchemy import func, select
from sqlalchemy.ext.asyncio import AsyncSession

from app.api.deps import get_current_active_user, get_db
from app.models import HistoricalCase, User
from app.services.admin_guard import require_workshop_pin
from app.services.excel_sync_service import (
    export_cases_excel_bytes,
    import_cases_from_excel_bytes,
    sync_cases_to_excel,
)
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
cases_alias_router = APIRouter(prefix="/api", tags=["Cases Excel Sync & Verification"])


class SaveCaseRequest(BaseModel):
    brand: str = Field(..., examples=["Toyota"])
    model: str = Field(..., examples=["Avanza"])
    year: int | None = Field(default=2016)
    engine_capacity: str | None = Field(default="1.3")
    engine_code: str | None = Field(default=None, examples=["1NR-VE"])
    odometer_km: int | None = Field(default=None, ge=0, examples=[75000])
    license_plate: str | None = Field(default=None, examples=["L 1234 AB"])
    mechanic_name: str | None = Field(default=None, examples=["Budi Santoso"])
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
            "engine_code": c.engine_code or "",
            "odometer_km": c.odometer_km,
            "license_plate": c.license_plate or "",
            "mechanic_name": c.mechanic_name or "",
            "verification_status": (c.verification_status or "TERVERIFIKASI").upper(),
            "created_at": c.created_at.strftime("%Y-%m-%d") if getattr(c, "created_at", None) else "",
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


@router.get(
    "/cases/export-excel",
    summary="Unduh Seluruh Basis Pengetahuan Kasus dalam Format Excel (DATA_KASUS_AGOS.xlsx)",
)
@cases_alias_router.get(
    "/cases/export-excel",
    summary="Unduh DATA_KASUS_AGOS.xlsx (PRD Alias)",
)
async def export_cases_excel(
    db: AsyncSession = Depends(get_db),
    current_user: User = Depends(get_current_active_user),
) -> Response:
    raw = await export_cases_excel_bytes(db)
    return Response(
        content=raw,
        media_type="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
        headers={"Content-Disposition": 'attachment; filename="DATA_KASUS_AGOS.xlsx"'},
    )


@router.post(
    "/cases/import-excel",
    summary="Impor / Tambah Kasus dari File Excel (.xlsx) ke Database & Auto-Sync",
)
@cases_alias_router.post(
    "/cases/import-excel",
    summary="Impor File DATA_KASUS_AGOS.xlsx (PRD Alias)",
)
async def import_cases_excel(
    file: UploadFile = File(...),
    db: AsyncSession = Depends(get_db),
    current_user: User = Depends(get_current_active_user),
) -> dict:
    raw = await file.read()
    if not raw:
        raise HTTPException(status_code=400, detail="File Excel kosong.")
    try:
        res = await import_cases_from_excel_bytes(db, raw)
    except Exception as exc:
        raise HTTPException(status_code=400, detail=f"Gagal membaca file Excel (.xlsx): {exc}") from exc
    return res


@cases_alias_router.get("/cases", summary="Daftar Seluruh Kasus Historis (PRD Alias)")
async def list_cases_alias(
    system_filter: str | None = Query(None),
    search: str | None = Query(None),
    db: AsyncSession = Depends(get_db),
    current_user: User = Depends(get_current_active_user),
) -> list[dict]:
    return await list_historical_cases(system_filter=system_filter, search=search, db=db, current_user=current_user)


@router.post(
    "/cases",
    status_code=status.HTTP_201_CREATED,
    summary="Simpan Kasus Selesai Baru ke Database + Auto-Sync Excel (SIMPAN_KASUS)",
)
@cases_alias_router.post(
    "/cases",
    status_code=status.HTTP_201_CREATED,
    summary="Simpan Kasus Selesai Baru + Auto-Sync Excel (PRD Alias)",
)
async def create_historical_case(
    payload: SaveCaseRequest,
    db: AsyncSession = Depends(get_db),
    current_user: User = Depends(get_current_active_user),
) -> dict:
    """Menyimpan kasus perbaikan baru (status DRAFT) + auto-sync ke DATA_KASUS_AGOS.xlsx."""
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
    dtc_list = split_dtc_codes(payload.dtc)
    dtc_stored = ", ".join(dtc_list) if dtc_list else "Tidak ada"

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
        engine_code=(payload.engine_code or "").strip().upper() or None,
        odometer_km=payload.odometer_km,
        license_plate=(payload.license_plate or "").strip().upper() or None,
        mechanic_name=(payload.mechanic_name or "").strip() or None,
        verification_status="DRAFT",
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
    excel_path = await sync_cases_to_excel(db)

    return {
        "status": "success",
        "message": f"Kasus berhasil disimpan ({new_case.case_code} · Status: DRAFT) & disinkronkan ke Excel.",
        "case_code": new_case.case_code,
        "id": new_case.id,
        "verification_status": new_case.verification_status,
        "excel_synced": bool(excel_path),
    }


@router.put(
    "/cases/{case_id}/verify",
    summary="Verifikasi Standar Bengkel oleh Kepala Bengkel (PIN) + Auto-Sync Excel (REQ-08)",
)
@cases_alias_router.put(
    "/cases/{case_id}/verify",
    summary="Verifikasi Kasus Standar Bengkel (PRD Alias)",
)
async def verify_historical_case(
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
    case_obj.verification_status = "TERVERIFIKASI"
    await db.commit()
    excel_path = await sync_cases_to_excel(db)
    return {
        "status": "verified",
        "id": case_obj.id,
        "case_code": case_obj.case_code,
        "verification_status": "TERVERIFIKASI",
        "excel_synced": bool(excel_path),
        "message": f"Kasus {case_obj.case_code} resmi TERVERIFIKASI Standar Bengkel & tersinkron ke Excel.",
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
    await sync_cases_to_excel(db)
    return {"status": "deleted", "case_code": code, "message": f"Kasus {code} dihapus & Excel disinkronkan."}


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
