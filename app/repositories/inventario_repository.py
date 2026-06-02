from advanced_alchemy.repository import SQLAlchemyAsyncRepository
from app.models.inventario import UserInventory

class UserInventoryRepository(SQLAlchemyAsyncRepository):
    model_type = UserInventory