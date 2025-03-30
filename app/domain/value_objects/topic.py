from enum import Enum


class Topic(Enum):
    SALES = "sales"
    PRICING = "pricing"
    SUPPORT = "support"

    @staticmethod
    def create(topic: str) -> "Topic":
        return Topic(topic)
