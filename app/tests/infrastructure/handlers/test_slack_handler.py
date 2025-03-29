import unittest

from app.domain.entities.notification import NotificationID
from app.domain.events.domain_events import SlackNotificationCreatedEvent
from app.domain.value_objects.description import Description
from app.domain.value_objects.topic import Topic
from app.infrastructure.handlers.slack_handler import SlackHandler


class SlackHandlerTestCase(unittest.TestCase):
    def test_given_slack_notification_created_event_when_handle_then_error_is_raised(self):
        notification_id = NotificationID.generate()
        topic = Topic.SALES
        description = Description.create("Slack description")
        event = SlackNotificationCreatedEvent(notification_id, topic, description)
        handler = SlackHandler()

        with self.assertRaises(NotImplementedError):
            handler.handle(event)
