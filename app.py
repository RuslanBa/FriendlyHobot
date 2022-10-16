from flask import Flask
import asyncio
from aiogram.utils import executor
from aiogram import types
from loader import bot, dp
from schedular import scheduler_monday, scheduler_thursday


# app = Flask(__name__)
#
#
# @app.route('/')
# def hello_world():
#     return 'Hello'
#

@dp.message_handler()
async def answer(message: types.Message):
    await message.answer(text='Привет')


async def on_startup(_):
    asyncio.create_task(scheduler_monday())
    asyncio.create_task(scheduler_thursday())


if __name__ == '__main__':
    print('начинаем работу')
    port = '0.0.0.0:8080'
    executor.start_polling(dp, on_startup=on_startup)
