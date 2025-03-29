from app.domain.events.domain_events import SlackNotificationCreatedEvent
from app.domain.handlers.notification_handlers import SlackNotificationHandler


class SlackHandler(SlackNotificationHandler):
    def handle(self, event: SlackNotificationCreatedEvent):
        channel, message = event.create_slack_content()
        self.send_message(channel, message)

    def send_message(self, channel: str, message: str) -> None:
        raise NotImplementedError("Slack handler not implemented")
