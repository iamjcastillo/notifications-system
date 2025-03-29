from abc import ABC, abstractmethod

from app.domain.entities.notification import Notification
from app.domain.events.event_publisher import EventPublisher
from app.domain.value_objects.description import Description
from app.domain.value_objects.topic import Topic


class NotificationService(ABC):
    @abstractmethod
    def create_notification(self, topic: Topic, description: Description) -> Notification:
        ...


class NotificationServiceImpl(NotificationService):
    def __init__(self, event_publisher: EventPublisher):
        self._event_publisher = event_publisher

    def create_notification(self, topic: str, description: str) -> Notification:
        topic = Topic.create(topic)
        description = Description.create(description)
        notification = Notification.create(topic, description, self._event_publisher)
        return notification
