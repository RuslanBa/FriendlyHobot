from aiogram import types
from loader import dp
from inline_bottons import Specialties


@dp.message_handler(text='О Friendly Hobot')
async def answer(message: types.Message):
    await message.answer(text='Привет! Я, начинающий бот и хочу научиться подбирать нужных людей друг для друга. '
                              'Я еще "молод" - работаю сейчас только в Алании, гуляю по чатам и собираю людей, '
                              'которые готовы помогать другими, предлагают свои услуги.\n\n'
                              'Если вы такой человек, то обязательно нажимайте на кнопку "Рассказать о себе". '
                              'Я задам несколько вопросов и пойму, как вы можете быть полезны другим))')
