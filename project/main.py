from fastapi import FastAPI, Query, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from employee_data import fetch_employee_data

app = FastAPI()
templates = Jinja2Templates(directory="templates")

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

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
