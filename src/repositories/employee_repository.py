from sqlalchemy.orm import Session
from models import Employee

def get_all_employees(db: Session):
    return db.query(Employee).all()

def create_employee(db: Session, employee_data: dict):
    new_employee = Employee(**employee_data)
    db.add(new_employee)
    db.commit()
    db.refresh(new_employee)
    return new_employee