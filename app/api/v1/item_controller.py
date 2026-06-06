import random
from litestar import Controller, get, post, delete
from litestar.di import Provide
from app.services.item_service import ItemService, provide_item_service
from app.models.item import Item
from app.domain.structs import ItemResponse, ItemCreate
from collections.abc import Sequence


class ItemController(Controller):
    path = "/items"
    dependencies = {"service": Provide(provide_item_service)}

    @get()
    async def get_items(self, service: ItemService) -> Sequence[Item]:
        return await service.list()

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

    @delete("/{item_id:int}")
    async def delete_item(self, service: ItemService, item_id: int) -> None:
        await service.delete(item_id)

    @get("/random")
    async def get_random_item(self, service: ItemService) -> ItemResponse:
        items = await service.list()
        item = random.choice(items)
        return ItemResponse(id=item.id, name=item.name, rarity=item.rarity, item_type=item.item_type)
