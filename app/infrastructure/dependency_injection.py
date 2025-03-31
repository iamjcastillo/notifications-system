import logging

from app.application.services.notification_service import NotificationServiceImpl
from app.domain.events.domain_events import EmailNotificationCreatedEvent, SlackNotificationCreatedEvent, \
    NotionNotificationCreatedEvent
from app.domain.events.event_publisher import EventPublisherImpl
from app.infrastructure.handlers.email_handler import EmailHandler
from app.infrastructure.handlers.notion_handler import NotionHandler
from app.infrastructure.handlers.slack_handler import SlackHandler
from app.infrastructure.instrumentation.notification_instrumentation import NotificationInstrumentation


def setup_notification_system():
    logger = logging.getLogger(__name__)
    event_publisher = EventPublisherImpl()
    instrumentation = NotificationInstrumentation(logger)

    email_handler = EmailHandler()
    event_publisher.subscribe(EmailNotificationCreatedEvent, email_handler.handle)

    slack_handler = SlackHandler()
    event_publisher.subscribe(SlackNotificationCreatedEvent, slack_handler.handle)

    notion_handler = NotionHandler(instrumentation)
    event_publisher.subscribe(NotionNotificationCreatedEvent, notion_handler.handle)

    notification_service = NotificationServiceImpl(event_publisher)

    return notification_service
