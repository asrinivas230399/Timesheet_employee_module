import pytest
from httpx import AsyncClient
from app.main import app
from app.database import Base, engine, SessionLocal
from sqlalchemy.orm import sessionmaker

# Create a new session for testing
TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

@pytest.fixture(scope="module")
def test_db():
    # Create the database tables
    Base.metadata.create_all(bind=engine)
    db = TestingSessionLocal()
    try:
        yield db
    finally:
        db.close()
    # Drop the database tables
    Base.metadata.drop_all(bind=engine)

@pytest.mark.asyncio
async def test_create_employee(test_db):
    async with AsyncClient(app=app, base_url="http://test") as ac:
        response = await ac.post("/employees/", json={"name": "Alice", "position": "Developer", "salary": 70000})
    assert response.status_code == 200
    assert response.json()["name"] == "Alice"

@pytest.mark.asyncio
async def test_read_employee(test_db):
    async with AsyncClient(app=app, base_url="http://test") as ac:
        response = await ac.get("/employees/1")
    assert response.status_code == 200
    assert response.json()["name"] == "Alice"

@pytest.mark.asyncio
async def test_update_employee(test_db):
    async with AsyncClient(app=app, base_url="http://test") as ac:
        response = await ac.put("/employees/1", json={"name": "Alice", "position": "Senior Developer", "salary": 80000})
    assert response.status_code == 200
    assert response.json()["position"] == "Senior Developer"