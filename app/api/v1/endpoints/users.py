from fastapi import APIRouter, HTTPException, Depends
from app.services.user_service import UserService
from typing import Annotated
from app.schemas.user import UserCreate, UserResponse, UserUpdate
from app.core.exceptions import UserNotFoundError
from app.api.deps import get_user_service

router = APIRouter()
UserServiceDep = Annotated[UserService, Depends(get_user_service)]

@router.get("", response_model=list[UserResponse])
def get_users(service: UserServiceDep):
    return service.get_all_users()

@router.post("", response_model=UserResponse, status_code=201)
def create_user(data: UserCreate, service: UserServiceDep):
    return service.create_user(data)

@router.get("/{user_id}", response_model=UserResponse)
def get_user(user_id: int, service: UserServiceDep):
    try:
        return service.get_user(user_id)
    except UserNotFoundError:
        raise HTTPException(status_code=404, detail=f"User {user_id} not found")

@router.patch("/{user_id}", response_model=UserResponse)
def update_user(user_id: int, data: UserUpdate, service: UserServiceDep):
    try:
        return service.update_user(user_id, data)
    except UserNotFoundError:
        raise HTTPException(status_code=404, detail=f"User {user_id} not found")