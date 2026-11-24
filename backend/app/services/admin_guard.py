"""
Workshop Admin PIN Guard & 1-Click Database Backup / Restore Service
====================================================================
Melindungi aksi sensitif bengkel (Hapus Kasus, Impor/Hapus Paket Manual,
Restore Database) dengan PIN Kepala Bengkel (4–8 digit, tersimpan sebagai
hash SHA-256) serta menyediakan fitur ekspor & restore database 1-klik.
"""

from __future__ import annotations

import hashlib
import hmac
import json
import os
import re
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

from fastapi import APIRouter, Depends, Header, HTTPException, Query, status
from pydantic import BaseModel, Field
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from app.api.deps import get_current_active_user, get_db
from app.models import HistoricalCase, User
from app.services.vehicle_applicability import (
    load_custom_manual_packs,
    save_custom_manual_pack,
)

SECURITY_CONFIG_PATH = Path(__file__).resolve().parent.parent / "data" / "workshop_security.json"
_TMP_SECURITY_CONFIG_PATH = Path("/tmp/agos_workshop_security.json")
_SALT = "agos_smart_diagnostik_workshop_pin_v1"
DEFAULT_PIN = "1234"


def _is_readonly_env() -> bool:
    return bool(
        os.getenv("VERCEL")
        or os.getenv("VERCEL_ENV")
        or os.getenv("AWS_LAMBDA_FUNCTION_NAME")
        or not os.access(SECURITY_CONFIG_PATH.parent, os.W_OK)
    )


def _get_writable_security_path() -> Path:
    return _TMP_SECURITY_CONFIG_PATH if _is_readonly_env() else SECURITY_CONFIG_PATH


def _hash_pin(pin: str) -> str:
    return hashlib.sha256(f"{_SALT}:{pin.strip()}".encode("utf-8")).hexdigest()


def _load_security_config() -> dict[str, Any]:
    target_path = _get_writable_security_path()
    read_path = target_path if target_path.exists() else SECURITY_CONFIG_PATH
    if not read_path.exists():
        default_cfg = {
            "pin_enabled": True,
            "is_default_pin": True,
            "pin_hash": _hash_pin(DEFAULT_PIN),
            "updated_at": datetime.now(timezone.utc).isoformat(),
        }
        try:
            target_path.parent.mkdir(parents=True, exist_ok=True)
            target_path.write_text(json.dumps(default_cfg, indent=2), encoding="utf-8")
        except OSError:
            pass
        return default_cfg
    try:
        data = json.loads(read_path.read_text(encoding="utf-8"))
        if not data.get("pin_hash"):
            data["pin_hash"] = _hash_pin(DEFAULT_PIN)
            data["is_default_pin"] = True
        return data
    except Exception:
        return {
            "pin_enabled": True,
            "is_default_pin": True,
            "pin_hash": _hash_pin(DEFAULT_PIN),
        }


def _save_security_config(cfg: dict[str, Any]) -> None:
    target_path = _get_writable_security_path()
    target_path.parent.mkdir(parents=True, exist_ok=True)
    target_path.write_text(json.dumps(cfg, indent=2), encoding="utf-8")


def verify_pin_value(pin: str | None) -> bool:
    if not pin:
        return False
    cfg = _load_security_config()
    expected = str(cfg.get("pin_hash", ""))
    actual = _hash_pin(pin)
    return hmac.compare_digest(expected, actual)


async def require_workshop_pin(
    x_workshop_pin: str | None = Header(default=None, alias="X-Workshop-Pin"),
) -> str:
    """FastAPI dependency: wajib menyertakan header X-Workshop-Pin yang valid untuk aksi sensitif."""
    cfg = _load_security_config()
    if not cfg.get("pin_enabled", True):
        return "disabled"
    if not verify_pin_value(x_workshop_pin):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Akses terkunci: PIN Kepala Bengkel diperlukan atau salah. Buka gembok Mode Admin terlebih dahulu.",
        )
    return "verified"


# ---------------------------------------------------------------------------
# SCHEMAS & ROUTER ADMIN
# ---------------------------------------------------------------------------

class VerifyPinRequest(BaseModel):
    pin: str = Field(..., min_length=4, max_length=12)


class ChangePinRequest(BaseModel):
    current_pin: str = Field(..., min_length=4, max_length=12)
    new_pin: str = Field(..., min_length=4, max_length=8)


class BackupRestoreRequest(BaseModel):
    historical_cases: list[dict[str, Any]] = []
    custom_manual_packs: list[dict[str, Any]] = []


router = APIRouter(prefix="/api/v1/admin", tags=["Workshop Admin Security & Backup"])


@router.get("/security-status", summary="Status PIN Kepala Bengkel")
async def get_security_status(
    current_user: User = Depends(get_current_active_user),
) -> dict[str, Any]:
    cfg = _load_security_config()
    is_def = bool(cfg.get("is_default_pin", False))
    return {
        "pin_enabled": bool(cfg.get("pin_enabled", True)),
        "is_default_pin": is_def,
        "default_hint": "PIN standar awal: 1234 (segera ubah melalui menu Mode Admin)" if is_def else None,
        "updated_at": cfg.get("updated_at"),
    }


@router.post("/verify-pin", summary="Verifikasi PIN Kepala Bengkel")
async def verify_workshop_pin(
    payload: VerifyPinRequest,
    current_user: User = Depends(get_current_active_user),
) -> dict[str, Any]:
    ok = verify_pin_value(payload.pin)
    if not ok:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="PIN Kepala Bengkel salah. Silakan coba lagi.",
        )
    cfg = _load_security_config()
    return {
        "valid": True,
        "is_default_pin": bool(cfg.get("is_default_pin", False)),
        "message": "Mode Kepala Bengkel aktif. Aksi Hapus, Impor Manual, dan Backup/Restore terbuka.",
    }


@router.post("/change-pin", summary="Ubah PIN Kepala Bengkel (4-8 digit angka)")
async def change_workshop_pin(
    payload: ChangePinRequest,
    current_user: User = Depends(get_current_active_user),
) -> dict[str, Any]:
    if not verify_pin_value(payload.current_pin):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="PIN lama salah.",
        )
    new_clean = payload.new_pin.strip()
    if not re.fullmatch(r"\d{4,8}", new_clean):
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="PIN baru harus berupa 4 sampai 8 digit angka.",
        )
    cfg = _load_security_config()
    cfg["pin_hash"] = _hash_pin(new_clean)
    cfg["is_default_pin"] = new_clean == DEFAULT_PIN
    cfg["updated_at"] = datetime.now(timezone.utc).isoformat()
    _save_security_config(cfg)
    return {
        "status": "success",
        "message": "PIN Kepala Bengkel berhasil diperbarui.",
    }


@router.get("/backup", summary="Ekspor Backup Lengkap Database Kasus & Paket Manual (JSON)")
async def export_workshop_backup(
    pin: str | None = Query(None, description="Opsional PIN via query jika tidak via header"),
    x_workshop_pin: str | None = Header(default=None, alias="X-Workshop-Pin"),
    db: AsyncSession = Depends(get_db),
    current_user: User = Depends(get_current_active_user),
) -> dict[str, Any]:
    provided_pin = x_workshop_pin or pin
    if not verify_pin_value(provided_pin):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="PIN Kepala Bengkel diperlukan untuk mengunduh backup database.",
        )

    cases = (await db.execute(select(HistoricalCase).order_by(HistoricalCase.case_code.asc()))).scalars().all()
    cases_payload = [
        {
            "case_code": c.case_code,
            "brand": c.brand,
            "model": c.model,
            "year": c.year,
            "engine_capacity": c.engine_capacity,
            "complaint": c.complaint,
            "symptom": c.symptom,
            "dtc": c.dtc,
            "stft": c.stft,
            "ltft": c.ltft,
            "rpm": c.rpm,
            "o2_voltage": c.o2_voltage,
            "map_kpa": c.map_kpa,
            "maf_gps": c.maf_gps,
            "ect_c": c.ect_c,
            "inspection_findings": c.inspection_findings,
            "final_diagnosis": c.final_diagnosis,
            "repair_action": c.repair_action,
            "system_category": c.system_category,
            "affected_system": c.affected_system,
            "group_category": c.group_category,
            "manual_book_ref": c.manual_book_ref,
        }
        for c in cases
    ]
    custom_packs = load_custom_manual_packs()

    return {
        "backup_format": "agos_smart_diagnostik_backup_v1",
        "exported_at": datetime.now(timezone.utc).isoformat(),
        "total_cases": len(cases_payload),
        "total_custom_packs": len(custom_packs),
        "historical_cases": cases_payload,
        "custom_manual_packs": custom_packs,
    }


@router.post("/restore", summary="Restore Backup Database Kasus & Paket Manual (Memerlukan PIN Admin)")
async def restore_workshop_backup(
    payload: BackupRestoreRequest,
    _pin_ok: str = Depends(require_workshop_pin),
    db: AsyncSession = Depends(get_db),
    current_user: User = Depends(get_current_active_user),
) -> dict[str, Any]:
    existing_codes = set((await db.execute(select(HistoricalCase.case_code))).scalars().all())
    added_cases = 0
    for item in payload.historical_cases:
        code = str(item.get("case_code") or "").strip()
        if not code or code in existing_codes:
            continue
        new_case = HistoricalCase(
            case_code=code,
            brand=str(item.get("brand") or ""),
            model=str(item.get("model") or ""),
            year=item.get("year"),
            engine_capacity=str(item.get("engine_capacity") or "-"),
            complaint=str(item.get("complaint") or ""),
            symptom=str(item.get("symptom") or ""),
            dtc=str(item.get("dtc") or "Tidak ada"),
            stft=item.get("stft"),
            ltft=item.get("ltft"),
            rpm=item.get("rpm"),
            o2_voltage=str(item.get("o2_voltage") or "-"),
            map_kpa=item.get("map_kpa"),
            maf_gps=item.get("maf_gps"),
            ect_c=item.get("ect_c"),
            inspection_findings=str(item.get("inspection_findings") or ""),
            final_diagnosis=str(item.get("final_diagnosis") or ""),
            repair_action=str(item.get("repair_action") or ""),
            system_category=str(item.get("system_category") or "Kelistrikan"),
            affected_system=str(item.get("affected_system") or "-"),
            group_category=str(item.get("group_category") or item.get("system_category") or "Kelistrikan"),
            manual_book_ref=str(item.get("manual_book_ref") or ""),
        )
        db.add(new_case)
        existing_codes.add(code)
        added_cases += 1

    if added_cases > 0:
        await db.commit()

    restored_packs = 0
    for pack in payload.custom_manual_packs:
        if isinstance(pack, dict) and pack.get("brand") and pack.get("model"):
            save_custom_manual_pack(dict(pack))
            restored_packs += 1

    return {
        "status": "success",
        "added_cases": added_cases,
        "restored_packs": restored_packs,
        "message": f"Restore selesai: {added_cases} kasus baru ditambahkan & {restored_packs} paket manual kustom dipulihkan.",
    }
