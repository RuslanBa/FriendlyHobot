from aiogram.types import ReplyKeyboardMarkup, KeyboardButton


menu_start = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Найти специалиста"),
            KeyboardButton(text="Рассказать о себе"),
            KeyboardButton(text='О сервисе')
        ]
    ],
    resize_keyboard=True)
