import pytest
from unittest.mock import AsyncMock, MagicMock
from uuid import uuid4
from app.services.item_service import ItemService
from app.models.item import Item

@pytest.mark.asyncio
async def test_get_random_item_service():
    mock_session = AsyncMock()
    mock_result = MagicMock()
    
    # Configuramos la respuesta esperada
    expected_item = Item(id=uuid4(), name="Amuleto de Concentración")
    mock_result.scalar_one_or_none.return_value = expected_item
    mock_session.execute.return_value = mock_result
    
    service = ItemService(session=mock_session)
    result = await service.get_random_item()
    
    assert result is not None
    assert result.name == "Amuleto de Concentración"
    mock_session.execute.assert_called_once()