from fastapi import FastAPI, Depends, HTTPException, status, Request
from sqlalchemy.orm import Session
from typing import List, Optional
import logging

from . import models, auth
from .database import SessionLocal, engine
from .models import Employee, EmployeeEdit, EmployeeLoginUpdate, EmployeeContactUpdate, EmployeeTermsUpdate
from .logging_config import setup_logging

app = FastAPI()

models.Base.metadata.create_all(bind=engine)

setup_logging()

@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.get("/employees", response_model=List[models.Employee])
async def get_employees(
    name: Optional[str] = None,
    role: Optional[str] = None,
    status: Optional[str] = None,
    db: Session = Depends(SessionLocal),
    _: str = Depends(lambda: auth.role_required("read"))
):
    query = db.query(Employee)
    
    if name:
        query = query.filter(Employee.name == name)
    if role:
        query = query.filter(Employee.role == role)
    if status:
        query = query.filter(Employee.status == status)
    
    employees = query.all()
    logging.info(f"Retrieved {len(employees)} employees")
    return employees

@app.get("/employees/{employee_id}", response_model=models.Employee)
async def get_employee(employee_id: int, db: Session = Depends(SessionLocal)):
    employee = db.query(Employee).filter(Employee.id == employee_id).first()
    if not employee:
        logging.warning(f"Employee with id {employee_id} not found")
        raise HTTPException(status_code=404, detail="Employee not found")
    logging.info(f"Retrieved employee with id {employee_id}")
    return employee

@app.put("/employees/edit/{employee_id}", response_model=models.Employee)
async def edit_employee(
    employee_id: int,
    employee_data: models.EmployeeEdit,
    db: Session = Depends(SessionLocal),
    _: str = Depends(lambda: auth.role_required("write"))
):
    employee = db.query(Employee).filter(Employee.id == employee_id).first()
    if not employee:
        logging.warning(f"Employee with id {employee_id} not found")
        raise HTTPException(status_code=404, detail="Employee not found")
    
    for key, value in employee_data.dict(exclude_unset=True).items():
        setattr(employee, key, value)
    
    db.commit()
    db.refresh(employee)
    logging.info(f"Updated employee with id {employee_id}")
    return employee

@app.post("/token", response_model=auth.Token)
async def login_for_access_token(form_data: auth.OAuth2PasswordRequestForm = Depends()):
    user = auth.authenticate_user(form_data.username, form_data.password)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password",
            headers={"WWW-Authenticate": "Bearer"},
        )
    access_token = auth.create_access_token(data={"sub": user.username})
    return {"access_token": access_token, "token_type": "bearer"}