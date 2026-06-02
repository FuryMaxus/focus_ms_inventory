import msgspec

class ItemResponse(msgspec.Struct):
    id: int
    nombre: str