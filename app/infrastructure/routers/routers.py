from fastapi import APIRouter

from app.infrastructure.dependency_injection import setup_notification_system
from app.infrastructure.dtos.dto import NotificationCreationRequest

router = APIRouter()


@router.get("/health", tags=["Health"])
async def health():
    return "Healthy"


@router.post("/notifications", tags=["Notifications"])
async def create_notification(notification_creation_request: NotificationCreationRequest):
    notification_service = setup_notification_system()
    notification_service.create_notification(
        notification_creation_request.topic, notification_creation_request.description
    )
