from aiogram.types import ReplyKeyboardMarkup, KeyboardButton


menu_start = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='Найти исполнителя'),
            KeyboardButton(text='Найти заказы'),
            KeyboardButton(text='О Friendly Hobot')
        ]
    ],
    resize_keyboard=True)


# menu_start = ReplyKeyboardMarkup(
#     keyboard=[
#         [
#             KeyboardButton(text='Найти исполнителя'),
#             KeyboardButton(text='Ваши услуги и резюме'),
#             KeyboardButton(text='О Friendly Hobot')
#         ],
#         [
#             KeyboardButton(text='Оставить заявку'),
#             KeyboardButton(text='Мои заявки')
#         ]
#     ],
#     resize_keyboard=True)


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
            KeyboardButton(text='Найти заказы'),
            KeyboardButton(text='О Friendly Hobot')
        ],
        # [
        #     KeyboardButton(text="Редактировать в каталоге"),
        #     KeyboardButton(text='Добавить/изменить другого'),
        # ]
    ],
    resize_keyboard=True)
