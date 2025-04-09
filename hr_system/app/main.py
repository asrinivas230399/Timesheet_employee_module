from fastapi import FastAPI, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session
from . import crud, models, schemas, websocket, auth
from .database import SessionLocal, engine
from datetime import timedelta

models.Base.metadata.create_all(bind=engine)

app = FastAPI(title="HR System API", description="This is a simple HR system API built with FastAPI.", version="1.0.0")

# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.post("/token", response_model=schemas.Token)
async def login_for_access_token(form_data: OAuth2PasswordRequestForm = Depends()):
    user = auth.authenticate_user(auth.fake_users_db, form_data.username, form_data.password)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password",
            headers={"WWW-Authenticate": "Bearer"},
        )
    access_token_expires = timedelta(minutes=auth.ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = auth.create_access_token(
        data={"sub": user["username"]}, expires_delta=access_token_expires
    )
    return {"access_token": access_token, "token_type": "bearer"}

@app.post("/employees/", response_model=schemas.Employee, summary="Create a new employee", description="Create a new employee with the given name, position, and salary.")
def create_employee(employee: schemas.EmployeeCreate, db: Session = Depends(get_db), current_user: dict = Depends(auth.get_current_active_user)):
    db_employee = crud.create_employee(db=db, employee=employee)
    websocket.manager.broadcast(f"New employee created: {db_employee.name}")
    return db_employee

@app.get("/employees/{employee_id}", response_model=schemas.Employee, summary="Get an employee by ID", description="Retrieve an employee's details by their ID.")
def read_employee(employee_id: int, db: Session = Depends(get_db), current_user: dict = Depends(auth.get_current_active_user)):
    db_employee = crud.get_employee(db, employee_id=employee_id)
    if db_employee is None:
        raise HTTPException(status_code=404, detail="Employee not found")
    return db_employee

@app.get("/employees/", response_model=list[schemas.Employee], summary="List employees", description="Retrieve a list of employees with pagination support.")
def read_employees(skip: int = 0, limit: int = 10, db: Session = Depends(get_db), current_user: dict = Depends(auth.get_current_active_user)):
    employees = crud.get_employees(db, skip=skip, limit=limit)
    return employees

@app.websocket("/ws/employees")
async def websocket_endpoint(websocket: WebSocket):
    await websocket.manager.connect(websocket)
    try:
        while True:
            data = await websocket.receive_text()
            await websocket.send_text(f"Message text was: {data}")
    except WebSocketDisconnect:
        websocket.manager.disconnect(websocket)
