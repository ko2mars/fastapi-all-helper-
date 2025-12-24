from sqlalchemy.orm import (
    DeclarativeBase,
    Mapped,
    mapped_column,
    declared_attr
)
from sqlalchemy import Integer


class ORMBase(DeclarativeBase):
    """
    The basic class for all ORM models.
    
    It is a declarative base from which all tables are inherited.
    The class itself is not initialized as a separate table in the SQL database,
    but serves as a template to define structure of the child models.
    """
    
    __abstract__ = True 
    
    @declared_attr.directive
    def __tablename__(cls) -> str:
        """
        Docstring for __tablename__
        
        :param cls: The class name will be an input for the parameter, 
        which is inherited from ORMBase and becomes an SQL table.
        :return: It will be returned as our class name (an SQL table) and with 
        the lower() method will be lowered down to a lower register and added an "s" letter. 
        So we had a class:
        ```python
        from fastapi_helper.sql import ORMBase
        
        async def init_db():
        async with ...:
            await conn.run_sync(ORMBase.metadata.create_all)
        ```
        and with an initialization of the database,
        it will create all the tables in the database, giving them their names
        and lowering them into a lower register and adding an "s" letter automatically.
        
        And on the output we will get 
        a table with a name "users"
        
        :rtype: str
        """
        return cls.__name__.lower() + "s"
    
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    
