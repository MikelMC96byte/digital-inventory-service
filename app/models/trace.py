from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, DateTime, JSON
from sqlalchemy.orm import relationship

from ..database import Base


class Trace(Base):
    __tablename__ = "traces"

    id = Column(Integer, primary_key=True, index=True)
    id_user = Column(Integer, ForeignKey("users.id"))
    action = Column(String)
    target = Column(String)
    data = Column(JSON)
    registered_at = Column(DateTime)

    user = relationship("User", back_populates="users")