from pydantic import BaseModel, Field
from typing import Optional

class EmployeeCreate(BaseModel):
    name: str = Field(..., example="John Doe")
    age: int = Field(..., gt=0, example=30)
    position: str = Field(..., example="Software Engineer")

class EmployeeUpdate(BaseModel):
    name: Optional[str] = Field(None, example="John Doe")
    age: Optional[int] = Field(None, gt=0, example=30)
    position: Optional[str] = Field(None, example="Software Engineer")

class EmployeeResponse(BaseModel):
    id: int
    name: str
    age: int
    position: str

    class Config:
        orm_mode = True