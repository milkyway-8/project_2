"""
Файл, где хранятся команды для бота, прописанные через декоратор
"""

import helpers
from telegramBot import *
import telebot


bot = TelegramBot(telebot.TeleBot(os.getenv('TOKEN')))


@bot.my_bot.message_handler(commands=["start"])
def start(message):
    """Функция выводит весь функционал бота, доступный пользователю"""
    bot.my_bot.send_message(message.chat.id, 'Привет! Я бот "Birthday Memory". Нажми\n/start\n'
                                             '/info\n/add_birthday\n/show_birthdays\n/favourite_colors\n'
                                             '/budget\n/preferences\n/age\n/help\n/delete\n/Postcard_female_friend\n'
                                             '/Postcard_male_friend\n/Postcard_family_member\n/Postcard_teacher')


@bot.my_bot.message_handler(commands=["info"])
def info(message):
    """Функция выдает информацию о том, что делает бот"""
    bot.my_bot.send_message(message.chat.id, helpers.command_info(message.from_user.first_name))  # бот отправляет
    # сообщение пользователю из helpers command_info


@bot.my_bot.message_handler(commands=["add_birthday"])
def add_birthday(message):
    """Функция, запускает добавление информации в словарь birthday"""
    information = bot.my_bot.reply_to(message, "Отправьте день рождения в таком формате:\nname_surname YYYY-MM-DD "
                                               "color_color budget preference_preference")
    bot.my_bot.register_next_step_handler(information, bot.add_birthday_to_dictionary_birthdays)


@bot.my_bot.message_handler(commands=["show_birthdays"])
def activate_show_birthdays(message):
    """Функция запускает вывод добавленной информации из словаря birthdays"""
    bot.show_birthdays(message)


@bot.my_bot.message_handler(commands=["delete"])
def activate_delete(message):
    """Функция запускает удаление конкретной информации"""
    information = bot.my_bot.reply_to(message, "Введите, какого пользователя и его данные хотите удалить в формате:"
                                               "'name_surname'")
    bot.my_bot.register_next_step_handler(information, bot.find_user_and_delete)


@bot.my_bot.message_handler(commands=["help"])
def help_function(message):
    """Функция показывает, что делать, если нужна помощь с тг ботом"""
    bot.my_bot.send_message(message.chat.id, "Если у тебя возник вопрос, найди Дамиру и спроси у нее😊")


@bot.my_bot.message_handler(commands=["favourite_colors"])
def activate_print_favourite_colors(message):
    """Функция обрабатывает команду /favourite_colors"""
    information = bot.my_bot.reply_to(message, "Введите имя и фамилию человека в формате name_surname,"
                                               "любимые цвета которого хотите узнать")
    bot.my_bot.register_next_step_handler(information, bot.print_favourite_colors)


@bot.my_bot.message_handler(commands=["budget"])
def activate_print_budget(message):
    """Функция обрабатывает команду /budget"""
    information = bot.my_bot.reply_to(message, "Введите имя и фамилию человека в формате name_surname,"
                                               "чтобы узнать, какой бюджет для подарка вы установили")
    bot.my_bot.register_next_step_handler(information, bot.print_budget)


@bot.my_bot.message_handler(commands=["preferences"])
def activate_print_preferences(message):
    """Функция обрабатывает команду /preferences"""
    information = bot.my_bot.reply_to(message, "Введите имя и фамилию человека в формате name_surname,"
                                               "чтобы узнать его предпочтения")
    bot.my_bot.register_next_step_handler(information, bot.print_preferences)


@bot.my_bot.message_handler(commands=["age"])
def activate_print_preferences(message):
    """Функция обрабатывает команду /show_age"""
    information = bot.my_bot.reply_to(message, "Введите имя и фамилию человека в формате name_surname,"
                                               "чтобы узнать, сколько ему лет на момент вызова команды")
    bot.my_bot.register_next_step_handler(information, bot.get_age)


@bot.my_bot.message_handler(commands=["Postcard_female_friend"])
def postcard_female_friend(message):
    """Функция отправляет открытку, подходящую для подруги"""
    file_female = open("./friend female.jpg", "rb")  # открытие файла в бинарном режиме на чтение
    bot.my_bot.send_photo(message.chat.id, file_female)  # отправка фото


@bot.my_bot.message_handler(commands=["Postcard_male_friend"])
def postcard_male_friend(message):
    """Функция отправляет открытку, подходящую для друга"""
    file_male = open("./friend male.jpg", "rb")
    bot.my_bot.send_photo(message.chat.id, file_male)


@bot.my_bot.message_handler(commands=["Postcard_family_member"])
def postcard_family_member(message):
    """Функция отправляет открытку, подходящую для члена семьи"""
    file_family = open("./family.jpg", "rb")
    bot.my_bot.send_photo(message.chat.id, file_family)


@bot.my_bot.message_handler(commands=["Postcard_teacher"])
def postcard_teacher(message):
    """Функция отправляет открытку, подходящую для учителя"""
    file_teacher = open("./teacher.jpg", "rb")
    bot.my_bot.send_photo(message.chat.id, file_teacher)
