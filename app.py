import asyncio
from aiogram.utils import executor
from aiogram import types
from loader import bot, dp
from schedular import scheduler_monday, scheduler_thursday


@dp.message_handler()
async def answer(message: types.Message):
    await message.answer(text='Привет, я пока на все сообщения отвечаю этим текстом, '
                              'но скоро здесь будет полезная база контактов')


async def on_startup(_):
    asyncio.create_task(scheduler_monday())
    asyncio.create_task(scheduler_thursday())


if __name__ == '__main__':
    print('начинаем работу')
    executor.start_polling(dp, on_startup=on_startup)
