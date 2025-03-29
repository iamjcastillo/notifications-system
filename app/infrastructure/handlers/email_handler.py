from app.domain.events.domain_events import EmailNotificationCreatedEvent
from app.domain.handlers.notification_handlers import EmailNotificationHandler


class EmailHandler(EmailNotificationHandler):

    def handle(self, event: EmailNotificationCreatedEvent) -> None:
        recipient, subject, body = event.create_email_content()
        self.send_email(recipient, subject, body)

    def send_email(self, recipient: str, subject: str, body: str) -> None:
        print(f"Sending email to {recipient}")
        print(f"Subject: {subject}")
        print(f"Body: {body}")
