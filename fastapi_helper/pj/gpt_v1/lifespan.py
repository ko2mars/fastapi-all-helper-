from contextlib import asynccontextmanager
from typing import AsyncGenerator


from fastapi import FastAPI

from .settings import lifespan_helper


@asynccontextmanager
async def lifespan(app: FastAPI) -> AsyncGenerator[None, None]:
    """
    Управляет жизненным циклом приложения.

    Выполняет инициализацию ресурсов (подключение к БД, и тд)
    перед запуском сервера и обеспечивает корректное завершение работы
    при его остановке.

    Args:
        app: Экземпляр приложения FastAPI.

    Yields:
        None: Передает управление приложению после завершения инициализации.
    """
    await lifespan_helper.start_app()
    yield
    await lifespan_helper.close_app()