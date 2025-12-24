# 🚀 FastAPI Helper

[![Python](https://img.shields.io/badge/Python-3.10%2B-blue.svg)](https://python.org)
[![FastAPI](https://img.shields.io/badge/FastAPI-0.127%2B-green.svg)](https://fastapi.tiangolo.com)
[![SQLAlchemy](https://img.shields.io/badge/SQLAlchemy-2.0%2B-orange.svg)](https://sqlalchemy.org)
[![License](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
[![PyPI](https://img.shields.io/badge/PyPI-fastapi--helper-blue.svg)](https://pypi.org/project/fastapi-helper)

# Установка 
```bash 
pip install fastapi-all-helper
```

# Быстрый старт 
```python 
import asyncio

from fastapi_helper.sql import DataBaseHelper


db_helper = DataBaseHelper(
    url="sqlite+aiosqlite:///test.db"
)
# Ссылку на базу данных лучше хранить в .env оружении 
# тут она показана в качестве демонстрации


async def main() -> None:
    await db_helper.init_db()
    
    
if __name__ == "__main__":
    asyncio.run(main())
```

# Использование с FastAPI
```python 
import asyncio
from fastapi import FastAPI
from sqlalchemy import select
from fastapi_helper.sql import SQL, DataBaseHelper
import uvicorn




app = FastAPI()
db = DataBaseHelper(url="sqlite+aiosqlite:///test2.db") 
# Ссылку на базу данных лучше хранить в .env оружении 
# тут она показана в качестве демонстрации


@app.get('/')
async def get_all_user():
    async with db.session_factory() as session:
        get_all = await session.execute(
            select(SQL.User)
        )
        return get_all.scalars().all()
    
    
async def main() -> None:
    await db.init_db()
    
    
if __name__ == "__main__":
    asyncio.run(main())
    uvicorn.run(app, port=8080)
```




