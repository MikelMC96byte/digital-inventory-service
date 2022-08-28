from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, DateTime, JSON
from sqlalchemy.orm import relationship

from ..database import Base


class Role(Base):
    __tablename__ = "roles"

    id = Column(Integer, primary_key=True, index=True)
    description = Column(String, index=True)
    rule_list = Column(JSON)
    registered_at = Column(DateTime)
    updated_at = Column(DateTime)
    deleted_at = Column(DateTime)