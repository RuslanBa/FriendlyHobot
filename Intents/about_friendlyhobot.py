from aiogram import types
from loader import dp
from inline_bottons import Specialties
from DB.add_log_db import add_new_log
from bottons import admin_menu


admin_id = [176221727]


@dp.message_handler(text='О Friendly Hobot')
async def answer(message: types.Message):
    id = message.from_user.id
    add_new_log(message.from_user.id, message.from_user.username, 'Аbout FriendlyHobot"')
    if id in admin_id:
        await message.answer('Привет, Коллега! Вижу, что ты админ)) Что ты хочешь сделать?',
                             reply_markup=admin_menu)
    else:
        await message.answer('Привет! Я сервис, помогающий подбирать нужных людей друг для друга. '
                             'Я еще "молод" - работаю сейчас только в Буэнос-Айресе, гуляю по чатам и собираю людей, '
                             'которые готовы помогать другими, предлагают свои услуги.\n\n'
                             'Если вы такой человек, то обязательно нажимайте на кнопку "Рассказать о себе". '
                             'Я задам несколько вопросов и создам ваш профиль в своей базе, чтобы показывать'
                             'его другим)) ')
