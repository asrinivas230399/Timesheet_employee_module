from sqlalchemy.orm import Session
from sqlalchemy.exc import StaleDataError
from fastapi import HTTPException
from . import models, schemas


def create_employee(db: Session, employee: schemas.EmployeeCreate):
    db_employee = models.Employee(**employee.dict())
    db.add(db_employee)
    db.commit()
    db.refresh(db_employee)
    return db_employee


def update_employee(db: Session, employee_id: int, employee_update: schemas.EmployeeCreate):
    db_employee = db.query(models.Employee).filter(models.Employee.id == employee_id).first()
    if db_employee is None:
        return None
    for key, value in employee_update.dict().items():
        setattr(db_employee, key, value)
    try:
        db.commit()
    except StaleDataError:
        db.rollback()
        raise HTTPException(status_code=409, detail="Conflict: Employee data has been modified by another transaction.")
    db.refresh(db_employee)
    return db_employee


def get_employee(db: Session, employee_id: int):
    return db.query(models.Employee).filter(models.Employee.id == employee_id).first()


def get_employees(db: Session, skip: int = 0, limit: int = 10):
    return db.query(models.Employee).offset(skip).limit(limit).all()


def get_employee_annual_cost(db: Session, employee_id: int):
    db_employee = get_employee(db, employee_id)
    if db_employee is None:
        raise HTTPException(status_code=404, detail="Employee not found")
    return db_employee.calculate_annual_cost()