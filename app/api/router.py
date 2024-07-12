#To include as many as router you want

from fastapi import APIRouter
from app.api.endpoints import endpoints



router = APIRouter()
router.include_router(endpoints.router)
