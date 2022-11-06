from aiogram.utils import executor
from aiogram.dispatcher.storage import FSMContext
from aiogram import types
from loader import bot, dp
from schedular import scheduler
from bottons import menu_start
from Intents.classes import About_me
from Intents import find_specialists, about_friendlyhobot, about_me
# from DB.add_log_db import add_new_log


@dp.message_handler(commands='Start')
async def start(message: types.Message):
    """ Приветствуем пользователя """

    # add_new_log(message.from_user.id, message.from_user.username, 'Команда старт"')

    await message.answer(text='Привет, давай познакомимся))',
                         reply_markup=menu_start)


@dp.message_handler()
async def answer(message: types.Message):
    print(message.chat.id)
    await message.answer(text=')))')
    # await message.answer(text='Привет, я пока на все сообщения отвечаю этим текстом, '
    #                           'но скоро здесь будет полезная база контактов')


# Переход в главное меню -----------------------------------------------

all_states = [About_me.AB_go, About_me.AB_name, About_me.AB_spec, About_me.AB_price]


@dp.message_handler(text='Главное меню')
async def advertising(message: types.Message):
    await message.answer('Это мое главное меню. Чтобы вы хотели сделать?', reply_markup=menu_start)


@dp.message_handler(text='Главное меню', state=all_states)
async def go_main(message: types.Message, state: FSMContext):
    await message.answer('Давайте вернемся в главное меню. Выберите, что вас интересует', reply_markup=menu_start)
    await state.finish()


# async def on_startup(_):
#     asyncio.create_task(scheduler())


if __name__ == '__main__':
    print('начинаем работу')
    executor.start_polling(dp, skip_updates=True)
    # executor.start_polling(dp, on_startup=on_startup, skip_updates=True)
