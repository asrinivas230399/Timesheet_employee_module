from fastapi import FastAPI
from routers import employee

app = FastAPI()

# Include the employee router
app.include_router(employee.router)

@app.get("/")
async def root():
    return {"message": "Welcome to the Employee Management System"}