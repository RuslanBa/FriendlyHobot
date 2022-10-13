from flask import Flask
import asyncio
from aiogram.utils import executor
from loader import bot, dp
from schedular import scheduler_monday, scheduler_thursday


app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello'


async def on_startup(_):
    asyncio.create_task(scheduler_monday())
    asyncio.create_task(scheduler_thursday())


if __name__ == '__main__':
    print('начинаем работу')
    executor.start_polling(dp, on_startup=on_startup)
