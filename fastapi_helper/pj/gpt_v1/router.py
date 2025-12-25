from fastapi import APIRouter, Request
from .types import (
    square_types,
    create_chat
)
from .enums import Models
from .schema import (
    SQUARESchema,
    Schema400,
    ChatSchema,
)


router = APIRouter(
    tags=["🌐CHAT GPT"],
    prefix="/v1",
    
)

@router.get('/', responses={
    200: {
        "model": SQUARESchema,
        "description": "Success Response"
    },
    400: {
        "model": Schema400,
        "description": "IP address problem"
    }
})
async def square_api(request: Request):
    """
    Получение сетевой идентификации.

    Эндпоинт проверяет соединение и возвращает публичный IP-адрес клиента, 
    который используется системой для проверки прав доступа.

    Responses:
        200: Успешный возврат IP-адреса.
        400: Проблема с определением адреса хоста.
    """
    return await square_types(
        request=request
    )
    
@router.post('/create/chat', responses={
    200: {
        "model": ChatSchema,
        "description": "Success Response"
    },
    400: {
        "model": Schema400,
        "description": "IP address problem"
    }
})
async def create_chat_api(request: Request, model:Models, prompt: str):
    """
    Генерация запроса и получение ответа через ии.

    Принимает текстовый запрос и отправляет его в выбранную 
    модель ИИ. Помимо ответа нейросети, фиксирует IP-адрес пользоваптеля
    для проверки валидности, такая проверка была введнена чтобы люди не могли 
    через программы отправлять и парсить страницу

    Args:
        model: Выбранная версия модели.
        prompt: Текст вопроса или инструкции для ИИ.

    Responses:
        200: Сгенерированный ответ от GPT.
        400: Ошибка доступа (не определен IP).
    """
    return await create_chat(
        request=request,
        model=model,
        prompt=prompt
    )
