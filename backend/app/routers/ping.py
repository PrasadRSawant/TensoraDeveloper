from fastapi import APIRouter

ping_router = APIRouter()


@ping_router.get("/ping", tags=["Ping"])
async def pong():
    return {"ping": "pong!"}