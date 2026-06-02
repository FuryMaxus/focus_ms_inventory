import msgspec

class ItemResponse(msgspec.Struct):
    id: int
    name: str
    rarity: str
    item_type: str