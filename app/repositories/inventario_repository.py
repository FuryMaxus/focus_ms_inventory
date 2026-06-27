from advanced_alchemy.repository import SQLAlchemyAsyncRepository
from app.models.user_inventory import UserInventoryModel

class UserInventoryRepository(SQLAlchemyAsyncRepository):
    model_type = UserInventoryModel