from pydantic import BaseModel, Field,  ConfigDict

class TaskBase(BaseModel):
    title: str = Field(
        ..., 
        min_length=1, 
        max_length=100,
        description="Title of the task (1 - 100 characters)"
    )
    description: str | None = None


class TaskCreate(TaskBase):
    pass


class TaskUpdate(BaseModel):
    title: str | None = Field(None, min_length=1, max_length=100)
    description: str | None = None
    is_completed: bool | None = None

class TaskResponse(TaskBase):
    id: int
    is_completed: bool = False
    model_config = ConfigDict(from_attributes=True)