from pydantic import BaseModel, Field, EmailStr, ConfigDict

class UserBase(BaseModel):
    email: EmailStr = Field(
        ...,
        description="User mail to login or register"
    )
    username: str = Field(
        ...,
        min_length=3,
        max_length=20,
    )


class UserCreate(UserBase):
    password: str = Field(..., min_length=8)


class UserUpdate(BaseModel):
    email: EmailStr | None = None
    username: str | None = None


class UserResponse(UserBase):
    id: int
    is_active: bool = True
    model_config = ConfigDict(from_attributes=True)