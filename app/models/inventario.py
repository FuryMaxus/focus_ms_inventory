from advanced_alchemy.mixins.bigint import BigIntPrimaryKey
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import ForeignKey, Boolean

class UserInventory(BigIntPrimaryKey):
    __tablename__ = "user_inventory"

    user_id: Mapped[int] = mapped_column(nullable=False, index=True)
    item_id: Mapped[int] = mapped_column(ForeignKey("items.id"), nullable=False)
    is_equipped: Mapped[bool] = mapped_column(Boolean, default=False, nullable=False)