from fastapi import FastAPI
from fastapi.routing import APIRoute
from starlette.middleware.cors import CORSMiddleware

from app.routers import ping

def custom_generate_unique_id(route: APIRoute) -> str:
    return f"{route.tags[0]}-{route.name}"


app = FastAPI(generate_unique_id=custom_generate_unique_id)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],  # Allows frontend to connect
    allow_credentials=True,
    allow_methods=["*"],  # Allows all methods
    allow_headers=["*"],  # Allows all headers
)

app.include_router(ping.router)