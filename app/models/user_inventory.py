from uuid import UUID
from sqlalchemy import ForeignKey, Boolean
from sqlalchemy.orm import Mapped, mapped_column
from app.models.base import Base

class UserInventoryModel(Base):
    __tablename__ = "user_inventory"

    user_id: Mapped[UUID] = mapped_column(nullable=False, index=True)
    item_id: Mapped[UUID] = mapped_column(ForeignKey("items.id"), nullable=False)
    is_equipped: Mapped[bool] = mapped_column(Boolean, default=False, nullable=False)