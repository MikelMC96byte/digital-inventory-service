from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, DateTime
from sqlalchemy.orm import relationship

from ..database import Base


class Subfamilies(Base):
    __tablename__ = "subfamilies"

    id = Column(Integer, primary_key=True, index=True)
    description = Column(String, index=True)
    id_family = Column(Integer, ForeignKey("families.id"))
    registered_at = Column(DateTime)
    updated_at = Column(DateTime)
    deleted_at = Column(DateTime)

    family = relationship("Family", back_populates="subfamilies")