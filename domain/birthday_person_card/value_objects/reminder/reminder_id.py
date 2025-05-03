from dataclasses import dataclass
from uuid import UUID, uuid4


@dataclass(frozen=True)
class ReminderId:
    """Value object representing the identifier of a ReminderId"""

    value: UUID

    @staticmethod
    def generate() -> "ReminderId":
        """Generate a new ID"""
        return ReminderId(uuid4())

    def __str__(self) -> str:
        return str(self.value)
