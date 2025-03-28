import unittest

from app.domain.entities.notification import Notification
from app.domain.value_objects.description import Description
from app.domain.value_objects.notification_id import NotificationID
from app.domain.value_objects.topic import Topic


class NotificationTestCase(unittest.TestCase):
    def test_creating_notification_returns_correct_object(self):
        topic = Topic.SALES
        description = Description("Test description")

        notification = Notification.create(topic, description)

        self.assertEqual(notification.topic, Topic.SALES)
        self.assertEqual(notification.description, Description("Test description"))
        self.assertTrue(isinstance(notification.id, NotificationID))
