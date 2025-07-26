from typing import Optional
from sqlalchemy import Text, String, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column

from .base import Base

class Market(Base):
    __tablename__ = "markets"
    
    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    user_id: Mapped[int] = mapped_column(ForeignKey('users.id'), nullable=True)
    price: Mapped[int] = mapped_column(nullable=False)
    product_name: Mapped[str] = mapped_column(String(100), nullable=False)
    is_buy: Mapped[bool] = mapped_column(default=False)
    