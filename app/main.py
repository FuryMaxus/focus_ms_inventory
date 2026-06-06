from litestar import Litestar
from litestar.plugins.sqlalchemy import SQLAlchemyAsyncConfig, SQLAlchemyPlugin
from app.api.v1.inventory_controller import ItemController, UserInventoryController
from app.core.config import DATABASE_URL
from app.core.security import jwt_auth

db_config = SQLAlchemyAsyncConfig(
    connection_string=DATABASE_URL,
    create_all=True,
)

app = Litestar(
    route_handlers=[ItemController, UserInventoryController],
    plugins=[SQLAlchemyPlugin(db_config)],
    on_app_init=[jwt_auth.on_app_init],
)