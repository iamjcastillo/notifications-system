import unittest

from app.domain.entities.notification import NotificationID
from app.domain.events.domain_events import EmailNotificationCreatedEvent, SlackNotificationCreatedEvent, \
    NotionNotificationCreatedEvent
from app.domain.value_objects.description import Description
from app.domain.value_objects.topic import Topic


class DomainEventTestCase(unittest.TestCase):
    def test_given_email_notification_created_event_when_creating_content_then_email_content_is_created(self):
        notification_id = NotificationID.generate()
        topic = Topic.PRICING
        description = Description.create("Email description")
        event = EmailNotificationCreatedEvent(notification_id, topic, description)

        recipient, subject, body = event.create_email_content()

        self.assertEqual(recipient, "test@gmail.com")
        self.assertEqual(subject, "New Notification: pricing")
        self.assertEqual(body, "You have a new notification regarding: Email description")

    def test_given_slack_notification_created_event_when_creating_content_then_slack_content_is_created(self):
        notification_id = NotificationID.generate()
        topic = Topic.SALES
        description = Description.create("Slack description")
        event = SlackNotificationCreatedEvent(notification_id, topic, description)

        channel, message = event.create_slack_content()

        self.assertEqual(channel, "New Notification: sales")
        self.assertEqual(message, "You have a new notification regarding: Slack description")

    def test_given_notion_notification_created_event_when_creating_content_then_notion_content_is_created(self):
        notification_id = NotificationID.generate()
        topic = Topic.SUPPORT
        description = Description.create("Notion description")
        event = NotionNotificationCreatedEvent(notification_id, topic, description)

        subject, body = event.create_notion_content()

        self.assertEqual(subject, "New Notification: support")
        self.assertEqual(body, "You have a new notification regarding: Notion description")
