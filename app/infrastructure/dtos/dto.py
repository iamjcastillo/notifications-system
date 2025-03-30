from dataclasses import dataclass


@dataclass(frozen=True)
class NotificationCreationRequest:
    topic: str
    description: str


@dataclass(frozen=True)
class NotificationDTO:
    id: str
    topic: str
    description: str


@dataclass(frozen=True)
class NotificationResponse:
    notification: NotificationDTO
