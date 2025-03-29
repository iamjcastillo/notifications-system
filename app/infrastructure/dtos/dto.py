from dataclasses import dataclass


@dataclass(frozen=True)
class NotificationCreationRequest:
    topic: str
    description: str
