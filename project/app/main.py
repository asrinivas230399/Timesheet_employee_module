from fastapi import FastAPI
from sqlalchemy import create_engine, event
from sqlalchemy.orm import sessionmaker
from .sync_service import SyncService
from .models import SomeModel  # Import your SQLAlchemy models here

app = FastAPI()

# Example database URL
DATABASE_URL = "sqlite:///./test.db"

# Optimize connection pooling
engine = create_engine(DATABASE_URL, pool_size=20, max_overflow=0)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Initialize SyncService
sync_service = SyncService(SessionLocal())

# Event listener for database changes
def after_insert_listener(mapper, connection, target):
    # Trigger synchronization after an insert operation
    sync_service.synchronize()

# Register the event listener
event.listen(SomeModel, 'after_insert', after_insert_listener)

# Define your models and other FastAPI routes here
