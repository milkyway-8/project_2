"""
Файл хранит валидацию ввода пользователя, которая нужна для корректной работы тг бота и обработки ошибок
"""
import datetime


class Validation:
    @staticmethod
    def _validate_date(date):
        """Функция, которая валидирует введенную дату"""
        date_format = "%Y-%m-%d"
        try:
            date_object = datetime.datetime.strptime(date, date_format)
            current_date = datetime.datetime.now()  # получаем текущую дату
            if date_object <= current_date:
                return True
            else:
                return False
        except:
            return False

    @staticmethod
    def _validate_budget(budget):
        """Функция, которая валидирует введенный бюджет"""
        try:
            float(budget)  # проверка, что budget-целое число
            return True
        except:
            return False

    @staticmethod
    def _validate_name_surname(name_surname):
        """Функция, которая валидирует введенный ключ словаря birthdays(name_surname)"""
        if not isinstance(name_surname, str):
            return False
        if not (name_surname.isalpha() and "_" in name_surname):  # проверка, что name_surname содержит буквы и _
            return False
        return True
