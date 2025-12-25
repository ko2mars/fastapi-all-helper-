from pydantic import BaseModel





class SQUARESchema(BaseModel):
    """
    Схема данных возврата для эдпоинта /v1/.
    
    Attributes:
        ip: IP-адрес связанного узла или устройства.
    """
    ip: str 
    
    
class ChatSchema(BaseModel):
    """
    Схема сообщения чата.
    
    Attributes:
        type: Тип возращемоего значения только text.
        message: Ответ чата гпт  храниться в этом  сообщении.
    """
    type: str 
    messge: str 
    
class Schema400(BaseModel):
    """
    Схема ошибки валидации данных запроса.
    когда вы вызываете эдпоинт если данные которые вы ввели не валидные 
    и сервер не может их обработать вы получите messge об ошибке.
    
    Attributes:
        message: Детализированное сообщение о причине ошибки.
    """
    message: str 