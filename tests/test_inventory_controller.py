from uuid import uuid4
from unittest.mock import patch, AsyncMock
from app.models.inventario import UserInventory
from litestar.status_codes import HTTP_200_OK, HTTP_201_CREATED, HTTP_204_NO_CONTENT

BASE_PATH = "/inventory"

@patch("app.services.inventory_service.UserInventoryService.list", new_callable=AsyncMock)
def test_get_user_inventory(mock_list, test_client):
    user_id = uuid4()
    item_id = uuid4()
    inv_id = uuid4()
    
    mock_list.return_value = [
        UserInventory(id=inv_id, user_id=user_id, item_id=item_id, is_equipped=True)
    ]
    
    response = test_client.get(f"{BASE_PATH}/{user_id}")
    
    assert response.status_code == HTTP_200_OK
    assert response.json()[0]["is_equipped"] is True
    assert response.json()[0]["item_id"] == str(item_id)

@patch("app.services.inventory_service.UserInventoryService.create", new_callable=AsyncMock)
def test_add_item_to_inventory(mock_create, test_client):
    user_id = uuid4()
    item_id = uuid4()
    inv_id = uuid4()
    
    mock_create.return_value = UserInventory(id=inv_id, user_id=user_id, item_id=item_id, is_equipped=False)
    
    payload = {
        "user_id": str(user_id),
        "item_id": str(item_id),
        "is_equipped": False
    }
    
    response = test_client.post(BASE_PATH, json=payload)
    
    assert response.status_code == HTTP_201_CREATED
    assert response.json()["id"] == str(inv_id)

@patch("app.services.inventory_service.UserInventoryService.delete", new_callable=AsyncMock)
def test_remove_item_from_inventory(mock_delete, test_client):
    inv_id = uuid4()
    mock_delete.return_value = None 
    
    response = test_client.delete(f"{BASE_PATH}/{inv_id}")
    
    assert response.status_code == HTTP_204_NO_CONTENT
    mock_delete.assert_called_once_with(inv_id)