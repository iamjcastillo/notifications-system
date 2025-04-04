from dataclasses import dataclass

from app.domain.events.domain_events import EmailNotificationCreatedEvent, \
    SlackNotificationCreatedEvent, NotionNotificationCreatedEvent
from app.domain.events.event_publisher import EventPublisher
from app.domain.value_objects.description import Description
from app.domain.value_objects.notification_id import NotificationID
from app.domain.value_objects.topic import Topic


@dataclass(frozen=True)
class Notification:
    id: NotificationID
    topic: Topic
    description: Description
    __event_classification = {
        Topic.PRICING: EmailNotificationCreatedEvent,
        Topic.SALES: SlackNotificationCreatedEvent,
        Topic.SUPPORT: NotionNotificationCreatedEvent
    }

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
