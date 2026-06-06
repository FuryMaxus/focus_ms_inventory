from advanced_alchemy.service import SQLAlchemyAsyncRepositoryService
from sqlalchemy.ext.asyncio import AsyncSession
from app.repositories.item_repository import ItemRepository

class ItemService(SQLAlchemyAsyncRepositoryService):
    repository_type = ItemRepository

async def provide_item_service(db_session: AsyncSession) -> ItemService:
    return ItemService(session=db_session)