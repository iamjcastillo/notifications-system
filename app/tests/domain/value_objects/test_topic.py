import unittest

from app.domain.value_objects.topic import Topic


class TopicTestCase(unittest.TestCase):
    def test_topic_values_are_correct(self):
        self.assertEqual("sales", Topic.SALES.value)
        self.assertEqual("pricing", Topic.PRICING.value)
