"""Файл хранит весь основной функционал тг бота"""

from datetime import datetime, timedelta
import telebot
from apscheduler.schedulers.background import BackgroundScheduler
from dotenv import load_dotenv

from Data import *
from exceptions import InvalidTypeData, InvalidBotType, IncorrectInterval
from validation import *

load_dotenv()


class TelegramBot:
    def __init__(self, bot, data_storage=Data("birthdays.json"), schedule_interval=30):  #устанавливаю интервал на 30с,
        # но это для того, чтобы быстрее показывало при проверке
        self.my_bot = bot
        self.birthdays = data_storage.load_birthdays()
        self.data_storage = data_storage
        self.schedule_interval = schedule_interval
        self.scheduler = BackgroundScheduler()  # создаем планировщик
        self.set_scheduler()  # устанавливаем планировщик

    """Валидация через property"""
    @property
    def my_bot(self):
        return self._my_bot

    @my_bot.setter
    def my_bot(self, value):
        if not isinstance(value, telebot.TeleBot):
            raise InvalidBotType("Бот должен быть экземпляром telebot.TeleBot")
        self._my_bot = value

    @property
    def data_storage(self):
        return self._data_storage

    @data_storage.setter
    def data_storage(self, value):
        if not isinstance(value, Data):
            raise InvalidTypeData("data_storage должен быть экземпляром класса Data")
        self._data_storage = value

    @property
    def schedule_interval(self):
        return self._schedule_interval

    @schedule_interval.setter
    def schedule_interval(self, value):
        if not isinstance(value, int):
            raise InvalidTypeData("schedule_interval должно быть целым числом")
        if value <= 0:
            raise IncorrectInterval("schedule_interval должно быть больше 0")
        self._schedule_interval = value


    @staticmethod
    def check_input(message):  # идею, как реализовать эту функцию, помог придумать chat gpt
        """Функция проверяет введенную пользователем информацию, заполняется словарь ошибок разными возникшими ошибками,
        если они есть"""
        parts = message.text.split(" ", 5)  # Разделяем сообщение на 5 частей
        if len(parts) != 5:
            return {
                "error": "Неверное количество аргументов, введите 5 значений(иными словами, пробелов должно быть 4)."}
        name_surname, date, favourite_color, budget, preferences = parts
        errors = {}  # создание словаря errors, где ключи-то, что показывает, по какому аргументу прозошла ошибка,
        # а значение-текст ошибки, который впоследствии будет выводиться пользователю
        if not Validation._validate_name_surname(name_surname):
            errors['name_surname'] = "Имя и фамилия должны содержать буквы и _."
        if not Validation._validate_date(date):
            errors['date'] = "Некорректный формат даты. Введите дату в формате YYYY-MM-DD."
        if not Validation._validate_budget(budget):
            errors['budget'] = "Бюджет должен быть числом."
        return errors

    def add_birthday_to_dictionary_birthdays(self, message):
        """Функция добавляет информацию в словарь birthdays
        при отсутствии ошибок, либо выводит пользователю возникшие ошибки"""
        try:
            errors = self.check_input(message)
            if errors:
                error_message = "\n".join(errors.values())
                self.my_bot.reply_to(message, f"Ошибка ввода:\n{error_message}\nНажми снова /add_birthday")
                return
            name_surname, date, favourite_color, budget, preferences = message.text.split(" ", 5)
            if name_surname in self.birthdays:
                self.my_bot.reply_to(message,
                                     "Такие имя и фамилия уже были добавлены. Вызовите /add_birthday еще раз и "
                                     "введите данные"
                                     "в формате: "
                                     "'name_surname YYYY-MM-DD color_color_color budget "
                                     "preference_preference_preference'.")
                return
            self.birthdays[name_surname] = [date, message.chat.id, favourite_color, budget, preferences]
            self.data_storage.save_birthdays(self.birthdays)
            self.my_bot.reply_to(message, f"День Рождения для {name_surname} на {date} добавлен!")
        except:
            self.my_bot.reply_to(message, "Попробуйте снова. Вызовите /add_birthday еще раз и введите данные "
                                          "в формате: "
                                          "'name_surname YYYY-MM-DD color_color_color... budget "
                                          "preference_preference_preference...'.")

    def get_birthday_year(self, message):
        """Функция возвращает год рождения человека"""
        return int(self.birthdays[message.text][0].split("-")[0])

    def get_age(self, message):
        """Функция возвращает возраст человека на сегодняшний момент"""
        if message.text in self.birthdays.keys():
            current_year = datetime.datetime.now().year
            birthday_year = self.get_birthday_year(message)
            age = current_year - birthday_year
            self.my_bot.reply_to(message, f"Человеку {message.text} сейчас {age}")
        else:
            self.my_bot.send_message(message.chat.id, text='Попробуй ещё. Для этого снова введи /show_age')

    def show_birthdays(self, message):
        """Функция показывает то, что записано в словарь, а именно name_surname и дату рождения"""
        if self.birthdays:
            response = "🎂 Предстоящие Дни Рождения:\n"
            for key, value in self.birthdays.items():
                response += f"- {key}: {value[0]}\n"
        else:
            response = "Ничего ещё не добавлено"
        self.my_bot.reply_to(message, response)

    def find_user_and_delete(self, message):
        """Функция удаляет человека(=ключ) из словаря birthdays"""
        if message.text in self.birthdays.keys():
            del self.birthdays[message.text]
            self.data_storage.save_birthdays(self.birthdays)
            self.my_bot.reply_to(message, f"{message.text} удалён!")
        else:
            self.my_bot.send_message(message.chat.id, text='Попробуй ещё. Для этого снова введи /delete ')

    def print_favourite_colors(self, message):
        """Функция выводит любимые цвета по name_surname"""
        if message.text in self.birthdays.keys():
            self.my_bot.send_message(message.chat.id, f"Любимые цвета: "
                                                      f"{', '.join(self.birthdays[message.text][2].split('_'))}")
        else:
            self.my_bot.send_message(message.chat.id, text='Попробуй ещё. Для этого снова введи /favourite_colors')

    def print_budget(self, message):
        """Функция выводит бюджет на подарок по name_surname"""
        if message.text in self.birthdays.keys():
            self.my_bot.send_message(message.chat.id, f"Бюджет: {self.birthdays[message.text][3]}")
        else:
            self.my_bot.send_message(message.chat.id, text='Попробуй ещё. Для этого снова введи /budget')

    def print_preferences(self, message):
        """Функция выводит предпочтения по name_surname"""
        if message.text in self.birthdays.keys():
            self.my_bot.send_message(message.chat.id, f"Предпочтения: {self.birthdays[message.text][4]}")
        else:
            self.my_bot.send_message(message.chat.id, text='Попробуй ещё. Для этого снова введи /preferences')

    def set_scheduler(self):
        """Функция устанавливает планировщик"""
        self.scheduler.add_job(self.send_birthday_reminders, "interval", seconds=self.schedule_interval,
                               start_date=datetime.datetime.now() + timedelta(seconds=10))
        self.scheduler.start()

    def send_birthday_reminders(self):
        """Функция отправляет уведомления о наступившем ДР"""
        today = datetime.datetime.now().date()
        for key, value in self.birthdays.items():
            try:
                birthday = datetime.datetime.strptime(value[0], "%Y-%m-%d").date()
                if birthday.month == today.month and birthday.day == today.day:
                    self.my_bot.send_message(chat_id=value[1], text=f"🎉 Сегодня день рождения у {key}! 🎂")
            except:

                print(f"Ошибка отправки напоминания для {key}")
