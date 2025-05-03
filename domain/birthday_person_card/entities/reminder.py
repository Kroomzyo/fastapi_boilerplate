from domain.birthday_person_card.value_objects.reminder.reminder_budget import (
    ReminderBudget,
)
from domain.birthday_person_card.value_objects.reminder.reminder_date import (
    ReminderDate,
)
from domain.birthday_person_card.value_objects.reminder.reminder_id import ReminderId
from domain.birthday_person_card.value_objects.reminder.reminder_status import (
    ReminderStatus,
)


class Reminder:
    """Reminder entity represents a one-time notification related to a BirthdayPerson"""

    def __init__(
        self,
        id: ReminderId,
        reminder_date: ReminderDate,
        budget: ReminderBudget = 0,
        status: ReminderStatus = ReminderStatus.INACTIVE,
    ):
        self._id = id
        self._reminder_date = reminder_date
        self._budget = budget
        self._status = status

    @property
    def id(self) -> ReminderId:
        return self._id

    @property
    def reminder_date(self) -> ReminderDate:
        return self._reminder_date

    @property
    def budget(self) -> ReminderBudget:
        return self._budget

    @property
    def status(self) -> ReminderStatus:
        return self._status

    def update_budget(self, new_budget: ReminderBudget) -> None:
        self._budget = new_budget

    def update_reminder_date(self, new_date: ReminderDate) -> None:
        self._reminder_date = new_date

    def activate(self) -> None:
        self._status = ReminderStatus.ACTIVE

    def deactivate(self) -> None:
        self._status = ReminderStatus.INACTIVE

    def is_active(self) -> bool:
        return self.status.is_active()

    def __repr__(self):
        return (
            f"Reminder(id={self.id}, "
            f"reminder_date={self.reminder_date}, "
            f"budget={self.budget.value}, "
            f"status={self.status.value})"
        )

    @staticmethod
    def create(
        reminder_date: ReminderDate,
        budget: ReminderBudget = ReminderBudget.from_int(0),
        status: ReminderStatus = ReminderStatus.INACTIVE,
    ) -> "Reminder":
        """Create a new Reminder"""
        return Reminder(
            id=ReminderId.generate(),
            reminder_date=reminder_date,
            budget=budget,
            status=status,
        )
