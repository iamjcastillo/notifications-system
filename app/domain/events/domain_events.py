from abc import ABC
from dataclasses import dataclass
from typing import Tuple

from app.domain.value_objects.description import Description
from app.domain.value_objects.notification_id import NotificationID
from app.domain.value_objects.topic import Topic


@dataclass(frozen=True)
class DomainEvent(ABC):
    ...


@dataclass(frozen=True)
class NotificationCreatedEvent(DomainEvent):
    notification_id: NotificationID
    topic: Topic
    description: Description


@dataclass(frozen=True)
class EmailNotificationCreatedEvent(NotificationCreatedEvent):
    def create_email_content(self) -> Tuple[str, str, str]:
        recipient = "test@gmail.com"
        subject = f"New Notification: {self.topic.value}"
        body = f"You have a new notification regarding: {self.description.value}"
        return recipient, subject, body


@dataclass(frozen=True)
class SlackNotificationCreatedEvent(NotificationCreatedEvent):
    def create_slack_content(self) -> Tuple[str, str]:
        channel = f"New Notification: {self.topic.value}"
        message = f"You have a new notification regarding: {self.description.value}"
        return channel, message


@dataclass(frozen=True)
class NotionNotificationCreatedEvent(NotificationCreatedEvent):
    def create_notion_content(self) -> Tuple[str, str, str]:
        subject = f"New Notification: {self.topic.value}"
        body = f"You have a new notification regarding: {self.description.value}"
        return subject, body, str(self.notification_id.value)
