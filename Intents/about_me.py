from aiogram import types
from loader import dp
from inline_bottons import yes_no


@dp.message_handler(text='Рассказать о себе')
async def answer(message: types.Message):
    await message.answer(text='Давайте познакомимся поближе)) '
                              'Мне нужно задать вам несколько вопросов, чтобы я мог рассказать о вас. '
                              'После вопросов я покажу, как будет выглядеть информация о вас для других людей. '
                              'Вы всегда сможете ее скорректировать. Поехали?', reply_markup=yes_no)
