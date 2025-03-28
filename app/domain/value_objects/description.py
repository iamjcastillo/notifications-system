from dataclasses import dataclass


@dataclass(frozen=True)
class Description:
    value: str
