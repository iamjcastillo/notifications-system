import unittest

from app.domain.value_objects.description import Description


class DescriptionTestCase(unittest.TestCase):
    def test_create_valid_description(self):
        description = Description('Test description')

        self.assertEqual('Test description', description.value)
