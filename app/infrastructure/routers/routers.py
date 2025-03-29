from fastapi import APIRouter, Request
from slowapi import Limiter
from slowapi.util import get_remote_address

from app.infrastructure.dependency_injection import setup_notification_system
from app.infrastructure.dtos.dto import NotificationCreationRequest

router = APIRouter()
limiter = Limiter(key_func=get_remote_address)


@router.get("/health", tags=["Health"])
@limiter.limit("10/minute")
async def health(request: Request):
    return "Healthy"


@router.post("/notifications", tags=["Notifications"])
@limiter.limit("5/minute")
async def create_notification(
        request: Request,
        notification_creation_request: NotificationCreationRequest
):
    notification_service = setup_notification_system()
    notification_service.create_notification(
        notification_creation_request.topic, notification_creation_request.description
    )
