from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column
from app.models.base import Base

class ItemModel(Base):
    __tablename__ = "items"

    name: Mapped[str] = mapped_column(String(100), nullable=False)
    description: Mapped[str] = mapped_column(String(255), nullable=True)
    rarity: Mapped[str] = mapped_column(String(50), nullable=False) 
    item_type: Mapped[str] = mapped_column(String(50), nullable=False) 
    asset_url: Mapped[str] = mapped_column(String(255), nullable=True)