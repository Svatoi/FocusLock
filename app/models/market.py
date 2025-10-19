from sqlalchemy import String, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship, backref

from .base import Base
from .utils import ModelMixin

class Market(Base, ModelMixin):
    __tablename__ = "markets"
    
    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    user_id: Mapped[int] = mapped_column(ForeignKey('users.id'), nullable=True)
    price: Mapped[int] = mapped_column(nullable=False)
    product_name: Mapped[str] = mapped_column(String(100), nullable=False)
    is_buy: Mapped[bool] = mapped_column(default=False)
    
    # user = relationship("User", back_populates="markets")
    