import unittest

from app.application.services.notification_service import NotificationServiceImpl
from app.domain.events.domain_events import EmailNotificationCreatedEvent, SlackNotificationCreatedEvent, \
    NotionNotificationCreatedEvent
from app.domain.events.event_publisher import EventPublisherImpl
from app.infrastructure.dependency_injection import setup_notification_system


class DITestCase(unittest.TestCase):
    def test_setup_notification_system(self):
        notification_service = setup_notification_system()

        assert isinstance(notification_service, NotificationServiceImpl)

        event_publisher = notification_service._event_publisher
        assert isinstance(event_publisher, EventPublisherImpl)

        assert EmailNotificationCreatedEvent in event_publisher._subscribers
        assert SlackNotificationCreatedEvent in event_publisher._subscribers
        assert NotionNotificationCreatedEvent in event_publisher._subscribers
