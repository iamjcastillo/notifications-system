import unittest
from unittest.mock import patch

from app.domain.entities.notification import NotificationID
from app.domain.events.domain_events import EmailNotificationCreatedEvent
from app.domain.value_objects.description import Description
from app.domain.value_objects.topic import Topic
from app.infrastructure.handlers.email_handler import EmailHandler


class EmailHandlerTestCase(unittest.TestCase):
    @patch("app.infrastructure.handlers.email_handler.EmailHandler.send_email")
    def test_given_email_notification_created_event_when_handling_then_email_is_sent(self, mock_send_email):
        notification_id = NotificationID.generate()
        topic = Topic.PRICING
        description = Description.create("Email description")
        event = EmailNotificationCreatedEvent(notification_id, topic, description)
        handler = EmailHandler()

        handler.handle(event)

        self.assertTrue(mock_send_email.called)
        self.assertEqual(mock_send_email.call_count, 1)
        self.assertEqual(mock_send_email.call_args[0][0], "test@gmail.com")
        self.assertEqual(mock_send_email.call_args[0][1], "New Notification: pricing")
        self.assertEqual(mock_send_email.call_args[0][2], "You have a new notification regarding: Email description")
