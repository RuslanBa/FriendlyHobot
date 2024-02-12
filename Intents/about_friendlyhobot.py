from aiogram import types
from aiogram.dispatcher.storage import FSMContext
from loader import dp, bot
from inline_bottons import feedback, admin_buttons
from DB.add_log_db import add_new_log
from bottons import admin_menu
from Classes.states_classes import Feedback
from loader import admin_id


@dp.message_handler(text='О Friendly Hobot')
async def about_one(message: types.Message):
    id = message.from_user.id
    add_new_log(message.from_user.id, message.from_user.username, 'Аbout FriendlyHobot"')

    await message.answer('Привет! Я сервис, помогающий подбирать нужных людей друг для друга. '
                         'Я еще "молод" - работаю сейчас только в Буэнос-Айресе, гуляю по чатам и собираю людей, '
                         'которые готовы помогать другими, предлагают свои услуги.\n\n'
                         'Если вы такой человек, то обязательно нажимайте на кнопку "Ваши услуги и резюме". '
                         'Я задам несколько вопросов и создам ваш профиль в своей базе, чтобы показывать'
                         'его другим))\n\n'
                         'А если вы чем-то хотите поделиться с моими разрабочикам, напишите! '
                         'Обязательно передам им ваши пожелания и замечания!', reply_markup=feedback)
    if id in admin_id:
        await message.answer('Меню для админа:', reply_markup=admin_buttons)


@dp.callback_query_handler(text='Написать разработчикам')
async def about_two(message: types.Message):
    await bot.send_message(message.from_user.id, text='Напишите ваше пожелания, замечание или комментарий')
    await Feedback.Feedback_send.set()


@dp.message_handler(state=Feedback.Feedback_send)
async def about_three(message: types.Message, state: FSMContext):
    text = message.text
    id = message.from_user.id
    tg_username = message.from_user.username
    await bot.send_message(message.from_user.id, text='Cпасибо! Отправил ваш комментарий разработчикам')

    if tg_username is None:
        await bot.send_message('176221727',
                               text=f'Пользователь с id {id} и без username оставил комментарий:\n\n{text}')
    else:
        await bot.send_message('176221727',
                               text=f'Пользователь с id {id} и username {tg_username} оставил комментарий:\n\n{text}')
    await state.finish()
