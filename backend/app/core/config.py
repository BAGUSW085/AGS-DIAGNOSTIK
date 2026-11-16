"""
Konfigurasi Environment Proyek — app/core/config.py
"""

import os


class Settings:
    PROJECT_NAME: str = os.getenv("PROJECT_NAME", "AGOS SMART DIAGNOSTIK by Agos Corporation")
    VERSION: str = "1.1.0"
    API_V1_STR: str = "/api/v1"

    _raw_db_url: str = os.getenv(
        "DATABASE_URL", "sqlite+aiosqlite:///./bengkel_masa_depan.db"
    )
    if _raw_db_url.startswith("postgres://"):
        DATABASE_URL: str = _raw_db_url.replace("postgres://", "postgresql+asyncpg://", 1)
    elif _raw_db_url.startswith("postgresql://") and "+asyncpg" not in _raw_db_url:
        DATABASE_URL = _raw_db_url.replace("postgresql://", "postgresql+asyncpg://", 1)
    else:
        DATABASE_URL = _raw_db_url
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
