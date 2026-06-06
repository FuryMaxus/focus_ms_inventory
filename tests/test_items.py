import pytest
from app.core.security import jwt_auth

TOKEN = jwt_auth.create_token(identifier="test_user")

@pytest.mark.asyncio
async def test_get_items(client):
    response = await client.get("/items", headers={"Authorization": f"Bearer {TOKEN}"})
    print(response.json())
    assert response.status_code == 200

@pytest.mark.asyncio
async def test_create_item(client):
    response = await client.post("/items", json={
        "name": "Espada",
        "description": "Una espada",
        "rarity": "common",
        "item_type": "weapon",
        "asset_url": "https://ejemplo.com/espada.png"
    }, headers={"Authorization": f"Bearer {TOKEN}"})
    print(response.json())
    assert response.status_code == 201