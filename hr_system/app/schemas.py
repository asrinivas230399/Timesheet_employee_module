from pydantic import BaseModel

class Token(BaseModel):
    access_token: str
    token_type: str

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
