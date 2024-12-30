"""
Файл, где находится класс Data, хранящий данные в формате json
"""

import json
import os
from exceptions import NoFileAvailable, SaveDataError, InvalidTypeData


class Data:
    """Инициализация birthday_file-файла, в котором хранятся данные(имя, фамилия, дата рождения и т.д.) в формате json
    """

    def __init__(self, birthday_file='birthdays.json'):
        self.birthday_file = birthday_file

    def load_birthdays(self):
        """Функция загружает информацию(имя, фамилия, дата ДР и т.д.) из формата json"""
        try:
            if not os.path.exists(self.birthday_file):
                return {}
            with open(self.birthday_file, "r") as file:
                file_information = file.read().strip()
                return json.loads(file_information) if file_information else {}
        except:
            raise NoFileAvailable(f"Файл {self.birthday_file} не найден")

    def save_birthdays(self, birthdays):
        """Сохранение информации(имя, фамилия, дата ДР и т.д.)"""
        try:
            with open(self.birthday_file, "w") as file:
                json.dump(birthdays, file, indent=4)
        except:
            raise SaveDataError(f"Ошибка сохранения файла")

    """
    Валидация через property
    """
    @property
    def birthday_file(self):
        return self._birthday_file

    @birthday_file.setter
    def birthday_file(self, value):
        if not isinstance(value, str):
            raise InvalidTypeData("birthday_file должен быть строкой")
        if not value.lower().endswith(".json"):
            raise InvalidTypeData("birthday_file должен оканчиваться на '.json'")
        self._birthday_file = value
