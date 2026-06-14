from fastapi import APIRouter
from app.api.deps import SettingsDep

router = APIRouter()

@router.get("")
def check_health(config: SettingsDep):
    return {
        "status": "ok", 
        "version": config.VERSION_PROJECT,
        "environment": config.ENVIRONMENT,
        "debug": config.DEBUG
    }