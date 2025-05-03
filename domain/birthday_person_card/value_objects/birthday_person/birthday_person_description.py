"""Value objects for Person description."""

from dataclasses import dataclass


@dataclass(frozen=True)
class BirthdayPersonDescription:
    """Value object representing the description of a Birthday_Person"""

    value: str

    def __post_init__(self):
        if len(self.value) > 300:
            raise ValueError("Name must be 300 characters or less")

    def __str__(self) -> str:
        return self.value
