import unittest
from unittest.mock import MagicMock

from app.domain.events.domain_events import EmailNotificationCreatedEvent
from app.domain.events.event_publisher import EventPublisherImpl
from app.domain.value_objects.description import Description
from app.domain.value_objects.notification_id import NotificationID
from app.domain.value_objects.topic import Topic


class EventPublisherTestCase(unittest.TestCase):
    def test_when_event_is_subscribed_then_it_is_subscribed(self):
        event_publisher = EventPublisherImpl()

        event_publisher.subscribe(EmailNotificationCreatedEvent, lambda x: x)

        expected_number_of_subscribers = 1
        self.assertEqual(expected_number_of_subscribers, len(event_publisher._subscribers))

    def test_when_event_is_published_then_event_handler_is_called(self):
        event_publisher = EventPublisherImpl()
        event_handler = MagicMock()
        event = EmailNotificationCreatedEvent(NotificationID.generate(), Topic.PRICING, Description("test"))
        event_publisher.subscribe(EmailNotificationCreatedEvent, event_handler)

        event_publisher.publish(event)

        expected_number_of_calls = 1
        self.assertEqual(expected_number_of_calls, event_handler.call_count)
