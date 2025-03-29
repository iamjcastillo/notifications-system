from fastapi import FastAPI

from app.infrastructure.dependency_injection import setup_notification_system
from app.infrastructure.dtos.dto import NotificationCreationRequest

app = FastAPI(
    title='DDD API',
    description='A restful API for system handlers using Domain-Driven Design principles.',
    version='0.0.1',
)


@app.get("/health", tags=["Health"])
async def health():
    return "Healthy"


@app.post("/notifications", tags=["Notifications"])
async def create_notification(notification_creation_request: NotificationCreationRequest):
    notification_service = setup_notification_system()
    notification_service.create_notification(
        notification_creation_request.topic, notification_creation_request.description
    )
