import pytest
from litestar import Litestar
from litestar.testing import TestClient
from advanced_alchemy.extensions.litestar import SQLAlchemyAsyncConfig, SQLAlchemyPlugin
from app.api.v1.item_controller import ItemController
from app.api.v1.inventory_controller import UserInventoryController

db_config = SQLAlchemyAsyncConfig(
    connection_string="sqlite+aiosqlite:///:memory:"
)

@pytest.fixture(scope="function")
def test_client():
    app = Litestar(
        route_handlers=[ItemController, UserInventoryController],
        plugins=[SQLAlchemyPlugin(db_config)],
        debug=True
    )
    with TestClient(app=app, raise_server_exceptions=True) as client:
        yield client