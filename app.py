import asyncio
from aiogram import types
from aiogram.utils import executor
from loader import bot, dp
from schedular import scheduler_monday, scheduler_thursday


async def on_startup(_):
    asyncio.create_task(scheduler_monday())
    asyncio.create_task(scheduler_thursday())


if __name__ == '__main__':
    host = '0.0.0.0'
    print('начинаем работу')
    executor.start_polling(dp, on_startup=on_startup)
