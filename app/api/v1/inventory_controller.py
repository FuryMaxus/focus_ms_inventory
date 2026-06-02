import random
from litestar import Controller, get, post, delete
from litestar.di import Provide
from app.services.item_service import ItemService, provide_item_service
from app.services.inventario_service import UserInventoryService, provide_inventory_service
from app.models.item import Item
from app.models.inventario import UserInventory
from app.models.schemas import ItemResponse

class ItemController(Controller):
    path = "/items"
    dependencies = {"service": Provide(provide_item_service)}

    @get()
    async def get_items(self, service: ItemService) -> list[Item]:
        return await service.list()

    @post()
    async def create_item(self, service: ItemService, data: Item) -> Item:
        return await service.create(data)

    @delete("/{item_id:int}")
    async def delete_item(self, service: ItemService, item_id: int) -> None:
        await service.delete(item_id)

    @get("/random")
    async def get_random_item(self, service: ItemService) -> ItemResponse:
        items = await service.list()
        item = random.choice(items)
        return ItemResponse(id=item.id, name=item.name, rarity=item.rarity, item_type=item.item_type)


class UserInventoryController(Controller):
    path = "/inventory"
    dependencies = {"service": Provide(provide_inventory_service)}

    @get("/{user_id:int}")
    async def get_inventory(self, service: UserInventoryService, user_id: int) -> list[UserInventory]:
        return await service.list(user_id=user_id)

    @post()
    async def add_item(self, service: UserInventoryService, data: UserInventory) -> UserInventory:
        return await service.create(data)

    @delete("/{inventory_id:int}")
    async def remove_item(self, service: UserInventoryService, inventory_id: int) -> None:
        await service.delete(inventory_id)