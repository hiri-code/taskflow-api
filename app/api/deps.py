from app.services.task_service import TaskService
from app.services.user_service import UserService
from app.core.config import Settings, get_settings
from fastapi import Depends
from typing import Annotated

_task_service = TaskService()
_user_service = UserService()
SettingsDep = Annotated[Settings, Depends(get_settings)]

def get_task_service() -> TaskService:
    return _task_service

def get_user_service() -> UserService:
    return _user_service