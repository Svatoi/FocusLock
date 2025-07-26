from typing import Optional
from sqlalchemy import Text, String
from sqlalchemy.orm import Mapped, mapped_column

from .base import Base

class User(Base):
    __tablename__ = "users"
    
    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    username: Mapped[str] = mapped_column(String(100), nullable=False, unique=True)
    score: Mapped[int] = mapped_column(default=0)
    block_list_site: Mapped[Optional[str]] = mapped_column(Text)
    