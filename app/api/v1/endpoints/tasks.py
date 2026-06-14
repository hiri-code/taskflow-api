from fastapi import APIRouter, HTTPException, Depends
from app.services.task_service import TaskService
from typing import Annotated
from app.schemas.task import TaskCreate, TaskResponse, TaskUpdate
from app.core.exceptions import TaskNotFoundError
from app.api.deps import get_task_service

router = APIRouter()
TaskServiceDep = Annotated[TaskService, Depends(get_task_service)]

@router.get("", response_model=list[TaskResponse])
def get_tasks(service: TaskServiceDep):
    return service.get_all_tasks()

@router.post("", response_model=TaskResponse, status_code=201)
def create_task(data: TaskCreate, service: TaskServiceDep):
    return service.create_task(data)

@router.get("/{task_id}", response_model=TaskResponse)
def get_task(task_id: int, service: TaskServiceDep):
    try:
        return service.get_task(task_id)
    except TaskNotFoundError:
        raise HTTPException(status_code=404, detail=f"Task {task_id} not found")

@router.patch("/{task_id}", response_model=TaskResponse)
def update_task(task_id: int, data: TaskUpdate, service: TaskServiceDep):
    try:
        return service.update_task(task_id, data)
    except TaskNotFoundError:
        raise HTTPException(status_code=404, detail=f"Task {task_id} not found")