

from litestar import Controller, get, post, delete
from litestar.di import Provide
from app.services.inventario_service import UserInventoryService, provide_inventory_service
from app.models.inventario import UserInventory
from collections.abc import Sequence


class UserInventoryController(Controller):
    path = "/inventory"
    dependencies = {"service": Provide(provide_inventory_service)}

    @get("/{user_id:int}")
    async def get_inventory(self, service: UserInventoryService, user_id: int) -> Sequence[UserInventory]:
        return await service.list(user_id=user_id)

    @post()
    async def add_item(self, service: UserInventoryService, data: UserInventory) -> UserInventory:
        return await service.create(data)

    @delete("/{inventory_id:int}")
    async def remove_item(self, service: UserInventoryService, inventory_id: int) -> None:
        await service.delete(inventory_id)