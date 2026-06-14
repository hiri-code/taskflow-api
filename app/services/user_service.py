from app.schemas.user import UserCreate, UserResponse, UserUpdate
from app.core.exceptions import UserNotFoundError

class UserService:
    def __init__(self):
        self._users: list[UserResponse] = []
        self._next_id: int = 1

    def get_all_users(self) -> list[UserResponse]:
        return self._users
    
    def get_user(self, user_id: int) -> UserResponse:
        for user in self._users:
            if user.id == user_id:
                return user
        raise UserNotFoundError(user_id)
    
    def create_user(self, data: UserCreate) -> UserResponse:
        new_user = UserResponse(
            id = self._next_id,
            email = data.email,
            username = data.username,
            is_active = True
        )
        self._users.append(new_user)
        self._next_id += 1
        return new_user
    
    def update_user(self, user_id: int, data: UserUpdate) -> UserResponse:
        user = self.get_user(user_id)

        updates = data.model_dump(exclude_unset=True)
        for field, value in updates.items():
            setattr(user, field, value)

        return user