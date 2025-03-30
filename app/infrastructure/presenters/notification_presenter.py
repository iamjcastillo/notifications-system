from app.domain.entities.notification import Notification
from app.infrastructure.dtos.dto import NotificationDTO, NotificationResponse


class NotificationPresenter:
    @staticmethod
    def to_api_response(notification: Notification) -> NotificationResponse:
        return NotificationResponse(
            notification=NotificationDTO(
                id=str(notification.id.value),
                topic=notification.topic.value,
                description=notification.description.value
            )
        )
