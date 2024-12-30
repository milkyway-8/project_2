"""
Файл, где хранятся самописные исключения
"""


class InvalidTypeData(Exception):  # исключение для неподходящего типа информации
    pass


class NoFileAvailable(Exception):  # вызывается, если файл не найден
    pass


class SaveDataError(Exception):  # вызывается при ошибке сохранения информации
    pass


class InvalidBotType(Exception):  # вызывается, когда бот не telebot
    pass


class IncorrectInterval(Exception):  # вызывается при неверном установленном интервале
    pass