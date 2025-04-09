from fastapi import FastAPI, HTTPException, Depends
from sqlalchemy import event
import logging
from .sync_service import SyncService
from .models import SomeModel
from .db_connection import DBConnection
from .acl_service import ACLService

app = FastAPI()

# Example database URL
DATABASE_URL = "sqlite:///./test.db"

# Initialize DBConnection
db_connection = DBConnection(DATABASE_URL)

# Initialize SyncService
sync_service = SyncService(db_connection.get_session())

# Initialize ACLService
acl_service = ACLService("https://api.aclservice.com")

# Event listener for database changes
def after_insert_listener(mapper, connection, target):
    logging.info("Database insert detected, triggering synchronization.")
    sync_service.synchronize()

# Register the event listener
event.listen(SomeModel, 'after_insert', after_insert_listener)

# Configure logging
logging.basicConfig(level=logging.INFO, 
                    format='%(asctime)s - %(levelname)s - %(message)s',
                    handlers=[
                        logging.FileHandler("sync_service.log"),
                        logging.StreamHandler()
                    ])

async def get_current_user():
    # Placeholder for getting the current user
    return "user_id"

async def authorize_user(action: str, user_id: str = Depends(get_current_user)):
    is_authorized = await acl_service.is_user_authorized(user_id, action)
    if not is_authorized:
        logging.warning(f"Unauthorized access attempt by user {user_id} for action {action}.")
        raise HTTPException(status_code=403, detail="Not authorized to perform this action.")
    logging.info(f"User {user_id} authorized for action {action}.")

@app.get("/secure-data", dependencies=[Depends(authorize_user("view_secure_data"))])
async def get_secure_data():
    logging.info("Secure data accessed.")
    return {"data": "This is secure data."}

@app.post("/modify-data", dependencies=[Depends(authorize_user("modify_data"))])
async def modify_data():
    logging.info("Data modification requested.")
    return {"status": "Data modified successfully."}