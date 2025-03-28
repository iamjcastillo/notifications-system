from dataclasses import dataclass

MAX_LENGTH = 1000


@dataclass(frozen=True)
class Description:
    value: str

    def __post_init__(self):
        if not self.value.strip():
            raise ValueError("Description cannot be empty")
        if len(self.value) > MAX_LENGTH:
            raise ValueError("Description cannot exceed 1000 characters")

    @classmethod
    def create(cls, value: str):
        return cls(value)
