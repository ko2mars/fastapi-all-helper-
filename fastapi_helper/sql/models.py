from datetime import datetime

from .base import ORMBase

from sqlalchemy.orm import (
    Mapped,
    mapped_column,
)
from sqlalchemy import (
    String,
    DateTime
)



class SQL:
    
    class User(ORMBase):
        username: Mapped[str] = mapped_column(String, index=True)
        hash_password: Mapped[str] = mapped_column(String, index=True)
        create_at: Mapped[datetime] = mapped_column(DateTime, default=datetime.utcnow(), index=True)
    
    class UserSession(ORMBase):
        token: Mapped[str] = mapped_column(String, unique=True, index=True)
        exripe_at: Mapped[datetime] = mapped_column(DateTime)
        create_at: Mapped[datetime] = mapped_column(DateTime, default=datetime.utcnow(), index=True)