"""
Pydantic schemas package.
"""

from app.schemas.user import UserBase, UserCreate, UserUpdate, UserResponse
from app.schemas.vehicle import (
    CustomerBase, CustomerCreate, CustomerUpdate, CustomerResponse,
    VehicleBase, VehicleCreate, VehicleUpdate, VehicleResponse,
)
from app.schemas.diagnostic import (
    FaultCategoryBase, FaultCategoryCreate, FaultCategoryResponse,
    FaultHistoryBase, FaultHistoryCreate, FaultHistoryUpdate, FaultHistoryResponse,
    FaultCheckpointBase, FaultCheckpointCreate, FaultCheckpointResponse,
    SymptomCheckpointLinkBase, SymptomCheckpointLinkCreate, SymptomCheckpointLinkResponse,
)
from app.schemas.manual import (
    RepairManualBase, RepairManualCreate, RepairManualUpdate, RepairManualResponse,
    WiringDiagramBase, WiringDiagramCreate, WiringDiagramResponse,
    DTCCodeBase, DTCCodeCreate, DTCCodeResponse,
    SensorSpecBase, SensorSpecCreate, SensorSpecResponse,
)
from app.schemas.workshop import (
    WorkOrderBase, WorkOrderCreate, WorkOrderUpdate, WorkOrderResponse,
    WorkOrderItemBase, WorkOrderItemCreate, WorkOrderItemResponse,
)
from app.schemas.inventory import (
    SparepartBase, SparepartCreate, SparepartUpdate, SparepartResponse,
    StockMovementBase, StockMovementCreate, StockMovementResponse,
)
from app.schemas.transaction import (
    TransactionBase, TransactionCreate, TransactionResponse,
    TransactionItemBase, TransactionItemCreate, TransactionItemResponse,
)

__all__ = [
    "UserBase", "UserCreate", "UserUpdate", "UserResponse",
    "CustomerBase", "CustomerCreate", "CustomerUpdate", "CustomerResponse",
    "VehicleBase", "VehicleCreate", "VehicleUpdate", "VehicleResponse",
    "FaultCategoryBase", "FaultCategoryCreate", "FaultCategoryResponse",
    "FaultHistoryBase", "FaultHistoryCreate", "FaultHistoryUpdate", "FaultHistoryResponse",
    "FaultCheckpointBase", "FaultCheckpointCreate", "FaultCheckpointResponse",
    "SymptomCheckpointLinkBase", "SymptomCheckpointLinkCreate", "SymptomCheckpointLinkResponse",
    "RepairManualBase", "RepairManualCreate", "RepairManualUpdate", "RepairManualResponse",
    "WiringDiagramBase", "WiringDiagramCreate", "WiringDiagramResponse",
    "DTCCodeBase", "DTCCodeCreate", "DTCCodeResponse",
    "SensorSpecBase", "SensorSpecCreate", "SensorSpecResponse",
    "WorkOrderBase", "WorkOrderCreate", "WorkOrderUpdate", "WorkOrderResponse",
    "WorkOrderItemBase", "WorkOrderItemCreate", "WorkOrderItemResponse",
    "SparepartBase", "SparepartCreate", "SparepartUpdate", "SparepartResponse",
    "StockMovementBase", "StockMovementCreate", "StockMovementResponse",
    "TransactionBase", "TransactionCreate", "TransactionResponse",
    "TransactionItemBase", "TransactionItemCreate", "TransactionItemResponse",
]
