import logging
from uuid import uuid4


class NotificationInstrumentation:
    def __init__(self, logger: logging.Logger):
        self.logger = logger
        self.trace_id = uuid4()

    def error_sending_message(self, notification_id: str, error: Exception) -> None:
        self.logger.error(
            f"Error sending message. Notification ID: {notification_id}, error: {error}, trace_id {self.trace_id}"
        )
