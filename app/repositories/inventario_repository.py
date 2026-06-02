from advanced_alchemy.repository import SQLAlchemyAsyncRepository
from app.models.inventario import Inventario

class InventarioRepository(SQLAlchemyAsyncRepository):
    model_type = Inventario