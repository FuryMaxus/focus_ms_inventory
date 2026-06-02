from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import ForeignKey, Boolean
from app.models.base import Base

class UserInventory(Base):
    __tablename__ = "user_inventory"

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    user_id: Mapped[int] = mapped_column(nullable=False, index=True)
    item_id: Mapped[int] = mapped_column(ForeignKey("items.id"), nullable=False)
    is_equipped: Mapped[bool] = mapped_column(Boolean, default=False, nullable=False)