"""
API routers package.
"""

from app.routers.auth import router as auth_router
from app.routers.vehicles import router as vehicles_router
from app.routers.diagnostics import router as diagnostics_router
from app.routers.manuals import router as manuals_router
from app.routers.work_orders import router as work_orders_router
from app.routers.inventory import router as inventory_router
from app.routers.transactions import router as transactions_router

__all__ = [
    "auth_router",
    "vehicles_router",
    "diagnostics_router",
    "manuals_router",
    "work_orders_router",
    "inventory_router",
    "transactions_router",
]
