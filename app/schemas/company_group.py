from datetime import datetime
from typing import Union
from pydantic import BaseModel


class CompanyGroupBase(BaseModel):
    description: str
    
class CompanyGroupCreate(CompanyGroupBase):
    pass

class CompanyGroup(CompanyGroupBase):
    id: int
    registered_at: Union[datetime, None] = None
    updated_at: Union[datetime, None] = None
    deleted_at: Union[datetime, None] = None
    
    class Config:
        orm_mode = True
