from aiogram.types import ReplyKeyboardMarkup, KeyboardButton


menu_start = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='Найти исполнителя'),
            KeyboardButton(text='Ваши услуги и резюме'),
            KeyboardButton(text='О Friendly Hobot')
        ]
        # [
        #     KeyboardButton(text="Посмотреть запросы"),
        #
        # ]
    ],
    resize_keyboard=True)


menu_main = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Главное меню"),
        ]
    ],
    resize_keyboard=True)


admin_menu = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Найти исполнителя"),
            KeyboardButton(text='Ваши услуги и резюме')
        ],
        [
            KeyboardButton(text="Посмотреть запросы"),
            KeyboardButton(text='Добавить/изменить другого'),
            KeyboardButton(text='О Friendly Hobot')
        ]
    ],
    resize_keyboard=True)
