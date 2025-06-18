import pytest
from httpx import AsyncClient
from main import app

@pytest.mark.asyncio
async def test_homepage():
    async with AsyncClient(app=app, base_url="http://test") as client:
        response = await client.get("/")
        assert response.status_code == 200
        assert "Robot Controller" in response.text

@pytest.mark.asyncio
async def test_move_forward():
    async with AsyncClient(app=app, base_url="http://test") as client:
        response = await client.post("/move", data={"direction": "forward"})
        assert response.status_code == 200
        assert "Simulated move" in response.text or "Published" in response.text
