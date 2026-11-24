"""
Konfigurasi Environment Proyek — app/core/config.py
"""

import os
from pathlib import Path
import shutil


def _resolve_database_url() -> str:
    """Menentukan URL database yang aman untuk mode lokal maupun serverless read-only (Vercel)."""
    raw = os.getenv("DATABASE_URL", "").strip()
    if raw:
        if raw.startswith("postgres://"):
            return raw.replace("postgres://", "postgresql+asyncpg://", 1)
        if raw.startswith("postgresql://") and "+asyncpg" not in raw:
            return raw.replace("postgresql://", "postgresql+asyncpg://", 1)
        return raw

    bundled_db = Path(__file__).resolve().parent.parent.parent / "bengkel_masa_depan.db"
    is_serverless = bool(
        os.getenv("VERCEL")
        or os.getenv("VERCEL_ENV")
        or os.getenv("AWS_LAMBDA_FUNCTION_NAME")
    )
    dir_writable = os.access(bundled_db.parent, os.W_OK)

    if is_serverless or not dir_writable:
        tmp_db = Path("/tmp/bengkel_masa_depan.db")
        if not tmp_db.exists() and bundled_db.exists():
            try:
                shutil.copy2(bundled_db, tmp_db)
            except Exception:
                pass
        return f"sqlite+aiosqlite:///{tmp_db.as_posix()}"

    return f"sqlite+aiosqlite:///{bundled_db.as_posix()}"


class Settings:
    PROJECT_NAME: str = os.getenv("PROJECT_NAME", "AGOS SMART DIAGNOSTIK by Agos Corporation")
    VERSION: str = "1.1.0"
    API_V1_STR: str = "/api/v1"

    DATABASE_URL: str = _resolve_database_url()
    JWT_SECRET_KEY: str = os.getenv(
        "JWT_SECRET_KEY", "bengkel-masa-depan-super-secret-jwt-key-2026"
    )
    JWT_ALGORITHM: str = "HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES: int = int(
        os.getenv("ACCESS_TOKEN_EXPIRE_MINUTES", str(60 * 24))
    )
    VITARA_MANUAL_DIR: str = os.getenv(
        "VITARA_MANUAL_DIR", "./manual repair suzuki vitara"
    )
    DEV_ALLOW_ANONYMOUS_FALLBACK: bool = (
        os.getenv("DEV_ALLOW_ANONYMOUS_FALLBACK", "true").lower() == "true"
    )


settings = Settings()
