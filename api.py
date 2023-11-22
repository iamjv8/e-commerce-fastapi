from fastapi import APIRouter

from users import routes

api_router = APIRouter()
api_router.include_router(routes.user_router)