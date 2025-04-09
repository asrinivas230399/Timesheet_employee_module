from pydantic import BaseModel

class EmployeeBase(BaseModel):
    name: str
    position: str
    salary: int

class EmployeeCreate(EmployeeBase):
    pass

class Employee(EmployeeBase):
    id: int

    class Config:
        orm_mode = True

class Token(BaseModel):
    access_token: str
    token_type: str
