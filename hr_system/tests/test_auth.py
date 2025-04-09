import pytest
from httpx import AsyncClient
from app.main import app

@pytest.mark.asyncio
async def test_login_for_access_token():
    async with AsyncClient(app=app, base_url="http://test") as ac:
        response = await ac.post("/token", data={"username": "johndoe", "password": "secret"})
    assert response.status_code == 200
    assert "access_token" in response.json()

@pytest.mark.asyncio
async def test_access_protected_route():
    async with AsyncClient(app=app, base_url="http://test") as ac:
        # First, get the access token
        token_response = await ac.post("/token", data={"username": "johndoe", "password": "secret"})
        access_token = token_response.json()["access_token"]

        # Use the token to access a protected route
        headers = {"Authorization": f"Bearer {access_token}"}
        response = await ac.get("/employees/", headers=headers)
    assert response.status_code == 200