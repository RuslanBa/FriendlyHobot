from aiogram.utils import executor
from aiogram import types
from loader import dp
from schedular import scheduler
import Intents
import Intents_admin
from bottons import menu_start
from DB.add_log_db import add_new_log


@dp.message_handler(commands='Start')
async def start(message: types.Message):
    """ Приветствуем пользователя """
    add_new_log(message.from_user.id, message.from_user.username, 'Command start"')
    await message.answer(text='Привет, давай познакомимся))', reply_markup=menu_start)


@dp.message_handler()
async def answer(message: types.Message):
    print(message.chat.id)
    await message.answer(text=')))')


# async def on_startup(_):
#     asyncio.create_task(scheduler())


if __name__ == '__main__':
    print('начинаем работу')
    executor.start_polling(dp, skip_updates=True)
    # executor.start_polling(dp, on_startup=on_startup, skip_updates=True)
