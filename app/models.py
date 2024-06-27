from typing import List

from db import Base
import sqlalchemy as sa
from sqlalchemy.orm import Mapped, mapped_column, relationship


class Pizza(Base):
    __tablename__ = "pizzas"

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    name: Mapped[str] = mapped_column(sa.String(50))
    description: Mapped[str] = mapped_column(sa.String(100))
    prize: Mapped[int] = mapped_column(default=79)






    def __str__(self):
        return f"<Pizzs title:{self.name}>"


