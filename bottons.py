from aiogram.types import ReplyKeyboardMarkup, KeyboardButton


menu_start = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Найти работу или заказы"),
            KeyboardButton(text="Найти людей"),
            KeyboardButton(text='О сервисе')
        ]
    ],
    resize_keyboard=True)
