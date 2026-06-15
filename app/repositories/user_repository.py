from typing import Protocol

from app.schemas.user import UserResponse


class UserRepository(Protocol):
    def get_all(self) -> list[UserResponse]: ...
    def get_by_id(self, user_id: int) -> UserResponse | None: ...
    def add(self, user: UserResponse) -> UserResponse: ...
    def next_id(self) -> int: ...


class InMemoryUserRepository:
    def __init__(self):
        self._users: list[UserResponse] = []
        self._next_id: int = 1

    def get_all(self) -> list[UserResponse]:
        return self._users
    
    def get_by_id(self, user_id: int) -> UserResponse | None:
        for user in self._users:
            if user.id == user_id:
                return user
        return None
    
    def add(self, user: UserResponse) -> UserResponse:
        self._users.append(user)
        return user
    
    def next_id(self) -> int:
        current = self._next_id
        self._next_id += 1
        return current