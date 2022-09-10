from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, DateTime, JSON
from sqlalchemy.orm import relationship

from ..database import Base


class UserRule(Base):
    __tablename__ = "user_rules"

    id = Column(Integer, primary_key=True, index=True)
    id_user = Column(Integer, ForeignKey("users.id"))
    id_role = Column(Integer, ForeignKey("rules.id"))
    id_company = Column(Integer, ForeignKey("companies.id"))
    registered_at = Column(DateTime)
    updated_at = Column(DateTime)
    deleted_at = Column(DateTime)

    user = relationship("User", back_populates="user_roles")
    rule = relationship("Rule", back_populates="user_roles")
    company = relationship("Company", back_populates="user_roles")