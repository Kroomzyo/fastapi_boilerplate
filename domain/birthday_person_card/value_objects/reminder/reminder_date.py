from dataclasses import dataclass
from datetime import datetime


@dataclass(frozen=True)
class ReminderDate:
    day: int
    month: int
    hour: int

    @classmethod
    def from_datetime(cls, dt: datetime) -> "ReminderDate":
        """Фабричный метод для создания ReminderDate из datetime."""
        return cls(day=dt.day, month=dt.month, hour=dt.hour)

    @classmethod
    def from_string(cls, date_str: str) -> "ReminderDate":
        """Фабричный метод для создания ReminderDate из строки в формате 'DD-MM HH'."""
        day_month, hour = date_str.split()
        day, month = map(int, day_month.split("-"))
        return cls(day=int(day), month=int(month), hour=int(hour))

    def to_string(self) -> str:
        """Возвращает строковое представление даты в формате 'DD-MM HH'."""
        return f"{self.day:02d}-{self.month:02d} {self.hour:02d}"

    def __str__(self):
        return self.to_string()

    def matches_current_time(self) -> bool:
        """Проверяет, совпадает ли текущая дата и время с этим напоминанием."""
        now = datetime.now()
        return self.day == now.day and self.month == now.month and self.hour == now.hour
