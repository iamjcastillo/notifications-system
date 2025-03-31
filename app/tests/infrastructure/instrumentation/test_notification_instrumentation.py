import logging
import unittest
from unittest.mock import MagicMock

from app.infrastructure.instrumentation.notification_instrumentation import NotificationInstrumentation


class NotificationInstrumentationTestCase(unittest.TestCase):
    def test_error_sending_message(self):
        logger = MagicMock(spec=logging.Logger)
        instrumentation = NotificationInstrumentation(logger)
        instrumentation.error_sending_message("123", Exception("Test error"))

        self.assertEqual(logger.error.call_count, 1)
        self.assertEqual(
            logger.error.call_args[0][0],
            f"Error sending message. Notification ID: 123, error: Test error, trace_id {instrumentation.trace_id}"
        )
