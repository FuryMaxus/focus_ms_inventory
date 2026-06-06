import msgspec
from uuid import UUID
from typing import Optional


class ItemResponse(msgspec.Struct):
    id: UUID
    name: str
    rarity: str
    item_type: str
    description: Optional[str] = None
    asset_url: Optional[str] = None

class ItemCreate(msgspec.Struct):
    name: str
    rarity: str
    item_type: str
    description: Optional[str] = None
    asset_url: Optional[str] = None


class UserInventoryResponse(msgspec.Struct):
    id: UUID
    user_id: UUID
    item_id: UUID
    is_equipped: bool

class InventoryAddPayload(msgspec.Struct):
    user_id: UUID
    item_id: UUID
    is_equipped: bool = False