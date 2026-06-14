import logging

from app.schemas.task import TaskCreate, TaskResponse, TaskUpdate
from app.core.exceptions import TaskNotFoundError

logger = logging.getLogger(__name__)


class TaskService:
    def __init__(self):
        self._tasks: list[TaskResponse] = []  
        self._next_id: int = 1

    def get_all_tasks(self) -> list[TaskResponse]:
        return self._tasks
    
    def get_task(self, task_id: int) -> TaskResponse:
        for task in self._tasks:
            if task.id == task_id:
                return task
        logger.warning("Task not found: id=%s", task_id)
        raise TaskNotFoundError(task_id)
    
    def create_task(self, data: TaskCreate) -> TaskResponse:
        new_task = TaskResponse(
            id = self._next_id,
            title = data.title,
            description = data.description,
            is_completed = False
        )
        self._tasks.append(new_task)
        self._next_id += 1
        logger.info("Task created: id=%s title=%r", new_task.id, new_task.title)
        return new_task
    
    def update_task(self, task_id: int, data: TaskUpdate) -> TaskResponse:
        task = self.get_task(task_id)

        updates = data.model_dump(exclude_unset=True)
        for field, value in updates.items():
            setattr(task, field, value)

        return task