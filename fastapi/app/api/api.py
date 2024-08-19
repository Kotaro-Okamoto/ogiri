from fastapi import APIRouter

from api.endpoints import users, ogiri

api_router = APIRouter()
api_router.include_router(users.router, tags=["users"], prefix="/users") # tagsやprefixは設計に応じて付与
api_router.include_router(ogiri.router, tags=["ogiri"], prefix="/ogiri")