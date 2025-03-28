from dataclasses import dataclass

from app.domain.value_objects.description import Description
from app.domain.value_objects.notification_id import NotificationID
from app.domain.value_objects.topic import Topic


@dataclass(frozen=True)
class Notification:
    id: NotificationID
    topic: Topic
    description: Description

    @staticmethod
    def create(topic: Topic, description: Description) -> "Notification":
        return Notification(id=NotificationID.generate(), topic=topic, description=description)
