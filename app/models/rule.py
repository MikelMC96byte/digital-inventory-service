from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, DateTime, JSON
from sqlalchemy.orm import relationship

from ..database import Base


class Rule(Base):
    __tablename__ = "rules"

    id = Column(Integer, primary_key=True, index=True)
    description = Column(String, index=True)

    registered_at = Column(DateTime)
    updated_at = Column(DateTime)
    deleted_at = Column(DateTime)