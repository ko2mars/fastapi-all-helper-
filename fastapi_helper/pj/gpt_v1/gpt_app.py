from fastapi import FastAPI

from .router import router
from .settings import app_settings
from .lifespan import lifespan

def gpt_app() -> FastAPI:
    """
    Создает и настраивает экземпляр приложения FastAPI.

    Инициализирует приложение с глобальными настройками (заголовок, версия, 
    описание), подключает обработчик жизненного цикла (lifespan) 
    и регистрирует основные маршруты.
    
    Приложение легко мастабируемое и предлагает лишь некоторые функции 
    для работы с gpt вы можете легко подключить еще и свои эдпоинты если захотите 
    смотрите (Example)

    Returns:
        FastAPI: Сконфигурированный экземпляр приложения.
        
    Example:
       ```python 
       from fastapi_helper.pj import gpt_app
       from fastapi import APIRouter
       
       
       router = APIRouter()
       
       
       @router.get('/')
        async def index_app() -> dict[str, bool]:
            return {"ok": True}
            
            
        main_app = gpt_app()
        main_app.include_router(router=router)
       ```
    """
    app = FastAPI(
        title=app_settings.title,
        version=app_settings.version,
        description=app_settings.description,
        lifespan=lifespan
    )
    app.include_router(router)
    return app