from typing import Optional
from sqlalchemy import Text, String
from sqlalchemy.orm import Mapped, mapped_column, relationship

from .base import Base
from .utils import ModelMixin

class User(Base, ModelMixin):
    __tablename__ = "users"
    
    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    username: Mapped[str] = mapped_column(String(100), nullable=False, unique=True)
    score: Mapped[int] = mapped_column(default=0)
    block_list: Mapped[Optional[str]] = mapped_column(Text)
    
    tasks: Mapped[list["Task"]] = relationship("Task", back_populates="user", cascade="all, delete-orphan")
    