class AppException(Exception):
    status_code: int = 500

    def __init__(self, detail: str):
        self.detail = detail
        super().__init__(detail)


class NotFoundError(AppException):
    status_code = 404


class ConflictError(AppException):
    status_code = 409


# ------> Unique exceptions <-------


class TaskNotFoundError(NotFoundError):
    def __init__(self, task_id: int):
        super().__init__(f"Task {task_id} not found")


class TaskAlreadyCompletedError(ConflictError):
    def __init__(self, task_id: int):
        super().__init__(f"Task {task_id} is already completed")


class UserNotFoundError(NotFoundError):
    def __init__(self, user_id: int):
        super().__init__(f"User {user_id} not found")