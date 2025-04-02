import unittest

from fastapi import FastAPI
from fastapi.testclient import TestClient
from starlette.status import HTTP_200_OK, HTTP_422_UNPROCESSABLE_ENTITY

from app.infrastructure.routers.exception_handlers import register_exception_handlers
from app.infrastructure.routers.routers import router

app = FastAPI()
app.include_router(router)
register_exception_handlers(app)

client = TestClient(app)


class RoutersTestCase(unittest.TestCase):
    def test_create_notification(self):
        test_data = {
            "topic": "pricing",
            "description": "Test Description"
        }

        response = client.post(
            "/notifications",
            json=test_data
        )

        response_json = response.json()
        notification = response_json.get("notification")
        self.assertEqual(response.status_code, HTTP_200_OK)
        self.assertEqual(notification.get("topic"), "pricing")
        self.assertEqual(notification.get("description"), "Test Description")

    def test_given_invalid_topic_then_return_unprocessable_entity_error(self):
        test_data = {
            "topic": "invalid",
            "description": "Test Description"
        }

        response = client.post(
            "/notifications",
            json=test_data
        )

        self.assertEqual(response.status_code, HTTP_422_UNPROCESSABLE_ENTITY)
        self.assertEqual(response.json().get("message"), "'invalid' is not a valid Topic")

    def test_given_invalid_description_then_return_unprocessable_entity_error(self):
        test_data = {
            "topic": "pricing",
            "description": "a" * 1001
        }

        response = client.post(
            "/notifications",
            json=test_data
        )

        self.assertEqual(response.status_code, HTTP_422_UNPROCESSABLE_ENTITY)
        self.assertEqual(response.json().get("message"), "Description cannot exceed 1000 characters")

    def test_given_empty_description_then_return_unprocessable_entity_error(self):
        test_data = {
            "topic": "pricing",
            "description": ""
        }

        response = client.post(
            "/notifications",
            json=test_data
        )

        self.assertEqual(response.status_code, HTTP_422_UNPROCESSABLE_ENTITY)
        self.assertEqual(response.json().get("message"), "Description cannot be empty")
