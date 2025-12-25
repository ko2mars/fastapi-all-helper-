from enum import Enum

from ...config import settings

class Models(str, Enum):
    """
    Docstring для Models
    
    Данный класс используется для перечесления 
    моделей исскуственного иннтелекта 
    
    Используется в эдпоинте /v1/create/chat, 
    чтобы вы не вводили модели лично,для вашего же бдительстава
    используется данный класс 
    
    """
    MODEL_GPT_4 =  settings.gpt_4
    
    
class AppColor(str, Enum):
    """
    Docstring для AppColor
    
    Данный класс используется для перечесления 
    цветовой палитры, используется для логгирования 
    
    """
    RED = "\033[31m"
    GREEN = "\033[32m"
    YELLOW = "\033[33m"
    BLUE = "\033[34m"
    MAGENTA = "\033[35m"
    CYAN = "\033[36m"
    RESET = "\033[0m"
    BOLD = "\033[1m"