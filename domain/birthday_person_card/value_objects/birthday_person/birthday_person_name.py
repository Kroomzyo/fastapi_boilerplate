"""Value objects for Person name."""

from dataclasses import dataclass


@dataclass(frozen=True)
class BirthdayPersonName:
    """Value object representing the name of a Birthday_Person"""

    value: str

    def __post_init__(self):
        if len(self.value) > 30:
            raise ValueError("Name must be 30 characters or less")

    def __str__(self) -> str:
        return self.value
