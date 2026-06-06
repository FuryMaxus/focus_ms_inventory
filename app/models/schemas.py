import msgspec
from typing import Optional

class ItemResponse(msgspec.Struct):
    id: int
    name: str
    rarity: str
    item_type: str

class ItemCreate(msgspec.Struct):
    name: str
    rarity: str
    item_type: str
    description: Optional[str] = None
    asset_url: Optional[str] = None