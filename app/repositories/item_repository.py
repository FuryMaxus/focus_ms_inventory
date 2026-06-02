from advanced_alchemy.repository import SQLAlchemyAsyncRepository
from app.models.item import Item

class ItemRepository(SQLAlchemyAsyncRepository):
    model_type = Item