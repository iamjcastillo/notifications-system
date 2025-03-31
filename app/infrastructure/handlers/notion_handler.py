import os

from notion_client import Client

from app.domain.events.domain_events import NotionNotificationCreatedEvent
from app.domain.exceptions.exceptions import NotionException
from app.domain.handlers.notification_handlers import NotionNotificationHandler
from app.infrastructure.instrumentation.notification_instrumentation import NotificationInstrumentation

NOTION_API_KEY = os.getenv("NOTION_API_KEY")
NOTION_PAGE_ID = os.getenv("NOTION_PAGE_ID")


class NotionHandler(NotionNotificationHandler):
    def __init__(self, instrumentation: NotificationInstrumentation):
        self.notion = Client(auth=NOTION_API_KEY)
        self.page_id = NOTION_PAGE_ID
        self.instrumentation = instrumentation

    def handle(self, event: NotionNotificationCreatedEvent) -> None:
        subject, body, notification_id = event.create_notion_content()
        try:
            self.send_message(subject, body)
        except Exception as e:
            self.instrumentation.error_sending_message(notification_id, e)
            raise NotionException(f"Error sending message to Notion: {e}") from e

    def send_message(self, subject: str, body: str) -> None:
        table_block = {
            "type": "table",
            "table": {
                "table_width": 2,
                "has_column_header": True,
                "children": [
                    {
                        "type": "table_row",
                        "table_row": {
                            "cells": [
                                [{
                                    "type": "text",
                                    "text": {
                                        "content": subject
                                    }
                                }],
                                [{
                                    "type": "text",
                                    "text": {
                                        "content": body
                                    }
                                }]
                            ]
                        }
                    }
                ]
            }
        }

        self.notion.blocks.children.append(self.page_id, children=[table_block])
