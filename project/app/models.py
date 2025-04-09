from sqlalchemy import Column, Integer, String, Float
from .database import Base
from pydantic import BaseModel, EmailStr, validator
from typing import Optional

class Employee(Base):
    __tablename__ = "employees"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    status = Column(String, index=True)
    role = Column(String, index=True)
    projects = Column(String)
    workday_duration = Column(Float)
    hourly_rate = Column(Float)
    username = Column(String, unique=True, index=True)
    password = Column(String)
    email = Column(String, unique=True, index=True)
    phone = Column(String)

class EmployeeEdit(BaseModel):
    name: Optional[str] = None
    status: Optional[str] = None
    role: Optional[str] = None
    projects: Optional[str] = None
    workday_duration: Optional[float] = None
    hourly_rate: Optional[float] = None

    @validator('workday_duration', 'hourly_rate')
    def validate_positive(cls, v):
        if v is not None and v <= 0:
            raise ValueError('Must be greater than zero')
        return v

class EmployeeLoginUpdate(BaseModel):
    username: str
    password: str

    @validator('username', 'password')
    def validate_non_empty(cls, v):
        if not v:
            raise ValueError('Must not be empty')
        return v

class EmployeeContactUpdate(BaseModel):
    email: EmailStr
    phone: str

    @validator('phone')
    def validate_phone(cls, v):
        if not v.isdigit() or len(v) < 10:
            raise ValueError('Invalid phone number')
        return v

class EmployeeTermsUpdate(BaseModel):
    workday_duration: float
    hourly_rate: float

    @validator('workday_duration', 'hourly_rate')
    def validate_positive(cls, v):
        if v <= 0:
            raise ValueError('Must be greater than zero')
        return v