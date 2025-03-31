import unittest
from unittest.mock import patch, MagicMock

from app.domain.events.domain_events import NotionNotificationCreatedEvent
from app.domain.exceptions.exceptions import NotionException
from app.domain.value_objects.description import Description
from app.domain.value_objects.notification_id import NotificationID
from app.domain.value_objects.topic import Topic
from app.infrastructure.handlers.notion_handler import NotionHandler
from app.infrastructure.instrumentation.notification_instrumentation import NotificationInstrumentation


class NotionHandlerTestCase(unittest.TestCase):
    @patch("app.infrastructure.handlers.notion_handler.NotionHandler.send_message")
    def test_given_notion_notification_created_event_when_handling_then_message_is_sent(self, mock_send_message):
        notification_id = NotificationID.generate()
        topic = Topic.SUPPORT
        description = Description.create("Notion description")
        event = NotionNotificationCreatedEvent(notification_id, topic, description)
        instrumentation = MagicMock(spec=NotificationInstrumentation)
        handler = NotionHandler(instrumentation)

        handler.handle(event)

        self.assertTrue(mock_send_message.called)
        self.assertEqual(mock_send_message.call_count, 1)
        self.assertEqual(mock_send_message.call_args[0][0], "New Notification: support")
        self.assertEqual(mock_send_message.call_args[0][1], "You have a new notification regarding: Notion description")

    @patch("app.infrastructure.handlers.notion_handler.Client")
    def test_given_notion_exception_when_handling_then_exception_is_raised(self, mock_notion):
        mock_notion.return_value.blocks.children.append.side_effect = Exception("Error sending message to Notion")
        notification_id = NotificationID.generate()
        topic = Topic.SUPPORT
        description = Description.create("Notion description")
        event = NotionNotificationCreatedEvent(notification_id, topic, description)
        instrumentation = MagicMock(spec=NotificationInstrumentation)
        handler = NotionHandler(instrumentation)

        with self.assertRaises(NotionException):
            handler.handle(event)
