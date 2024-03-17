from aiogram.utils import executor
from aiogram import types
from loader import dp, bot
from schedular import scheduler
import Intents
import Intents_admin
from inline_bottons import menu_start
from DB.add_log_db import add_new_log
from Classes.client_classes import alfa_user


@dp.message_handler(commands='Start')
async def start(message: types.Message):
    """ Приветствуем пользователя """
    await alfa_user.add_alfa_user(message, 'Start')
    add_new_log(message.from_user.id, message.from_user.username, 'Command start"')
    aaa = await bot.send_message(message.from_user.id, text='Привет, давай познакомимся))', reply_markup=menu_start)
    await alfa_user.add_msg_id(message, aaa)


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
