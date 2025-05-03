from dataclasses import dataclass


@dataclass(frozen=True)
class ReminderBudget:
    """Value object representing the identifier of a ReminderBudget"""

    value: int

    def __post_init__(self):
        if self.value < 0 or self.value > 1000000:
            raise ValueError("Budget can be from zero to 1 million")

    @classmethod
    def from_int(cls, value: int) -> "ReminderBudget":
        return cls(value=value)

    def __str__(self) -> str:
        return str(self.value)
