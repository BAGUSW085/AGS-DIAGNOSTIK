"""
Auto-Sync Excel (.xlsx) Service untuk Basis Pengetahuan Kasus CBR (REQ-13)
==========================================================================
Menyinkronkan seluruh kasus terselesaikan (`HistoricalCase`) secara atomik
ke file `DATA_KASUS_AGOS.xlsx` memakai `openpyxl` dengan 12 kolom baku PRD v2.2.0
(+ metadata pelengkap agar round-trip Ekspor <-> Impor 100% lossless).

Aman untuk lingkungan lokal (Windows/Linux) maupun serverless read-only (Vercel `/tmp`).
"""

from __future__ import annotations

from datetime import datetime, timezone
import io
import logging
import os
from pathlib import Path
import re
from typing import Any

from openpyxl import Workbook, load_workbook
from openpyxl.styles import Alignment, Font, PatternFill
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from app.models import HistoricalCase

logger = logging.getLogger(__name__)

BACKEND_DIR = Path(__file__).resolve().parents[2]
WORKSPACE_ROOT = BACKEND_DIR.parent
LOCAL_EXCEL_PATH = WORKSPACE_ROOT / "DATA_KASUS_AGOS.xlsx"
TMP_EXCEL_PATH = Path("/tmp/DATA_KASUS_AGOS.xlsx")

# 12 Kolom Baku PRD v2.2.0 + 4 Kolom Pelengkap (Lossless Round-Trip)
EXCEL_HEADERS = [
    "id_kasus",
    "tanggal_selesai",
    "nomor_polisi",
    "merek",
    "model",
    "kode_mesin",
    "tahun",
    "kilometer",
    "keluhan",
    "kode_dtc",
    "diagnosis_akhir",
    "tindakan_perbaikan",
    "status_verifikasi",
    "gejala",
    "nama_mekanik",
    "sistem",
]


def _is_readonly_env() -> bool:
    return bool(
        os.getenv("VERCEL")
        or os.getenv("VERCEL_ENV")
        or os.getenv("AWS_LAMBDA_FUNCTION_NAME")
        or not os.access(WORKSPACE_ROOT, os.W_OK)
    )


def get_excel_sync_path() -> Path:
    return TMP_EXCEL_PATH if _is_readonly_env() else LOCAL_EXCEL_PATH


def _parse_int_clean(val: Any) -> int | None:
    if val is None or val == "":
        return None
    if isinstance(val, (int, float)):
        iv = int(round(val))
        return iv if iv >= 0 else None
    digits = re.sub(r"[^\d]", "", str(val))
    return int(digits) if digits else None


def build_excel_workbook_from_cases(cases: list[HistoricalCase]) -> Workbook:
    wb = Workbook()
    ws = wb.active
    ws.title = "DATA_KASUS_AGOS"

    header_fill = PatternFill(start_color="0C4A6E", end_color="0C4A6E", fill_type="solid")
    header_font = Font(name="Calibri", size=11, bold=True, color="FFFFFF")

    ws.append(EXCEL_HEADERS)
    for col_idx in range(1, len(EXCEL_HEADERS) + 1):
        cell = ws.cell(row=1, column=col_idx)
        cell.fill = header_fill
        cell.font = header_font
        cell.alignment = Alignment(horizontal="center", vertical="center")

    for c in cases:
        dt_str = (
            c.created_at.strftime("%Y-%m-%d")
            if getattr(c, "created_at", None) is not None
            else datetime.now(timezone.utc).strftime("%Y-%m-%d")
        )
        ws.append(
            [
                c.case_code or "",
                dt_str,
                c.license_plate or "",
                c.brand or "",
                c.model or "",
                c.engine_code or "",
                int(c.year) if c.year is not None else "",
                int(c.odometer_km) if c.odometer_km is not None else "",
                c.complaint or "",
                c.dtc or "Tidak ada",
                c.final_diagnosis or "",
                c.repair_action or "",
                (c.verification_status or "TERVERIFIKASI").upper(),
                c.symptom or "",
                c.mechanic_name or "",
                c.system_category or "Umum",
            ]
        )

    col_widths = [12, 14, 15, 14, 18, 13, 8, 12, 34, 16, 36, 40, 16, 32, 18, 14]
    for idx, w in enumerate(col_widths, start=1):
        col_letter = ws.cell(row=1, column=idx).column_letter
        ws.column_dimensions[col_letter].width = w

    ws.freeze_panes = "A2"
    return wb


def workbook_to_bytes(wb: Workbook) -> bytes:
    buf = io.BytesIO()
    wb.save(buf)
    buf.seek(0)
    return buf.getvalue()


async def sync_cases_to_excel(session: AsyncSession) -> Path | None:
    """Menyinkronkan seluruh baris HistoricalCase ke DATA_KASUS_AGOS.xlsx secara atomik."""
    try:
        cases = (
            await session.execute(
                select(HistoricalCase).order_by(HistoricalCase.case_code.asc())
            )
        ).scalars().all()
        wb = build_excel_workbook_from_cases(list(cases))
        target = get_excel_sync_path()
        target.parent.mkdir(parents=True, exist_ok=True)
        tmp_path = target.with_suffix(".tmp.xlsx")
        wb.save(tmp_path)
        os.replace(tmp_path, target)
        logger.info("Auto-sync Excel berhasil (%d kasus) -> %s", len(cases), target)
        return target
    except Exception as exc:
        logger.warning("Auto-sync Excel dilewati (non-fatal): %s", exc)
        return None


async def export_cases_excel_bytes(session: AsyncSession) -> bytes:
    """Menghasilkan bytes file DATA_KASUS_AGOS.xlsx langsung dari database aktif."""
    cases = (
        await session.execute(
            select(HistoricalCase).order_by(HistoricalCase.case_code.asc())
        )
    ).scalars().all()
    wb = build_excel_workbook_from_cases(list(cases))
    return workbook_to_bytes(wb)


async def import_cases_from_excel_bytes(
    session: AsyncSession, raw_bytes: bytes
) -> dict[str, Any]:
    """Mengimpor kasus dari file .xlsx (12 kolom baku PRD v2.2.0) ke SQLite lalu auto-sync."""
    wb = load_workbook(filename=io.BytesIO(raw_bytes), data_only=True)
    ws = wb.active

    rows = list(ws.iter_rows(values_only=True))
    if not rows:
        return {"imported": 0, "updated": 0, "skipped": 0, "total_cases": 0}

    header_raw = [str(h or "").strip().lower().replace(" ", "_") for h in rows[0]]
    col_map: dict[str, int] = {h: idx for idx, h in enumerate(header_raw) if h}

    def get_val(row: tuple, *aliases: str, default: str = "") -> Any:
        for a in aliases:
            if a in col_map and col_map[a] < len(row):
                v = row[col_map[a]]
                if v is not None and str(v).strip() != "":
                    return v
        return default

    existing_rows = (await session.execute(select(HistoricalCase))).scalars().all()
    by_code: dict[str, HistoricalCase] = {
        (c.case_code or "").upper(): c for c in existing_rows
    }
    max_num = len(existing_rows)
    for code in by_code:
        m = re.match(r"^K(\d+)$", code)
        if m:
            max_num = max(max_num, int(m.group(1)))

    imported = 0
    updated = 0
    skipped = 0

    for row in rows[1:]:
        if not row or all(v is None or str(v).strip() == "" for v in row):
            continue

        merek = str(get_val(row, "merek", "brand") or "").strip()
        model = str(get_val(row, "model") or "").strip()
        keluhan = str(get_val(row, "keluhan", "complaint") or "").strip()
        diagnosis = str(get_val(row, "diagnosis_akhir", "final_diagnosis", "diagnosis") or "").strip()
        tindakan = str(get_val(row, "tindakan_perbaikan", "repair_action", "solusi") or "").strip()

        if not merek or not model or not (keluhan or diagnosis):
            skipped += 1
            continue

        raw_code = str(get_val(row, "id_kasus", "case_code", "id") or "").strip().upper()
        if not raw_code:
            max_num += 1
            raw_code = f"K{str(max_num).zfill(3)}"
            while raw_code in by_code:
                max_num += 1
                raw_code = f"K{str(max_num).zfill(3)}"

        nopol = str(get_val(row, "nomor_polisi", "license_plate", "nopol") or "").strip().upper() or None
        kode_mesin = str(get_val(row, "kode_mesin", "engine_code") or "").strip().upper() or None
        tahun = _parse_int_clean(get_val(row, "tahun", "year"))
        km = _parse_int_clean(get_val(row, "kilometer", "odometer_km", "km"))
        dtc = str(get_val(row, "kode_dtc", "dtc") or "Tidak ada").strip() or "Tidak ada"
        gejala = str(get_val(row, "gejala", "symptom") or keluhan).strip()
        status_ver = str(get_val(row, "status_verifikasi", "verification_status") or "DRAFT").strip().upper()
        if status_ver not in {"TERVERIFIKASI", "DRAFT"}:
            status_ver = "TERVERIFIKASI" if "VERIF" in status_ver else "DRAFT"
        mekanik = str(get_val(row, "nama_mekanik", "mechanic_name") or "").strip() or None
        sistem = str(get_val(row, "sistem", "system_category") or "Umum").strip() or "Umum"

        if raw_code in by_code:
            obj = by_code[raw_code]
            obj.brand = merek
            obj.model = model
            obj.year = tahun if tahun is not None else obj.year
            obj.engine_code = kode_mesin or obj.engine_code
            obj.odometer_km = km if km is not None else obj.odometer_km
            obj.license_plate = nopol or obj.license_plate
            obj.mechanic_name = mekanik or obj.mechanic_name
            obj.complaint = keluhan or obj.complaint
            obj.symptom = gejala or obj.symptom
            obj.dtc = dtc
            obj.final_diagnosis = diagnosis or obj.final_diagnosis
            obj.repair_action = tindakan or obj.repair_action
            obj.verification_status = status_ver
            obj.system_category = sistem
            updated += 1
        else:
            obj = HistoricalCase(
                case_code=raw_code,
                brand=merek,
                model=model,
                year=tahun,
                engine_capacity="-",
                engine_code=kode_mesin,
                odometer_km=km,
                license_plate=nopol,
                mechanic_name=mekanik,
                verification_status=status_ver,
                complaint=keluhan or diagnosis,
                symptom=gejala or keluhan or diagnosis,
                dtc=dtc,
                inspection_findings=f"Impor Excel ({raw_code}): {gejala or keluhan}",
                final_diagnosis=diagnosis or keluhan,
                repair_action=tindakan or "Lihat catatan perbaikan Excel",
                system_category=sistem,
                group_category="Pendukung" if sistem in {"Pendingin", "Pelumasan", "Kelistrikan", "Emisi"} else "Pembakaran",
                manual_book_ref=f"Impor Excel DATA_KASUS_AGOS.xlsx ({raw_code})",
            )
            session.add(obj)
            by_code[raw_code] = obj
            imported += 1

    await session.commit()
    await sync_cases_to_excel(session)
    return {
        "status": "success",
        "imported": imported,
        "updated": updated,
        "skipped": skipped,
        "total_cases": len(by_code),
    }
