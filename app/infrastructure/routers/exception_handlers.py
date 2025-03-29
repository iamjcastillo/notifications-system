from fastapi import FastAPI, Request
from starlette.responses import JSONResponse
from starlette.status import HTTP_400_BAD_REQUEST


def register_exception_handlers(app: FastAPI):
    @app.exception_handler(ValueError)
    def value_error_exception_handler(_: Request, exc: ValueError):
        return JSONResponse(
            status_code=HTTP_400_BAD_REQUEST,
            content={"message": str(exc)}
        )
