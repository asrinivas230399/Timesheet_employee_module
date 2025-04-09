import pytest
from httpx import AsyncClient
from app.main import app

@pytest.mark.asyncio
async def test_create_transaction():
    async with AsyncClient(app=app, base_url="http://test") as ac:
        response = await ac.post("/transactions/", json={"amount": 100.0, "currency": "USD", "timestamp": "2023-10-01T12:00:00", "description": "Test transaction"})
    assert response.status_code == 200
    assert response.json()["amount"] == 100.0

@pytest.mark.asyncio
async def test_read_transaction():
    async with AsyncClient(app=app, base_url="http://test") as ac:
        response = await ac.get("/transactions/1")
    assert response.status_code == 200
    assert response.json()["currency"] == "USD"
