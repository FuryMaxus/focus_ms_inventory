from litestar import Litestar, Router
from litestar.plugins.sqlalchemy import SQLAlchemyAsyncConfig, SQLAlchemyPlugin
from app.api.v1.inventory_controller import UserInventoryController
from app.api.v1.item_controller import ItemController
from app.core.config import DATABASE_URL
from app.core.security import jwt_auth
from app.core.exceptions import GLOBAL_EXCEPTION_HANDLERS

db_config = SQLAlchemyAsyncConfig(
    connection_string=DATABASE_URL,
    create_all=True,
)

api_v1_router = Router(
    path="/api/v1",
    route_handlers=[
        ItemController,
        UserInventoryController
    ]
)

app = Litestar(
    route_handlers=[api_v1_router],
    plugins=[SQLAlchemyPlugin(db_config)],
    on_app_init=[jwt_auth.on_app_init],
    exception_handlers=GLOBAL_EXCEPTION_HANDLERS,
)