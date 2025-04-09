from fastapi import APIRouter
from services.employee_service import add_employee

router = APIRouter(
    prefix="/employees",
    tags=["employees"]
)

@router.get("/")
async def get_employees():
    return {"message": "List of employees"}

@router.post("/")
async def create_employee(employee_data: dict):
    return add_employee(employee_data)