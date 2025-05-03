from dataclasses import dataclass
from uuid import UUID, uuid4


@dataclass(frozen=True)
class BirthdayPersonId:
    """Value object representing the identifier of a BirthdayPersonId"""

    value: UUID

    @staticmethod
    def generate() -> "BirthdayPersonId":
        """Generate a new ID"""
        return BirthdayPersonId(uuid4())

    def __str__(self) -> str:
        return str(self.value)
