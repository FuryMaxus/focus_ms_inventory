from advanced_alchemy.service import SQLAlchemyAsyncRepositoryService
from sqlalchemy.ext.asyncio import AsyncSession
from app.repositories.inventario_repository import UserInventoryRepository

class UserInventoryService(SQLAlchemyAsyncRepositoryService):
    repository_type = UserInventoryRepository

async def provide_inventory_service(db_session: AsyncSession) -> UserInventoryService:
    return UserInventoryService(session=db_session)