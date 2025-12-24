from sqlalchemy.orm import (
    DeclarativeBase,
    Mapped,
    mapped_column,
    declared_attr
)
from sqlalchemy import Integer


class ORMBase(DeclarativeBase):
    """
    Базовый класс для всех моделей ORM.
    
    Является декларативным основанием, от которого наследуются все таблицы.
    Сам класс не инициализируется как отдельная таблица в базе данных SQL,
    а служит шаблоном для определения структуры дочерних моделей.
    """
    
    __abstract__ = True 
    
    @declared_attr.directive
    def __tablename__(cls) -> str:
        """
        Docstring для __tablename__
        
        :param cls: В параметр будет входить название класса 
        который наследуется от ORMBase и становиться таблицей SQL
        :return: Возращаться будет имя нашего класса(Таблицы SQL) с помощью метода 
        lower() будет опускаться в нижний регистр и добавляться буква s 
        таким образом у нас был класс 
        ```python
        from fastapi_helper.sql import ORMBase
        
        async def init_db():
        async with ...:
            await conn.run_sync(ORMBase.metadata.create_all)
        ```
        Таким образом при иницилизации базы данных 
        он будет создавать все таблицы в базе данных взяв их имена 
        опустит их в нижний регистр и автоматически добавит окончание  s
        
        а на вызоде мы получим 
        таблицу с именем users
        
        :rtype: str
        """
        return cls.__name__.lower() + "s"
    
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    