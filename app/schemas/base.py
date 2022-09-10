from pydantic import BaseModel
from datetime import datetime

class Base(BaseModel):
    registered_at: datetime|None
    updated_at: datetime|None
    deleted_at: datetime|None