from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, DateTime
from sqlalchemy.orm import relationship

from ..database import Base


class Company(Base):
    __tablename__ = "companies"

    id = Column(Integer, primary_key=True, index=True)
    description = Column(String, index=True)
    id_company_group = Column(Integer, ForeignKey("company_groups.id"))
    id_owner_user = Column(String, ForeignKey("users.id"))
    registered_at = Column(DateTime)
    updated_at = Column(DateTime)
    deleted_at = Column(DateTime)

    owner_user = relationship("User", back_populates="companies")
    company_group = relationship("CompanyGroup", back_populates="company_groups")