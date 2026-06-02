from litestar import Litestar
from litestar.plugins.sqlalchemy import SQLAlchemyAsyncConfig, SQLAlchemyPlugin
from app.api.v1.inventory_controller import ItemController, InventarioController
from app.core.config import DATABASE_URL

db_config = SQLAlchemyAsyncConfig(
    connection_string=DATABASE_URL,
    create_all=True,
)

app = Litestar(
    route_handlers=[ItemController, InventarioController],
    plugins=[SQLAlchemyPlugin(db_config)],
)