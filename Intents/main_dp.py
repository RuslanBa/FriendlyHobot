from aiogram import types
from aiogram.dispatcher.storage import FSMContext
from Intents.classes import all_states
from bottons import menu_start, menu_main
from loader import bot, dp


# Переход в главное меню -----------------------------------------------


@dp.message_handler(text='Главное меню')
async def advertising(message: types.Message):
    await message.answer('Это мое главное меню. Чтобы вы хотели сделать?', reply_markup=menu_start)


@dp.message_handler(text='Главное меню', state=all_states)
async def go_main(message: types.Message, state: FSMContext):
    await message.answer('Давайте вернемся в главное меню. Выберите, что вас интересует', reply_markup=menu_start)
    await state.finish()


@dp.callback_query_handler(text='dont_change', state=all_states)
async def answer7(message: types.Message, state: FSMContext):
    """ 'No' button in menu for user fiedls """
    await bot.send_message(message.from_user.id, text='Отлично! Возвращаемся в главное меню',
                           reply_markup=menu_start)
    await state.finish()
