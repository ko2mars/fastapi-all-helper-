# 🚀 FastAPI Helper

[![Python](https://img.shields.io/badge/Python-3.10%2B-blue.svg)](https://python.org)
[![FastAPI](https://img.shields.io/badge/FastAPI-0.127%2B-green.svg)](https://fastapi.tiangolo.com)
[![SQLAlchemy](https://img.shields.io/badge/SQLAlchemy-2.0%2B-orange.svg)](https://sqlalchemy.org)
[![License](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
[![PyPI](https://img.shields.io/badge/PyPI-fastapi--helper-blue.svg)](https://pypi.org/project/fastapi-helper)

#📥 Installation
```bash
pip install fastapi-helper
```

#✅ Quick Start
```python
import asyncio
from fastapi_helper.sql import DataBaseHelper

db_helper = DataBaseHelper("sqlite+aiosqlite:///test.db")
# Database URL is better stored in .env environment
# here it's shown for demonstration purposes

async def main() -> None:
    await db_helper.init_db()

if __name__ == "__main__":
    asyncio.run(main())
```

#📱 Usage with FastAPI
```python
import asyncio
from fastapi import FastAPI
from sqlalchemy import select
from fastapi_helper.sql import DataBaseHelper
from fastapi_helper.sql import SQL
import uvicorn

app = FastAPI()
db = DataBaseHelper("sqlite+aiosqlite:///test2.db")
# Database URL is better stored in .env environment
# here it's shown for demonstration purposes

@app.get('/')
async def get_all_user():
    async with db.session_factory() as session:
        get_all = await session.execute(
            select(SQL.User)
        )
        return get_all.scalars().all()

async def main():
    await db.init_db()

if __name__ == "__main__":
    asyncio.run(main())
    uvicorn.run(app, port=8080)
```


