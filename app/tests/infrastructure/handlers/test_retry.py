import unittest

from app.infrastructure.handlers.retry import retry


class TestRetry(unittest.TestCase):
    def test_given_retry_decorator_when_decorating_function_then_function_is_called(self):
        @retry(max_retries=3, delay=1, backoff=2)
        def test_function():
            return "Success"

        result = test_function()
        self.assertEqual(result, "Success")
