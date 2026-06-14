from app.services.task_service import TaskService
from app.services.user_service import UserService

_task_service = TaskService()
_user_service = UserService()

def get_task_service() -> TaskService:
    return _task_service

def get_user_service() -> UserService:
    return _user_service