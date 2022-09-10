from sqlalchemy.orm import Session
from models import company_group as model
from schemas import company_group as schemas

def get_company_group(db: Session, id: int):
    return db.query(model.CompanyGroup).filter(model.CompanyGroup.id == id).first()

def get_company_groups(db: Session, skip: int = 0, limit: int = 100):
    return db.query(model.CompanyGroup).offset(skip).limit(limit).all()

def create_company_group(db: Session, company_group: schemas.CompanyGroupCreate):
    db_cg = model.CompanyGroup(
        description=company_group.description
    )
    db.add(db_cg)
    db.commit()
    db.refresh(db_cg)
    return db_cg