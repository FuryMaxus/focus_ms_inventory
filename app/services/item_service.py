from advanced_alchemy.service import SQLAlchemyAsyncRepositoryService
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
from sqlalchemy.sql.functions import random
from app.repositories.item_repository import ItemRepository
from app.models.item import Item

class ItemService(SQLAlchemyAsyncRepositoryService[Item]):
    repository_type = ItemRepository

    async def get_random_item(self) -> Item | None:
        statement = select(Item).order_by(random()).limit(1)
        result = await self.repository.session.execute(statement)
        return result.scalar_one_or_none()

async def provide_item_service(db_session: AsyncSession) -> ItemService:
    return ItemService(session=db_session)