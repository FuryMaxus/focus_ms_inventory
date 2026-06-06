from uuid import UUID
from litestar import Controller, get, post, delete
from litestar.di import Provide
from app.services.inventory_service import UserInventoryService, provide_inventory_service
from app.models.inventario import UserInventory
from app.domain.structs import UserInventoryResponse, InventoryAddPayload

class UserInventoryController(Controller):
    path = "/inventory"
    dependencies = {"service": Provide(provide_inventory_service)}

    @get("/{user_id:uuid}")
    async def get_inventory(self, service: UserInventoryService, user_id: UUID) -> list[UserInventoryResponse]:
        inventories = await service.list(user_id=user_id)
        return [
            UserInventoryResponse(
                id=inv.id, user_id=inv.user_id, item_id=inv.item_id, is_equipped=inv.is_equipped
            ) for inv in inventories
        ]
    
    @post()
    async def add_item(self, service: UserInventoryService, data: InventoryAddPayload) -> UserInventoryResponse:
        new_inv = await service.create(UserInventory(
            user_id=data.user_id,
            item_id=data.item_id,
            is_equipped=data.is_equipped
        ))
        return UserInventoryResponse(
            id=new_inv.id, user_id=new_inv.user_id, item_id=new_inv.item_id, is_equipped=new_inv.is_equipped
        )

    @delete("/{inventory_id:uuid}")
    async def remove_item(self, service: UserInventoryService, inventory_id: UUID) -> None:
        await service.delete(inventory_id)