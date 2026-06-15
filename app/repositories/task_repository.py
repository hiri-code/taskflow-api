from typing import Protocol

from app.schemas.task import TaskResponse


class TaskRepository(Protocol):
    def get_all(self) -> list[TaskResponse]: ...
    def get_by_id(self, task_id: int) -> TaskResponse | None: ...
    def add(self, task: TaskResponse) -> TaskResponse: ...
    def next_id(self) -> int: ...


class InMemoryTaskRepository:
    def __init__(self):
        self._tasks: list[TaskResponse] = []
        self._next_id: int = 1

    def get_all(self) -> list[TaskResponse]:
        return self._tasks
    
    def get_by_id(self, task_id: int) -> TaskResponse | None:
        for task in self._tasks:
            if task.id == task_id:
                return task
        return None
    
    def add(self, task: TaskResponse) -> TaskResponse:
        self._tasks.append(task)
        return task
    
    def next_id(self) -> int:
        current = self._next_id
        self._next_id += 1
        return current