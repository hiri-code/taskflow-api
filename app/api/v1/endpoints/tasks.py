from fastapi import APIRouter

router = APIRouter()

@router.get("")
def get_tasks():
    return []

@router.post("")
def create_task():
    return {"msg": "create task stub"}

@router.get("/{task_id}")
def get_task(task_id: int):
    return {"msg": "get task stub", "task_id": task_id}