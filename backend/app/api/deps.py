"""
Database Session Generator & Otorisasi Role-Based — app/api/deps.py
"""

from __future__ import annotations

from typing import AsyncGenerator, Optional

from fastapi import Depends, HTTPException, status
from fastapi.security import HTTPAuthorizationCredentials, HTTPBearer
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession, async_sessionmaker, create_async_engine

from app.core.config import settings
from app.core.security import decode_access_token
from app.models import User

engine = create_async_engine(settings.DATABASE_URL, echo=False)
AsyncSessionLocal = async_sessionmaker(
    engine, expire_on_commit=False, class_=AsyncSession
)

bearer_scheme = HTTPBearer(auto_error=False)


async def get_db() -> AsyncGenerator[AsyncSession, None]:
    async with AsyncSessionLocal() as session:
        yield session


async def get_current_active_user(
    credentials: Optional[HTTPAuthorizationCredentials] = Depends(bearer_scheme),
    db: AsyncSession = Depends(get_db),
) -> User:
    if credentials and credentials.credentials:
        payload = decode_access_token(credentials.credentials)
        username = payload.get("sub")
        stmt = select(User).where(User.username == username, User.is_active.is_(True))
        user = (await db.execute(stmt)).scalar_one_or_none()
        if user is None:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Pengguna tidak ditemukan atau tidak aktif.",
            )
        return user

    if settings.DEV_ALLOW_ANONYMOUS_FALLBACK:
        fallback_stmt = (
            select(User).where(User.is_active.is_(True)).order_by(User.id.asc()).limit(1)
        )
        fallback_user = (await db.execute(fallback_stmt)).scalar_one_or_none()
        if fallback_user is not None:
            return fallback_user
        return User(
            id=1,
            username="admin_dev",
            full_name="Administrator Bengkel (Dev Fallback)",
            password_hash="",
            role="admin",
            is_active=True,
        )

    raise HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Header Authorization Bearer token diperlukan.",
    )
