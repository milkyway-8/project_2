"""
Файл, где хранится функция, использующаяся в коде, нужная для того, чтобы к пользователю обращались по имени
(разные пользователи тг бота-разные имена)
"""


def command_info(name):
    """Функция, которая возвращает сообщение пользователю об умениях тг бота, обращаясь к пользователю по имени"""
    return (f"{name}, я бот, который может напомнить тебе о Дне рождении близких людей.\n"
            "Еще я могу отправить тебе картинку для поздравления члена семьи/подруги/друга/учителя.")