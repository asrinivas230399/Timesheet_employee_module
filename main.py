from fastapi import FastAPI, Depends, HTTPException, status, Request
from fastapi.security import OAuth2PasswordBearer
from sqlalchemy.orm import Session
from jose import JWTError, jwt
from typing import List, Optional
import logging

from . import models
from .database import SessionLocal, engine
from .models import Employee

app = FastAPI()

models.Base.metadata.create_all(bind=engine)

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

credentials_exception = HTTPException(
    status_code=status.HTTP_401_UNAUTHORIZED,
    detail="Could not validate credentials",
    headers={"WWW-Authenticate": "Bearer"},
)

# Mock function to get user roles
# In a real application, this should query the database or another service
user_roles = {
    "admin": ["read", "write"],
    "user": ["read"]
}

def get_user_roles(username: str):
    return user_roles.get(username, [])

# Middleware to check if the user has the required role
async def role_required(role: str, token: str = Depends(oauth2_scheme)):
    try:
        payload = jwt.decode(token, "secret", algorithms=["HS256"])
        username: str = payload.get("sub")
        if username is None:
            raise credentials_exception
        roles = get_user_roles(username)
        if role not in roles:
            raise HTTPException(
                status_code=status.HTTP_403_FORBIDDEN,
                detail="Not enough permissions",
                headers={"WWW-Authenticate": "Bearer"},
            )
    except JWTError:
        raise credentials_exception

@app.middleware("http")
async def auth_middleware(request: Request, call_next):
    token = request.headers.get("Authorization")
    if token:
        try:
            payload = jwt.decode(token.split()[1], "secret", algorithms=["HS256"])
            request.state.user = payload.get("sub")
        except JWTError:
            raise credentials_exception
    else:
        raise credentials_exception
    response = await call_next(request)
    return response

@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.get("/employees", response_model=List[models.Employee])
async def get_employees(
    name: Optional[str] = None,
    role: Optional[str] = None,
    status: Optional[str] = None,
    db: Session = Depends(SessionLocal),
    _: str = Depends(lambda: role_required("read"))
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
    _: str = Depends(lambda: role_required("write"))
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

@app.put("/employees/update-login/{employee_id}", response_model=models.Employee)
async def update_employee_login(
    employee_id: int,
    login_data: models.EmployeeLoginUpdate,
    db: Session = Depends(SessionLocal),
    _: str = Depends(lambda: role_required("write"))
):
    employee = db.query(Employee).filter(Employee.id == employee_id).first()
    if not employee:
        logging.warning(f"Employee with id {employee_id} not found")
        raise HTTPException(status_code=404, detail="Employee not found")
    
    employee.username = login_data.username
    employee.password = login_data.password  # In a real application, ensure to hash the password
    
    db.commit()
    db.refresh(employee)
    logging.info(f"Updated login for employee with id {employee_id}")
    return employee

@app.put("/employees/update-contact/{employee_id}", response_model=models.Employee)
async def update_employee_contact(
    employee_id: int,
    contact_data: models.EmployeeContactUpdate,
    db: Session = Depends(SessionLocal),
    _: str = Depends(lambda: role_required("write"))
):
    employee = db.query(Employee).filter(Employee.id == employee_id).first()
    if not employee:
        logging.warning(f"Employee with id {employee_id} not found")
        raise HTTPException(status_code=404, detail="Employee not found")
    
    employee.email = contact_data.email
    employee.phone = contact_data.phone
    
    db.commit()
    db.refresh(employee)
    logging.info(f"Updated contact for employee with id {employee_id}")
    return employee

@app.put("/employees/update-terms/{employee_id}", response_model=models.Employee)
async def update_employee_terms(
    employee_id: int,
    terms_data: models.EmployeeTermsUpdate,
    db: Session = Depends(SessionLocal),
    _: str = Depends(lambda: role_required("write"))
):
    employee = db.query(Employee).filter(Employee.id == employee_id).first()
    if not employee:
        logging.warning(f"Employee with id {employee_id} not found")
        raise HTTPException(status_code=404, detail="Employee not found")
    
    employee.workday_duration = terms_data.workday_duration
    employee.hourly_rate = terms_data.hourly_rate
    
    db.commit()
    db.refresh(employee)
    logging.info(f"Updated terms for employee with id {employee_id}")
    return employee

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
