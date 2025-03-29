from enum import Enum


class Topic(Enum):
    SALES = "sales"
    PRICING = "pricing"

    @staticmethod
    def create(topic: str) -> "Topic":
        return Topic(topic)
