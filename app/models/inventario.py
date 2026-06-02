from advanced_alchemy.mixins.bigint import BigIntPrimaryKey
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import ForeignKey, TIMESTAMP
from datetime import datetime

class Inventario(BigIntPrimaryKey):
    __tablename__ = "inventario"

    id_personaje: Mapped[int] = mapped_column(ForeignKey("personaje.id_personaje"))
    id_item: Mapped[int] = mapped_column(ForeignKey("item.id_item"))
    obtenido_en: Mapped[datetime] = mapped_column(TIMESTAMP, default=datetime.utcnow)