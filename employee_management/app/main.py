from fastapi import FastAPI, Query, Request, Form, HTTPException
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from app.employee_data import fetch_employee_data, edit_employee_record
import uvicorn

app = FastAPI()
templates = Jinja2Templates(directory="app/templates")

@app.get("/employees", response_class=HTMLResponse)
async def get_employees(request: Request, name: str = Query(None), role: str = Query(None), status: str = Query(None)):
    employees = fetch_employee_data()
    if name:
        name = name.lower()
        employees = [emp for emp in employees if name in emp['name'].lower()]
    if role:
        role = role.lower()
        employees = [emp for emp in employees if role == emp['position'].lower()]
    if status:
        status = status.lower()
        employees = [emp for emp in employees if status == emp['status'].lower()]
    return templates.TemplateResponse("dashboard.html", {"request": request, "employees": employees})

@app.post("/edit_employee")
async def edit_employee(employee_id: int = Form(...), name: str = Form(None), position: str = Form(None), status: str = Form(None), projects: str = Form(None), workday_duration: int = Form(None), hourly_rate: float = Form(None)):
    if hourly_rate is not None and hourly_rate < 0:
        raise HTTPException(status_code=400, detail="Hourly rate cannot be negative.")
    if workday_duration is not None and (workday_duration < 0 or workday_duration > 24):
        raise HTTPException(status_code=400, detail="Workday duration must be between 0 and 24 hours.")
    
    projects_list = projects.split(',') if projects else None
    updated_employee = edit_employee_record(employee_id, name=name, position=position, status=status, projects=projects_list, workday_duration=workday_duration, hourly_rate=hourly_rate)
    if updated_employee:
        return {"message": "Employee record updated successfully!", "employee": updated_employee}
    raise HTTPException(status_code=404, detail="Employee not found!")

@app.get("/add_employee", response_class=HTMLResponse)
async def add_employee_form(request: Request):
    return templates.TemplateResponse("add_employee.html", {"request": request})

@app.post("/add_employee")
async def add_employee(name: str = Form(...), position: str = Form(...), status: str = Form(...), projects: str = Form(...), workday_duration: int = Form(...), hourly_rate: float = Form(...)):
    new_employee = {
        'id': len(fetch_employee_data()) + 1,
        'name': name,
        'position': position,
        'status': status,
        'projects': projects.split(','),
        'workday_duration': workday_duration,
        'hourly_rate': hourly_rate
    }
    print(f"New employee added: {new_employee}")
    return {"message": "New employee added successfully!", "employee": new_employee}

@app.get("/feedback", response_class=HTMLResponse)
async def feedback_form(request: Request):
    return templates.TemplateResponse("feedback.html", {"request": request})

@app.post("/feedback")
async def submit_feedback(name: str = Form(...), feedback: str = Form(...)):
    if not name.strip():
        raise HTTPException(status_code=400, detail="Name cannot be empty.")
    if not feedback.strip():
        raise HTTPException(status_code=400, detail="Feedback cannot be empty.")
    
    print(f"Feedback received from {name}: {feedback}")
    return {"message": "Thank you for your feedback!"}

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
