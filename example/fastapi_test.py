import asyncio
from fastapi import FastAPI
from sqlalchemy import select
from fastapi_helper.sql import SQL, DataBaseHelper
import uvicorn




app = FastAPI()
db = DataBaseHelper(url="sqlite+aiosqlite:///test2.db")


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
    