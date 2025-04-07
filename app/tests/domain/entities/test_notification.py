import unittest
from unittest.mock import MagicMock

from app.domain.entities.notification import Notification
from app.domain.events.domain_events import EmailNotificationCreatedEvent, SlackNotificationCreatedEvent, \
    NotionNotificationCreatedEvent
from app.domain.events.event_publisher import EventPublisher
from app.domain.value_objects.description import Description
from app.domain.value_objects.notification_id import NotificationID
from app.domain.value_objects.topic import Topic


class NotificationTestCase(unittest.TestCase):
    def test_creating_notification_returns_correct_object(self):
        topic = Topic.SALES
        description = Description.create("Test description")
        event_publisher = MagicMock(spec_set=EventPublisher)
        Notification.register_event(Topic.SALES, SlackNotificationCreatedEvent)

        notification = Notification.create(topic, description, event_publisher)

        self.assertEqual(notification.topic, Topic.SALES)
        self.assertEqual(notification.description, Description.create("Test description"))
        self.assertTrue(isinstance(notification.id, NotificationID))

    def test_given_topic_is_pricing_when_notification_is_created_then_event_is_published(self):
        topic = Topic.PRICING
        description = Description.create("Email description")
        event_publisher = MagicMock(spec_set=EventPublisher)
        Notification.register_event(Topic.PRICING, EmailNotificationCreatedEvent)

        Notification.create(topic, description, event_publisher)

        expected_number_of_calls = 1
        self.assertEqual(expected_number_of_calls, event_publisher.publish.call_count)
        self.assertTrue(isinstance(event_publisher.publish.call_args[0][0], EmailNotificationCreatedEvent))

    def test_given_topic_is_sales_when_notification_is_created_then_event_is_published(self):
        topic = Topic.SALES
        description = Description.create("Slack description")
        event_publisher = MagicMock(spec_set=EventPublisher)
        Notification.register_event(Topic.SALES, SlackNotificationCreatedEvent)

        Notification.create(topic, description, event_publisher)

        expected_number_of_calls = 1
        self.assertEqual(expected_number_of_calls, event_publisher.publish.call_count)
        self.assertTrue(isinstance(event_publisher.publish.call_args[0][0], SlackNotificationCreatedEvent))

    def test_given_topic_is_support_when_notification_is_created_then_event_is_published(self):
        topic = Topic.SUPPORT
        description = Description.create("Notion description")
        event_publisher = MagicMock(spec_set=EventPublisher)
        Notification.register_event(Topic.SUPPORT, NotionNotificationCreatedEvent)

        Notification.create(topic, description, event_publisher)

        expected_number_of_calls = 1
        self.assertEqual(expected_number_of_calls, event_publisher.publish.call_count)
        self.assertTrue(isinstance(event_publisher.publish.call_args[0][0], NotionNotificationCreatedEvent))
