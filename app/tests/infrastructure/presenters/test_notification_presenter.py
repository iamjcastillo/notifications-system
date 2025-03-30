import unittest

from app.domain.entities.notification import Notification
from app.domain.value_objects.description import Description
from app.domain.value_objects.notification_id import NotificationID
from app.domain.value_objects.topic import Topic
from app.infrastructure.dtos.dto import NotificationDTO, NotificationResponse
from app.infrastructure.presenters.notification_presenter import NotificationPresenter


class NotificationPresenterTestCase(unittest.TestCase):
    def test_given_notification_when_to_response_then_returns_notification_response(self):
        notification_id = NotificationID.generate()
        notification_topic = Topic.SALES
        notification_description = Description.create("Test Description")
        notification = Notification(
            id=notification_id,
            topic=notification_topic,
            description=notification_description
        )

        notification_response = NotificationPresenter.to_api_response(notification)

        self.assertIsInstance(notification_response, NotificationResponse)
        self.assertIsInstance(notification_response.notification, NotificationDTO)
        self.assertEqual(str(notification_id.value), notification_response.notification.id)
        self.assertEqual("sales", notification_response.notification.topic)
        self.assertEqual("Test Description", notification_response.notification.description)
