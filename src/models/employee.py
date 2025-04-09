from pydantic import BaseModel
from typing import Optional

class EmployeeBase(BaseModel):
    first_name: str
    last_name: str
    email: str
    position: str

class EmployeeCreate(EmployeeBase):
    pass

class EmployeeInDB(EmployeeBase):
    id: int

    class Config:
        orm_mode = True