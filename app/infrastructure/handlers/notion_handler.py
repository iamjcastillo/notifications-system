import os

from notion_client import Client

from app.domain.events.domain_events import NotionNotificationCreatedEvent
from app.domain.exceptions.exceptions import NotionException
from app.domain.handlers.notification_handlers import NotionNotificationHandler

NOTION_API_KEY = os.getenv("NOTION_API_KEY")
NOTION_PAGE_ID = os.getenv("NOTION_PAGE_ID")


class NotionHandler(NotionNotificationHandler):
    def __init__(self):
        self.notion = Client(auth=NOTION_API_KEY)
        self.page_id = NOTION_PAGE_ID

    def handle(self, event: NotionNotificationCreatedEvent) -> None:
        subject, body = event.create_notion_content()
        self.send_message(subject, body)

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

        try:
            self.notion.blocks.children.append(self.page_id, children=[table_block])
        except Exception as e:
            raise NotionException(f"Error sending message to Notion: {e}") from e
