from fastapi import APIRouter

router = APIRouter()
@router.get("")
def get_users():
    return []

@router.post("")
def create_user():
    return {"msg": "create user stub"}

@router.get("/{user_id}")
def get_user(user_id: int):
    return {"msg": "get user stub", "user_id": user_id}