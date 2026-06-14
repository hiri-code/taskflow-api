from fastapi import FastAPI
from app.api.v1.router import api_router
from app.core.config import settings
from app.core.exception_handlers import register_exception_handlers
from app.core.logging import setup_logging
from app.core.middleware import log_requests_middleware

setup_logging()

app = FastAPI(
    title=settings.PROJECT_NAME,
    description=settings.DESCRIPTION_PROJECT,
    version=settings.VERSION_PROJECT
)

register_exception_handlers(app)
app.include_router(api_router, prefix=settings.API_V1_PREFIX)
app.middleware("http")(log_requests_middleware)