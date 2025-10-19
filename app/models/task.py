from datetime import datetime
from typing import Optional
from datetime import datetime
from sqlalchemy import Text, TIMESTAMP, String, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship, backref

from .base import Base
from .utils import ModelMixin

class Task(Base, ModelMixin):
    __tablename__ = "tasks"
    
    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    user_id: Mapped[int] = mapped_column(ForeignKey('users.id'), nullable=True)
    score: Mapped[int] = mapped_column(nullable=False)
    name: Mapped[str] = mapped_column(String(100), nullable=False)
    description: Mapped[Optional[str]] = mapped_column(Text)
    is_done: Mapped[Optional[bool]] = mapped_column(default=False)
    created_at: Mapped[datetime] = mapped_column(TIMESTAMP, default=datetime.now)
    
    user: Mapped["User"] = relationship("User", back_populates="tasks")