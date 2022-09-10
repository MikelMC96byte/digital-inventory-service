from .base import Base
from datetime import datetime

class WarehouseBase(Base):
    description: str
    
class WarehouseCreate(WarehouseBase):
    pass

class Warehouse(WarehouseBase):
    id: int

    class Config:
        orm_mode: True