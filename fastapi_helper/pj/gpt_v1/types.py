from g4f.client import AsyncClient
from fastapi import Request, status 
from fastapi.responses import JSONResponse


from .enums import Models

client = AsyncClient()



async def create_chat(request:Request, model: Models, prompt: str) -> JSONResponse:
    """
    Отправляет пользовательский запрос к указанной модели ИИ и возвращает ответ,
    включая IP-адрес пользователя.

    Проверяет наличие IP-адреса пользвателя в запросе. Если IP не найден,
    возвращает ошибку 400. В противном случае формирует запрос к API модели
    и , отправляет его.Возвращает ответ от модели.

    Args:
        request: Объект запроса FastAPI, используемый для получения IP-адреса пользователя.
        model: Перечисление Models, указывающее, какую модель ИИ использовать.
        prompt: Строка с пользовательским запросом для модели ИИ.

    Returns:
        JSONResponse:
            - 200 OK: JSON, содержащий тип ответа ("gpt-response"),
            - 400 Bad Request: JSON с сообщением об ошибке, если не удалось
              получить IP-адрес пользователя.
    """
    if not request.client or request.client.host is None:
        return JSONResponse(
            status_code=status.HTTP_400_BAD_REQUEST,
            content={
                "message": "Не удалось извлечь ваш ip адрес"
            }
        )
    response = await client.chat.completions.create(
        model=model.value,
        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ]
        
    )
    return JSONResponse(
        status_code=status.HTTP_200_OK,
        content={
            "type": "gpt-response",
            "message": response.choices[0].message.content 
        }
    )



async def square_types(request: Request) -> JSONResponse:
    """
    Определяет IP-адрес пользователя для идентификации в системe.

    Метод извлекает адрес хоста из входящего запроса. Если IP не определен
    возвращает ошибку 400.
    Используется как первичная проверка доступа перед работой с типами.

    Args:
        request: Объект HTTP-запроса от пользователя.

    Returns:
        JSONResponse: 
            - 200 OK: Содержит IP-адрес пользователя.
            - 400 Bad Request: Сообщение о невозможности получить IP.
    """
    if not request.client or request.client.host is None:
        return JSONResponse(
            status_code=status.HTTP_400_BAD_REQUEST,
            content={
                "message": "Не удолось получить ваш IP address"
            }
        )
    return JSONResponse(
        status_code=status.HTTP_200_OK,
        content={
            "ip": request.client.host
        }
    )
