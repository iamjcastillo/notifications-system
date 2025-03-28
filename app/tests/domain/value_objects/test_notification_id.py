import unittest
from uuid import UUID

from app.domain.value_objects.notification_id import NotificationID


class NotificationIDTestCase(unittest.TestCase):
    def test_generating_notification_id_creates_valid_uuid(self):
        notification_id = NotificationID.generate()

        self.assertTrue(isinstance(notification_id.value, UUID))

    def test_generating_notification_id_creates_unique_ids(self):
        first_notification_id = NotificationID.generate()
        second_notification_id = NotificationID.generate()

        self.assertNotEqual(first_notification_id, second_notification_id)
