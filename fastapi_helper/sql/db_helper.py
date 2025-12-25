from typing import (
    AsyncGenerator,
)


from sqlalchemy.ext.asyncio import (
    create_async_engine,
    async_sessionmaker,
    AsyncEngine,
    AsyncSession
)

from .base import ORMBase


class DataBaseHelper:
    """
    Docstring for DataBaseHelper
    
    DataBaseHelper is the main library class, and in this class such methods are implemented: 
    - Creating async engine 
    
    - Creating a session factory
    
    - Method(init_db) for database initialization
    
    - Method(dispose) for closing open connections with a database 
      when your app is shut down 
      
    - Method(session_getter) which opens connection with a database by request
      and temporarily gives a session for work, and with a shutdown
      closes connection automatically. 
      
    And you do not need to do this all manually - its already done for you!
    All you need is to create DataBaseHelper class object and in "url" put 
    a link to your database.
    
    
    
    """
    def __init__(
        self,
        url: str,
        echo: bool = False,
        echo_pool: bool = False
) -> None:
              
        self.engine: AsyncEngine = create_async_engine(
            url=url,
            echo=echo,
            echo_pool=echo_pool,

        )
        self.session_factory: async_sessionmaker[AsyncSession] = async_sessionmaker(
            bind=self.engine,
            autoflush=False,
            autocommit=False,
            expire_on_commit=False
        )


    async def init_db(self) -> None:
        """
        Docstring for init_db
        
        :param self: Creating an inititalization for
        an ORMBase class database.
        """
        async with self.engine.begin() as conn:
            await conn.run_sync(ORMBase.metadata.create_all)


    async def dispose(self) -> None:
        """
        Docstring for dispose
        
        :param self: This method
        """
        await self.engine.dispose()


    async def session_getter(self) -> AsyncGenerator:
        """
    Asynchronous generator for getting a database session.
    
    Uses session factory to create the connection context.
    After shuttdown in the code causing it session ends 
    automatically.
    
    Yields:
        AsyncSession: Session object to do SQL-requests.
        """
        async with self.session_factory() as session:
            yield session 
