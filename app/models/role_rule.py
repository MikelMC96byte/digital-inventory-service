from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, DateTime, JSON
from sqlalchemy.orm import relationship

from ..database import Base


class UserRole(Base):
    __tablename__ = "role_rules"

    id = Column(Integer, primary_key=True, index=True)
    id_role = Column(Integer, ForeignKey("roles.id"))
    id_rule = Column(Integer, ForeignKey("rules.id"))
    registered_at = Column(DateTime)
    updated_at = Column(DateTime)
    deleted_at = Column(DateTime)

    role = relationship("Role", back_populates="role_rules")
    rule = relationship("Rule", back_populates="role_rules")