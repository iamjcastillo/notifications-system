from dataclasses import dataclass

from app.domain.events.event_publisher import EventPublisher
from app.domain.value_objects.description import Description
from app.domain.value_objects.notification_id import NotificationID
from app.domain.value_objects.topic import Topic


@dataclass(frozen=True)
class Notification:
    id: NotificationID
    topic: Topic
    description: Description
    __event_classification = {}

    @classmethod
    def register_event(cls, topic: Topic, event_class: type) -> None:
        cls.__event_classification[topic] = event_class

    @classmethod
    def create(cls, topic: Topic, description: Description, event_publisher: EventPublisher) -> "Notification":
        notification_id = NotificationID.generate()
        notification = Notification(
            id=notification_id,
            topic=topic,
            description=description
        )

        if topic in cls.__event_classification:
            event = cls.__event_classification[topic](
                notification_id=notification_id, topic=topic, description=description
            )
            event_publisher.publish(event)

        return notification
