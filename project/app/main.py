from fastapi import FastAPI, Query, Request, Form
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from employee_data import fetch_employee_data
import uvicorn

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

@app.get("/feedback", response_class=HTMLResponse)
async def feedback_form(request: Request):
    return templates.TemplateResponse("feedback.html", {"request": request})

@app.post("/feedback")
async def submit_feedback(name: str = Form(...), feedback: str = Form(...)):
    # Handle the feedback, e.g., save it to a database or send it via email
    print(f"Feedback received from {name}: {feedback}")
    return {"message": "Thank you for your feedback!"}

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
