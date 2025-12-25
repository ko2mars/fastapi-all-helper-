from fastapi_helper.pj import gpt_app
from fastapi import APIRouter


router = APIRouter()

@router.get('/')
async def index_app() -> dict[str, bool]:
    return {"ok": True}


app = gpt_app()
app.include_router(router=router)