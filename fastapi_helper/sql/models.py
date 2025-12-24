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
    """
    Docstring for SQL
    
    Container for database table schemes storage.
    
    Inside this class ORM models are grouped (User, UserSession), 
    which allows to logically divide tables from the request logic.
    """
    
    class User(ORMBase):
        """
        Model for storage of users accounts.
        
        Contains information about users login (username), hashed password
        and registration date (create_at). Indexed fields allow to 
        do a qick search during an authorization.
        """
        username: Mapped[str] = mapped_column(String, index=True)
        hash_password: Mapped[str] = mapped_column(String, index=True)
        create_at: Mapped[datetime] = mapped_column(DateTime, default=datetime.utcnow(), index=True)
    
    class UserSession(ORMBase):
        """
        Model for controlling users active sessions.
        
        Used for storage of authorization tokens, time of their creation 
        and expiration date (expire_at), providing a safety mechanism 
        and access control.
        """
        
        
        token: Mapped[str] = mapped_column(String, unique=True, index=True)
        exripe_at: Mapped[datetime] = mapped_column(DateTime)
        create_at: Mapped[datetime] = mapped_column(DateTime, default=datetime.utcnow(), index=True)
