from advanced_alchemy.mixins.bigint import BigIntPrimaryKey
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import String

class Item(BigIntPrimaryKey):
    __tablename__ = "item"

    nombre: Mapped[str] = mapped_column(String(100))
    tipo: Mapped[str] = mapped_column(String(50))
    es_especial: Mapped[str] = mapped_column(String(1), default="N")