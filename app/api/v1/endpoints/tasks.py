from fastapi import APIRouter, HTTPException
from app.services.task_service import TaskService
from app.schemas.task import TaskCreate, TaskResponse, TaskUpdate
from app.core.exceptions import TaskNotFoundError

router = APIRouter()
task_service = TaskService()

@router.get("", response_model=list[TaskResponse])
def get_tasks():
    return task_service.get_all_tasks()

@router.post("", response_model=TaskResponse, status_code=201)
def create_task(data: TaskCreate):
    return task_service.create_task(data)

@router.get("/{task_id}", response_model=TaskResponse)
def get_task(task_id: int):
    try:
        return task_service.get_task(task_id)
    except TaskNotFoundError:
        raise HTTPException(status_code=404, detail=f"Task {task_id} not found")

@router.patch("/{task_id}", response_model=TaskResponse)
def update_task(task_id: int, data: TaskUpdate):
    try:
        return task_service.update_task(task_id, data)
    except TaskNotFoundError:
        raise HTTPException(status_code=404, detail=f"Task {task_id} not found")