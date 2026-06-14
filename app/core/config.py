from pydantic_settings import BaseSettings, SettingsConfigDict
from typing import Literal
from pydantic import field_validator
from functools import lru_cache


class Settings(BaseSettings):
    PROJECT_NAME: str = "TaskFlow API"
    DESCRIPTION_PROJECT: str = "Collaborative task and project management API"
    VERSION_PROJECT: str = "0.1.0"
    DEBUG: bool = False
    API_V1_PREFIX: str = "/api/v1"
    ENVIRONMENT: Literal["development", "testing", "production"] = "development"
    CORS_ORIGINS: list[str] = []

    @field_validator("CORS_ORIGINS", mode="before")
    @classmethod
    def parse_cors_origins(cls, value):
        if isinstance(value, str):
            return [origin.strip() for origin in value.split(",") if origin.strip()]
        return value

    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
    )


@lru_cache
def get_settings() -> Settings:
    return Settings()

settings = get_settings()