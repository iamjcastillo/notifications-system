from abc import ABC, abstractmethod

from app.domain.events.domain_events import NotificationCreatedEvent


class NotificationHandler(ABC):
    @abstractmethod
    def handle(self, event: NotificationCreatedEvent) -> None:
        pass


class EmailNotificationHandler(NotificationHandler):
    @abstractmethod
    def send_email(self, recipient: str, subject: str, body: str) -> None:
        pass


class SlackNotificationHandler(NotificationHandler):
    @abstractmethod
    def send_message(self, channel: str, message: str) -> None:
        pass


class NotionNotificationHandler(NotificationHandler):
    @abstractmethod
    def send_message(self, subject: str, body: str) -> None:
        pass
