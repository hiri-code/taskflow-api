import logging

from app.schemas.user import UserCreate, UserResponse, UserUpdate
from app.core.exceptions import UserNotFoundError
from app.repositories.user_repository import UserRepository

logger = logging.getLogger(__name__)

class UserService:
    def __init__(self, repository: UserRepository):
        self._repository = repository        

    def get_all_users(self) -> list[UserResponse]:
        return self._repository.get_all()
    
    def get_user(self, user_id: int) -> UserResponse:
        user = self._repository.get_by_id(user_id)
        if user is None:
            logger.warning("User not found: id=%s", user_id)
            raise UserNotFoundError(user_id)
        return user

    def create_user(self, data: UserCreate) -> UserResponse:
        new_user = UserResponse(
            id = self._repository.next_id(),
            email = data.email,
            username = data.username,
            is_active = True
        )
        self._repository.add(new_user)
        logger.info("User created: id=%s email=%s username=%s", new_user.id, new_user.email, new_user.username)
        return new_user
    
    def update_user(self, user_id: int, data: UserUpdate) -> UserResponse:
        user = self.get_user(user_id)
        updates = data.model_dump(exclude_unset=True)
        for field, value in updates.items():
            setattr(user, field, value)
        return user