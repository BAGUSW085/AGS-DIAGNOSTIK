"""
General helper functions — number generation, date formatting, etc.
"""

from datetime import datetime, timezone

from sqlalchemy import func, select
from sqlalchemy.ext.asyncio import AsyncSession


async def generate_order_number(db: AsyncSession, prefix: str, table_cls) -> str:
    """
    Generate an auto-incrementing order number for today.
    Format: {PREFIX}-YYYYMMDD-XXX  (e.g., WO-20261031-001)
    """
    today_str = datetime.now(timezone.utc).strftime("%Y%m%d")
    pattern = f"{prefix}-{today_str}-%"

    # Count existing records with today's prefix
    stmt = select(func.count()).where(
        table_cls.order_number.like(pattern)
        if hasattr(table_cls, "order_number")
        else table_cls.invoice_number.like(pattern)
    )
    result = await db.execute(stmt)
    count = result.scalar() or 0

    sequence = str(count + 1).zfill(3)
    return f"{prefix}-{today_str}-{sequence}"


def format_rupiah(amount: float) -> str:
    """Format a number as Indonesian Rupiah (Rp 1.250.000)."""
    if amount < 0:
        return f"-Rp {abs(amount):,.0f}".replace(",", ".")
    return f"Rp {amount:,.0f}".replace(",", ".")

