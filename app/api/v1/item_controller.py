from uuid import UUID
from litestar import Controller, get, post, delete
from litestar.di import Provide
from app.services.item_service import ItemService, provide_item_service
from app.models.item import Item
from app.domain.structs import ItemResponse, ItemCreate
from litestar.exceptions import NotFoundException

class ItemController(Controller):
    path = "/items"
    dependencies = {"service": Provide(provide_item_service)}

    @get()
    async def get_items(self, service: ItemService) -> list[ItemResponse]:
        items = await service.list()
        
        return [
            ItemResponse(
                id=i.id,
                name=i.name,
                rarity=i.rarity,
                item_type=i.item_type,
                description=i.description,
                asset_url=i.asset_url
            ) for i in items
        ]

    @post()
    async def create_item(self, service: ItemService, data: ItemCreate) -> ItemResponse:
        item = await service.create(Item(
            name=data.name,
            description=data.description,
            rarity=data.rarity,
            item_type=data.item_type,
            asset_url=data.asset_url
        ))
        return ItemResponse(id=item.id, name=item.name, rarity=item.rarity, item_type=item.item_type)

    @delete("/{item_id:uuid}")
    async def delete_item(self, service: ItemService, item_id: UUID) -> None:
        await service.delete(item_id)

    @get("/random")
    async def fetch_random_item(self, service: ItemService) -> ItemResponse:
        item = await service.get_random_item()
        if not item:
            raise NotFoundException(detail="No hay ítems en la base de datos.")
        
        return ItemResponse(
            id=item.id, name=item.name, rarity=item.rarity, 
            item_type=item.item_type, description=item.description, asset_url=item.asset_url
        )