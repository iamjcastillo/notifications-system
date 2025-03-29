from dataclasses import dataclass

from app.domain.value_objects.description import Description
from app.domain.value_objects.notification_id import NotificationID
from app.domain.value_objects.topic import Topic


@dataclass(frozen=True)
class DomainEvent:
    ...


@dataclass(frozen=True)
class NotificationCreatedEvent(DomainEvent):
    notification_id: NotificationID
    topic: Topic
    description: Description


@dataclass(frozen=True)
class EmailNotificationCreatedEvent(NotificationCreatedEvent):
    ...


@dataclass(frozen=True)
class SlackNotificationCreatedEvent(NotificationCreatedEvent):
    ...
