from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, DateTime
from sqlalchemy.orm import relationship

from ..database import Base


class CompanyGroup(Base):
    __tablename__ = "company_groups"

    id = Column(Integer, primary_key=True, index=True)
    description = Column(String, index=True)
    id_master_user = Column(String, ForeignKey("users.id"))
    registered_at = Column(DateTime)
    updated_at = Column(DateTime)
    deleted_at = Column(DateTime)