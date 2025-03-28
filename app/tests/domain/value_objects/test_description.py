import unittest

from app.domain.value_objects.description import Description


class DescriptionTestCase(unittest.TestCase):
    def test_given_valid_description_when_creating_then_return_description(self):
        description = Description.create('Test description')

        self.assertEqual('Test description', description.value)

    def test_given_empty_description_when_creating_then_raise_value_error(self):
        with self.assertRaises(ValueError):
            Description.create('')

    def test_given_description_exceeding_max_length_when_creating_then_raise_value_error(self):
        with self.assertRaises(ValueError):
            Description.create('a' * 1001)
