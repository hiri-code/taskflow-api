from fastapi import APIRouter
from app.core.config import settings

router = APIRouter()

@router.get("")
def check_health():
    return {"status": "ok", "version": settings.VERSION_PROJECT}