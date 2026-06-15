import logging

from app.schemas.task import TaskCreate, TaskResponse, TaskUpdate
from app.core.exceptions import TaskNotFoundError
from app.repositories.task_repository import TaskRepository

logger = logging.getLogger(__name__)


class TaskService:
    def __init__(self, repository: TaskRepository):
        self._repository = repository

    def get_all_tasks(self) -> list[TaskResponse]:
        return self._repository.get_all()
    
    def get_task(self, task_id: int) -> TaskResponse:
        task = self._repository.get_by_id(task_id)
        if task is None:
            logger.warning("Task not found: id=%s", task_id)
            raise TaskNotFoundError(task_id)
        return task
    
    def create_task(self, data: TaskCreate) -> TaskResponse:
        new_task = TaskResponse(
            id = self._repository.next_id(),
            title = data.title,
            description = data.description,
            is_completed = False
        )
        self._repository.add(new_task)
        logger.info("Task created: id=%s title=%r", new_task.id, new_task.title)
        return new_task
    
    def update_task(self, task_id: int, data: TaskUpdate) -> TaskResponse:
        task = self.get_task(task_id)
        updates = data.model_dump(exclude_unset=True)
        for field, value in updates.items():
            setattr(task, field, value)
        return task