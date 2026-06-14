from fastapi import APIRouter, HTTPException
from app.services.user_service import UserService
from app.schemas.user import UserCreate, UserResponse, UserUpdate
from app.core.exceptions import UserNotFoundError

router = APIRouter()
user_service = UserService()

@router.get("", response_model=list[UserResponse])
def get_users():
    return user_service.get_all_users()

@router.post("", response_model=UserResponse, status_code=201)
def create_user(data: UserCreate):
    return user_service.create_user(data)

@router.get("/{user_id}", response_model=UserResponse)
def get_user(user_id: int):
    try:
        return user_service.get_user(user_id)
    except UserNotFoundError:
        raise HTTPException(status_code=404, detail=f"User {user_id} not found")

@router.patch("/{user_id}", response_model=UserResponse)
def update_user(user_id: int, data: UserUpdate):
    try:
        return user_service.update_user(user_id, data)
    except UserNotFoundError:
        raise HTTPException(status_code=404, detail=f"User {user_id} not found")