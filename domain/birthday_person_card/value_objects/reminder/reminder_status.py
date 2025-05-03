from dataclasses import dataclass
from enum import Enum


@dataclass(frozen=True)
class ReminderStatus(Enum):
    """Value object representing the identifier of a ReminderStatus"""

    ACTIVE = "active"
    INACTIVE = "inactive"

    def is_active(self) -> bool:
        """Check for active/inactive"""
        return self == ReminderStatus.ACTIVE

    @classmethod
    def from_string(cls, value: str) -> "ReminderStatus":
        """Creating status from a string"""
        if value == "active":
            return cls.ACTIVE
        elif value == "inactive":
            return cls.INACTIVE
        raise ValueError(f"Invalid status value: {value}")

    def __str__(self) -> str:
        """Basic Representation"""
        return str(self.value)
