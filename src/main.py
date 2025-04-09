from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from models.user import User
from services.user_service import UserService
from database import init_db

app = FastAPI()

# Initialize the database
init_db()

# User service instance
user_service = UserService()

class UserCreateRequest(BaseModel):
    user_id: int
    name: str
    level: int

@app.post("/user")
async def create_user(user_request: UserCreateRequest):
    try:
        user = user_service.create_user(
            user_id=user_request.user_id,
            name=user_request.name,
            level=user_request.level
        )
        return {
            'user_id': user.user_id,
            'name': user.name,
            'level': user.level
        }
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))

# To run the server, use the command: uvicorn src.main:app --reload