from aiogram import types
from loader import dp
from inline_bottons import Specialties


@dp.message_handler(text='Найти специалиста')
async def answer(message: types.Message):
    await message.answer(text='Выберите категорию, в которой вы ищете специалиста', reply_markup=Specialties)
