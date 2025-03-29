from fastapi import FastAPI

from app.infrastructure.routers import routers
from app.infrastructure.routers.exception_handlers import register_exception_handlers

app = FastAPI(
    title='DDD API',
    description='A restful API for system handlers using Domain-Driven Design principles.',
    version='0.0.1',
)
app.include_router(routers.router)
register_exception_handlers(app)
