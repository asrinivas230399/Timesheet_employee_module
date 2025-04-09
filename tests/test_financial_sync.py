import pytest
from httpx import AsyncClient
from app.main import app

@pytest.mark.asyncio
async def test_financial_data_sync():
    async with AsyncClient(app=app, base_url="http://test") as ac:
        # Simulate creating a transaction
        response = await ac.post("/transactions/", json={"amount": 150.0, "currency": "EUR", "timestamp": "2023-10-01T12:00:00", "description": "Sync test transaction"})
        assert response.status_code == 200
        transaction_id = response.json()["id"]

        # Verify the transaction exists
        response = await ac.get(f"/transactions/{transaction_id}")
        assert response.status_code == 200
        assert response.json()["amount"] == 150.0

@pytest.mark.asyncio
async def test_financial_data_security():
    async with AsyncClient(app=app, base_url="http://test") as ac:
        # Attempt to access transactions without a token
        response = await ac.get("/transactions/")
        assert response.status_code == 401

        # Get the access token
        token_response = await ac.post("/token", data={"username": "johndoe", "password": "secret"})
        access_token = token_response.json()["access_token"]

        # Use the token to access transactions
        headers = {"Authorization": f"Bearer {access_token}"}
        response = await ac.get("/transactions/", headers=headers)
        assert response.status_code == 200