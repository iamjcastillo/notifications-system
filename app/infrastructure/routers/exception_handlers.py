from fastapi import FastAPI, Request
from starlette.responses import JSONResponse
from starlette.status import HTTP_500_INTERNAL_SERVER_ERROR, HTTP_422_UNPROCESSABLE_ENTITY

from app.domain.exceptions.exceptions import NotionException


def register_exception_handlers(app: FastAPI):
    @app.exception_handler(ValueError)
    def value_error_exception_handler(_: Request, exc: ValueError):
        return JSONResponse(
            status_code=HTTP_422_UNPROCESSABLE_ENTITY,
            content={"message": str(exc)}
        )

    @app.exception_handler(NotionException)
    def notion_exception_handler(_: Request, exc: NotionException):
        return JSONResponse(
            status_code=HTTP_500_INTERNAL_SERVER_ERROR,
            content={"message": str(exc)}
        )
