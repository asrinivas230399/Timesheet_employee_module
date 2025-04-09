from sqlalchemy.orm import Session
from src.repositories.employee_repository import get_all_employees, create_employee

def add_employee(db: Session, employee_data: dict):
    return create_employee(db, employee_data)

def list_employees(db: Session):
    return get_all_employees(db)