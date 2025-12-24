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
    def init(
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
        async with self.engine.begin() as conn:
            await conn.run_sync(ORMBase.metadata.create_all)


    async def dispose(self) -> None:
        await self.engine.dispose()


    async def session_getter(self) -> AsyncGenerator:
        async with self.session_factory() as session:
            yield session 
