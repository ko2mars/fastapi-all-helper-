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
    Docstring для DataBaseHelper
    
    DataBaseHelper гланый класс библиотеки в этом классе уже реализованы такие методы 
    - Cоздание async engine 
    
    - Cоздание фабрики сессии
    
    - Метод(init_db) для иницилизации базы данных
    
    - Метод(dispose) для завершения открытых соеденений с базой данных 
      при завершении работы вашего приложения 
      
    - Метод(session_getter) который при запросе открывает соеденение с баззой данных
      временно отдает сессию  для работы, а при завершении работы
      атоматически закрывает соеденение 
      
    И да вам не придеться все это писать в ручную уже все сделанно за вас
    вам лишь нужно создать обьект класс DataBaseHelper и в поле url укажите ссылку 
    на вашу баззу данных
    
    
    
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
        Docstring для init_db
        
        :param self: Создаем иницилизацию баззы данных на основе 
        класса ORMBase 
        """
        async with self.engine.begin() as conn:
            await conn.run_sync(ORMBase.metadata.create_all)


    async def dispose(self) -> None:
        """
        Docstring для dispose
        
        :param self: Данный метод 
        """
        await self.engine.dispose()


    async def session_getter(self) -> AsyncGenerator:
        """
    Асинхронный генератор для получения сессии базы данных.
    
    Использует сессионную фабрику для создания контекста подключения.
    После завершения работы в вызывающем коде, сессия автоматически 
    закрывается
    
    Yields:
        AsyncSession: Объект сессии для выполнения SQL-запросов.
        """
        async with self.session_factory() as session:
            yield session 
