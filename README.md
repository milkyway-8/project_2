# project_2
Автор: Алималлаева Дамира Фагилевна 464978

Проект2-улучшенная версия 1 проекта, модифицированный тг бот
# @modified_tg_reminder_bot
Бот, который может напомнить вам о Дне рождении близких людей. Еще он может отправить вам картинку для поздравления члена семьи/подруги/друга/учителя.

# Улучшения по сравнению с проектом 1:
Код переписан с функций на классы, добавлена функция просмотра возраста, предпочтений, бюджета, любимых цветов конкретного человека, теперь можно удалять не всех добавленных людей, а определенного человека. Теперь нельзя вводить неверный год рождения(в проекте 1 нельзя было вводить только неверный месяц/день). При некорректном вводе данных для человека вызываются различные ошибки.

# Как пользоваться?


После нажатия:

/start можно увидеть весь функционал бота, нажимая на который, будут исполняться различные функции

/info выдает информацию о тг боте

/add_birthday нужно ввести данные в указанном формате:  
# name_surname YYYY-MM-DD color_color_color budget preference_preference_preference
# ВАЖНО: Для минимизации ошибок пользователя советую проверять и помнить: 
          # цветов может быть больше или равно 1 шт, если их больше 1, то вводите через _. Например, розовый_черный_желтый_фиолетовый
          # предпочтений может быть больше или равно 1 шт, если их больше 1, то вводите через _. Например, танцы_плавание_бокс_игра_на_барабанах
          # пробелов между частями всех данных должно быть 4, всё введенное сообщение будет делиться на 5 частей
          # в name_surname должно быть только буквы и _
          # год/месяц/число следует вводить корректными и через -
# Если неверно ввести данные, бот пришлет сообщение о том, что именно пользователь ввел неверно.

/show_birthdays показывает всех уже добавленных пользователей

/favourite_colors нужно ввести name_surname-то, как вы вводили человека, когда записывали его данные. Потом по этому name_surname выводятся любимые цвет/цвета(!) конкретного человека

/budget нужно ввести name_surname-то, как вы вводили человека, когда записывали его данные. Потом по этому name_surname выводится бюджет подарка, который вы ставили, когда вводили данные человка

/preferences нужно ввести name_surname-то, как вы вводили человека, когда записывали его данные. Потом по этому name_surname выводятся предпочтение/предпочтения(!) конкретного человека

/age нужно ввести name_surname-то, как вы вводили человека, когда записывали его данные. Потом по этому name_surname выводится возраст человека(name_surname) на данный момент времени

/help выводит информацию о том, когда не знаете, что делать с ботом

/delete нужно ввести name_surname человека, данные о котором хотите удалить, тогда удалится только то, что связано с конкретным человеком и он сам

/Postcard_female_friend выводит открытку для поздравления подруги

/Postcard_male_friend выводит открытку для поздравления друга

/Postcard_family_member выводит открытку для поздравления члена семьи

/Postcard_teacher выводит открытку для поздравления учителя


# ВАЖНО: Если вы ввели что-то не то, снова нажмите /функция и введите корректно информацию, иначе бот не среагирует на ваш ввод




