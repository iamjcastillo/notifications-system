from app.application.services.notification_service import NotificationServiceImpl
from app.domain.events.domain_events import EmailNotificationCreatedEvent, SlackNotificationCreatedEvent, \
    NotionNotificationCreatedEvent
from app.domain.events.event_publisher import EventPublisherImpl
from app.infrastructure.handlers.email_handler import EmailHandler
from app.infrastructure.handlers.notion_handler import NotionHandler
from app.infrastructure.handlers.slack_handler import SlackHandler


def setup_notification_system():
    event_publisher = EventPublisherImpl()

    email_handler = EmailHandler()
    event_publisher.subscribe(EmailNotificationCreatedEvent, email_handler.handle)

    slack_handler = SlackHandler()
    event_publisher.subscribe(SlackNotificationCreatedEvent, slack_handler.handle)

    notion_handler = NotionHandler()
    event_publisher.subscribe(NotionNotificationCreatedEvent, notion_handler.handle)

    notification_service = NotificationServiceImpl(event_publisher)

    return notification_service
