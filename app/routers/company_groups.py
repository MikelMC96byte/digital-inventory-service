from fastapi import APIRouter, Depends, HTTPException
from schemas import company_group as schemas
from dependencies import get_db
from controllers import company_group as controller
from sqlalchemy.orm import Session
from pydantic.typing import List

router = APIRouter(
    prefix="/company-groups",
    tags=["Company Groups"],
    responses={
        404: {"description": "Company group or groups not found"},
        403: {"description": "Operation not allowed"}
    }
)

@router.get("", response_model=List[schemas.CompanyGroup])
async def read_company_groups(db: Session = Depends(get_db), skip: int = 0, limit: int = 10):
    return controller.get_company_groups(db=db, skip=skip, limit=limit)

@router.get("/{id}", response_model=schemas.CompanyGroup)
async def read_company_group(id: int, db: Session = Depends(get_db)):
    return controller.get_company_group(db=db, id=id)

@router.post("", response_model=schemas.CompanyGroup)
async def create_company_group(company_group: schemas.CompanyGroupCreate, db: Session = Depends(get_db)):
    return controller.create_company_group(db=db, company_group=company_group)