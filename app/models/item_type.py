from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, DateTime
from sqlalchemy.orm import relationship

from ..database import Base


class ItemTypes(Base):
    __tablename__ = "item_types"

    id = Column(Integer, primary_key=True, index=True)
    description = Column(String, index=True)
    id_subfamily = Column(Integer, ForeignKey("subfamilies.id"))
    id_family = Column(Integer, ForeignKey("families.id"))
    id_company = Column(Integer, ForeignKey("companies.id"))
    registered_at = Column(DateTime)
    updated_at = Column(DateTime)
    deleted_at = Column(DateTime)