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
    Docstring для SQL
    
    Контейнер для хранения схем таблиц базы данных.
    
    Внутри этого класса сгруппированы модели ORM (User, UserSession), 
    что позволяет логически отделить структуру таблиц от логики запросов.
    """
    
    class User(ORMBase):
        """
        Модель для хранения учетных данных пользователей.
        
        Содержит информацию о логине (username), хешированном пароле 
        и дате регистрации (create_at). Индексированные поля позволяют 
        быстро выполнять поиск при авторизации.
        """
        username: Mapped[str] = mapped_column(String, index=True)
        hash_password: Mapped[str] = mapped_column(String, index=True)
        create_at: Mapped[datetime] = mapped_column(DateTime, default=datetime.utcnow(), index=True)
    
    class UserSession(ORMBase):
        """
        Модель для управления активными сессиями пользователей.
        
        Используется для хранения токенов авторизации, времени их создания 
        и срока истечения (expire_at), обеспечивая механизм безопасности 
        и контроля доступа.
        """
        
        
        token: Mapped[str] = mapped_column(String, unique=True, index=True)
        exripe_at: Mapped[datetime] = mapped_column(DateTime)
        create_at: Mapped[datetime] = mapped_column(DateTime, default=datetime.utcnow(), index=True)