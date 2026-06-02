from litestar import Controller, get, post, delete
from litestar.di import Provide
from app.services.item_service import ItemService, provide_item_service
from app.services.inventario_service import InventarioService, provide_inventario_service
from app.models.item import Item
from app.models.inventario import Inventario

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
    from app.models.schemas import ItemResponse

    @get("/random")
    async def get_random_item(self, service: ItemService) -> ItemResponse:
        items = await service.list()
        item = random.choice(items)
        return ItemResponse(id=item.id, nombre=item.nombre)


class InventarioController(Controller):
    path = "/inventario"
    dependencies = {"service": Provide(provide_inventario_service)}

    @get("/{personaje_id:int}")
    async def get_inventario(self, service: InventarioService, personaje_id: int) -> list[Inventario]:
        return await service.list(id_personaje=personaje_id)

    @post()
    async def add_item(self, service: InventarioService, data: Inventario) -> Inventario:
        return await service.create(data)

    @delete("/{inventario_id:int}")
    async def remove_item(self, service: InventarioService, inventario_id: int) -> None:
        await service.delete(inventario_id)