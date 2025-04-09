from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
from pydantic import BaseModel, Field
from typing import Optional
from ..database import get_db
from ..models import Employee
from ..dependencies import get_current_user, RoleChecker

router = APIRouter(
    prefix="/employees",
    tags=["employees"],
)

class EmployeeCreate(BaseModel):
    name: str = Field(..., example="John Doe")
    age: int = Field(..., gt=0, example=30)
    position: str = Field(..., example="Software Engineer")

class EmployeeUpdate(BaseModel):
    name: Optional[str] = Field(None, example="John Doe")
    age: Optional[int] = Field(None, gt=0, example=30)
    position: Optional[str] = Field(None, example="Software Engineer")

# Define role checkers
admin_role = RoleChecker("admin")
user_role = RoleChecker("user")

@router.post("/", response_model=Employee, dependencies=[Depends(admin_role)])
def create_employee(employee: EmployeeCreate, db: Session = Depends(get_db)):
    db_employee = Employee(**employee.dict())
    db.add(db_employee)
    db.commit()
    db.refresh(db_employee)
    return db_employee

@router.get("/{employee_id}", response_model=Employee, dependencies=[Depends(user_role)])
def read_employee(employee_id: int, db: Session = Depends(get_db)):
    db_employee = db.query(Employee).filter(Employee.id == employee_id).first()
    if db_employee is None:
        raise HTTPException(status_code=404, detail="Employee not found")
    return db_employee

@router.put("/{employee_id}", response_model=Employee, dependencies=[Depends(admin_role)])
def update_employee(employee_id: int, employee: EmployeeUpdate, db: Session = Depends(get_db)):
    db_employee = db.query(Employee).filter(Employee.id == employee_id).first()
    if db_employee is None:
        raise HTTPException(status_code=404, detail="Employee not found")
    for key, value in employee.dict().items():
        if value is not None:
            setattr(db_employee, key, value)
    db.commit()
    db.refresh(db_employee)
    return db_employee

@router.delete("/{employee_id}", response_model=dict, dependencies=[Depends(admin_role)])
def delete_employee(employee_id: int, db: Session = Depends(get_db)):
    db_employee = db.query(Employee).filter(Employee.id == employee_id).first()
    if db_employee is None:
        raise HTTPException(status_code=404, detail="Employee not found")
    db.delete(db_employee)
    db.commit()
    return {"ok": True}