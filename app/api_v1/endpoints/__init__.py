from fastapi import APIRouter
from .youtube import router as youtube_router

router = APIRouter()

__all__ = ["router"]

router.include_router(youtube_router)
