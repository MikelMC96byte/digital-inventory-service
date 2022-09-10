from datetime import datetime
from typing import Any, Union
from pydantic import BaseModel


class CompanyBase(BaseModel):
    description: str
    id_company_group: int
    id_owner_group: int
    
class CompanyCreate(CompanyBase):
    pass

class Company(CompanyBase):
    id: int
    registered_at: Union[datetime, None] = None
    updated_at: Union[datetime, None] = None
    deleted_at: Union[datetime, None] = None
    
    class Config:
        orm_mode = True
