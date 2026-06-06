import pytest
import pytest_asyncio
from litestar.testing import AsyncTestClient
from advanced_alchemy.extensions.litestar import SQLAlchemyAsyncConfig, SQLAlchemyPlugin
from app.api.v1.inventory_controller import ItemController, UserInventoryController
from app.core.security import jwt_auth
from litestar import Litestar

from app.models.base import Base
from app.models.item import Item
from app.models.inventario import UserInventory

db_config = SQLAlchemyAsyncConfig(
    connection_string="sqlite+aiosqlite:///:memory:",
    create_all=True,
    metadata=Base.metadata,
)

test_app = Litestar(
    route_handlers=[ItemController, UserInventoryController],
    plugins=[SQLAlchemyPlugin(db_config)],
    on_app_init=[jwt_auth.on_app_init],
    debug=True,
)

@pytest_asyncio.fixture(scope="function")
async def client():
    async with AsyncTestClient(app=test_app) as c:
        yield c