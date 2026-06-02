from advanced_alchemy.service import SQLAlchemyAsyncRepositoryService
from sqlalchemy.ext.asyncio import AsyncSession
from app.repositories.inventario_repository import InventarioRepository

class InventarioService(SQLAlchemyAsyncRepositoryService):
    repository_type = InventarioRepository

async def provide_inventario_service(db_session: AsyncSession) -> InventarioService:
    return InventarioService(session=db_session)