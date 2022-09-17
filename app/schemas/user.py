from datetime import datetime
from typing import Any, Union
from pydantic import BaseModel


class UserBase(BaseModel):
    email: str
    name: str
    surname: str
    description: str
    su: bool
    id_company_group: int
    id_owner_group: int
    
class UserCreate(CompanyBase):
    password: str
    pass

class User(CompanyBase):
    id: int
    hashed_password: str
    registered_at: Union[datetime, None] = None
    updated_at: Union[datetime, None] = None
    deleted_at: Union[datetime, None] = None
    
    class Config:
        orm_mode = True
