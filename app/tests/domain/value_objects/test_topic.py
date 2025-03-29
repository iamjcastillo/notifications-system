import unittest

from app.domain.value_objects.topic import Topic


class TopicTestCase(unittest.TestCase):
    def test_given_sales_topic_when_create_then_topic_is_created(self):
        topic = Topic.create("sales")
        self.assertEqual(topic, Topic.SALES)

    def test_given_pricing_topic_when_create_then_topic_is_created(self):
        topic = Topic.create("pricing")
        self.assertEqual(topic, Topic.PRICING)

    def test_given_invalid_topic_when_create_then_error_is_raised(self):
        with self.assertRaises(ValueError):
            Topic.create("invalid")
