from uuid import uuid4
from unittest.mock import patch, AsyncMock
from app.models.item import Item
from litestar.status_codes import HTTP_200_OK, HTTP_201_CREATED, HTTP_404_NOT_FOUND

BASE_PATH = "/items" 

@patch("app.services.item_service.ItemService.list", new_callable=AsyncMock)
def test_get_items(mock_list, test_client):
    item_id = uuid4()
    mock_list.return_value = [
        Item(id=item_id, name="Poción Mágica", rarity="Común", item_type="Consumible", description="", asset_url="")
    ]
    
    response = test_client.get(BASE_PATH)
    
    assert response.status_code == HTTP_200_OK
    data = response.json()
    assert len(data) == 1
    assert data[0]["id"] == str(item_id)
    assert data[0]["name"] == "Poción Mágica"

@patch("app.services.item_service.ItemService.create", new_callable=AsyncMock)
def test_create_item(mock_create, test_client):
    new_id = uuid4()
    mock_create.return_value = Item(
        id=new_id, 
        name="Espada", 
        rarity="Épica", 
        item_type="Arma", 
        description="Una gran espada", 
        asset_url="url"
    )
    
    payload = {
        "name": "Espada",
        "rarity": "Épica",
        "item_type": "Arma"
    }
    
    response = test_client.post(BASE_PATH, json=payload)
    
    assert response.status_code == HTTP_201_CREATED
    assert response.json()["id"] == str(new_id)

@patch("app.services.item_service.ItemService.get_random_item", new_callable=AsyncMock)
def test_fetch_random_item_success(mock_get_random, test_client):
    item_id = uuid4()
    mock_get_random.return_value = Item(id=item_id, name="Escudo", rarity="Rara", item_type="Defensa", description="", asset_url="")
    
    response = test_client.get(f"{BASE_PATH}/random")
    
    assert response.status_code == HTTP_200_OK
    assert response.json()["name"] == "Escudo"

@patch("app.services.item_service.ItemService.get_random_item", new_callable=AsyncMock)
def test_fetch_random_item_not_found(mock_get_random, test_client):
    mock_get_random.return_value = None
    
    response = test_client.get(f"{BASE_PATH}/random")
    
    assert response.status_code == HTTP_404_NOT_FOUND