from dataclasses import dataclass
from uuid import UUID, uuid4


@dataclass(frozen=True)
class NotificationID:
    value: UUID

    @staticmethod
    def generate():
        return NotificationID(uuid4())
