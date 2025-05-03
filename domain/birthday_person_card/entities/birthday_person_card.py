from datetime import datetime
from typing import Optional

from domain.birthday_person_card.entities.reminder import Reminder
from domain.birthday_person_card.value_objects.birthday_person.birthday_person_description import (
    BirthdayPersonDescription,
)
from domain.birthday_person_card.value_objects.birthday_person.birthday_person_id import (
    BirthdayPersonId,
)
from domain.birthday_person_card.value_objects.birthday_person.birthday_person_name import (
    BirthdayPersonName,
)


class BirthdayPerson:
    """BirthdayCard entity represents a person having birthday with a number of details to fill notifications"""

    def __init__(
        self,
        id: BirthdayPersonId,
        birthday_person_name: BirthdayPersonName,
        birthday_date: Optional[datetime] = None,
        description: Optional[BirthdayPersonDescription] = None,
        reminder: Reminder = None,
    ):
        self._id = id
        self._birthday_person_name = birthday_person_name
        self._birthday_date = birthday_date
        self._description = description
        self._reminder = reminder

    @property
    def id(self) -> BirthdayPersonId:
        return self._id

    @property
    def birthday_person_name(self) -> BirthdayPersonName:
        return self._birthday_person_name

    @property
    def birthday_date(self) -> datetime:
        return self._birthday_date

    @property
    def description(self) -> BirthdayPersonDescription:
        return self._description

    @property
    def reminder(self) -> Reminder:
        return self._reminder

    @reminder.setter
    def reminder(self, reminder: Reminder) -> None:
        self._reminder = reminder

    def remove_reminder(self) -> None:
        self._reminder = None

    def __eq__(self, obj: object) -> bool:
        if isinstance(obj, BirthdayPerson):
            return self.id == obj.id
        return False

    @staticmethod
    def create(
        name: BirthdayPersonName,
        birth_date: Optional[datetime] = None,
        description: Optional[BirthdayPersonDescription] = None,
    ) -> "BirthdayPerson":
        """Create a new Birthday Person"""
        return BirthdayPerson(
            BirthdayPersonId.generate(), name, birth_date, description
        )
