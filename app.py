import asyncio
import datetime
from aiogram.utils import executor
from aiogram import types
from loader import bot, dp
from schedular import scheduler
from bottons import menu_start


@dp.message_handler(commands='Start')
async def start(message: types.Message):
    """ Приветствуем пользователя """

    await message.answer(text='Привет, давай познакомимся))',
                         reply_markup=menu_start)


@dp.message_handler()
async def answer(message: types.Message):
    print(message.chat.id)
    await message.answer(text='Привет, я пока на все сообщения отвечаю этим текстом, '
                              'но скоро здесь будет полезная база контактов')


async def on_startup(_):
    asyncio.create_task(scheduler())


if __name__ == '__main__':
    print('начинаем работу')
    executor.start_polling(dp, on_startup=on_startup)
