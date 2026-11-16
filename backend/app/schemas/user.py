"""
Pydantic schemas for User model.
"""

from datetime import datetime

from pydantic import BaseModel, ConfigDict, Field


class UserBase(BaseModel):
    """Shared user fields."""
    username: str = Field(..., min_length=3, max_length=50)
    full_name: str = Field(..., min_length=1, max_length=100)
    role: str = Field(
        default="mekanik",
        pattern="^(admin|mekanik|kasir|service_advisor)$",
        description="User role: admin, mekanik, kasir, service_advisor",
    )
    is_active: bool = True


class UserCreate(UserBase):
    """Schema for creating a new user — requires a plaintext password."""
    password: str = Field(..., min_length=6, max_length=128)


class UserUpdate(BaseModel):
    """Schema for updating user fields — all optional."""
    username: str | None = Field(default=None, min_length=3, max_length=50)
    full_name: str | None = Field(default=None, min_length=1, max_length=100)
    role: str | None = Field(
        default=None,
        pattern="^(admin|mekanik|kasir|service_advisor)$",
    )
    is_active: bool | None = None
    password: str | None = Field(default=None, min_length=6, max_length=128)


class UserResponse(UserBase):
    """Schema returned to the client — excludes hashed_password."""
    id: int
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)
