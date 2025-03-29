import unittest
from unittest.mock import MagicMock

from app.application.services.notification_service import NotificationServiceImpl
from app.domain.entities.notification import Notification
from app.domain.events.event_publisher import EventPublisher
from app.domain.value_objects.description import Description
from app.domain.value_objects.topic import Topic


class NotificationServiceTestCase(unittest.TestCase):
    def test_given_topic_and_description_then_notification_is_created(self):
        topic = "pricing"
        description = "Email description"
        event_publisher = MagicMock(spec_set=EventPublisher)
        notification_service = NotificationServiceImpl(event_publisher)

        notification = notification_service.create_notification(topic, description)

        self.assertTrue(isinstance(notification, Notification))
        self.assertEqual(notification.topic, Topic.PRICING)
        self.assertTrue(isinstance(notification.description, Description))
        self.assertEqual(notification.description.value, description)
