from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, DateTime, JSON
from sqlalchemy.orm import relationship

from ..database import Base


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    email = Column(String, unique=True, index=True)
    hashed_password = Column(String)
    name = Column(String, index=True)
    surname = Column(String, index=True)
    description = Column(String)
    role_list = Column(JSON)
    rule_list = Column(JSON)
    registered_at = Column(DateTime)
    updated_at = Column(DateTime)
    deleted_at = Column(DateTime)