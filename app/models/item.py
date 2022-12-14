from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, DateTime
from sqlalchemy.orm import relationship

from ..database import Base


class Item(Base):
    __tablename__ = "items"

    id = Column(Integer, primary_key=True, index=True)
    id_item_type = Column(Integer, ForeignKey("item_types.id"))
    id_warehouse = Column(Integer, ForeignKey("warehouses.id"))
    registered_at = Column(DateTime)
    updated_at = Column(DateTime)
    deleted_at = Column(DateTime)

    item_type = relationship("ItemType", back_populates="items")
    warehouse = relationship("Warehouse", back_populates="items")