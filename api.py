from fastapi import APIRouter

from routes import user

api_router = APIRouter()
api_router.include_router(user.user_router)