import asyncio
from fastapi_helper.sql import DataBaseHelper



db_helper = DataBaseHelper(
    url="sqlite+aiosqlite:///test.db"
)


async def main() -> None:
    await db_helper.init_db()
    
    
if __name__ == "__main__":
    asyncio.run(main())