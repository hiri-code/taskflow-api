import logging

from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
from app.core.exceptions import AppException

logger = logging.getLogger(__name__)

async def app_exception_handler(request: Request, exc: AppException) -> JSONResponse:
    if exc.status_code >= 500:
        logger.error(
            "%s %s -> %s: %s", request.method, request.url.path, exc.status_code, exc.detail
        )
    else:
        logger.warning(
            "%s %s -> %s: %s", request.method, request.url.path, exc.status_code, exc.detail
        )

    return JSONResponse(
        status_code=exc.status_code,
        content={"detail": exc.detail},
    )

def register_exception_handlers(app: FastAPI) -> None:
    app.add_exception_handler(AppException, app_exception_handler)