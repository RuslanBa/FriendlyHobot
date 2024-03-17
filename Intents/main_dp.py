from aiogram import types
from aiogram.dispatcher.storage import FSMContext
from Classes.states_classes import all_states, Order
from Classes.client_classes import alfa_user
from inline_bottons import menu_start
from loader import bot, dp
# from Intents.dialog import delete_dialog
from Intents.meeting_user import meetings0


# Переход в главное меню -----------------------------------------------


@dp.message_handler(text='Главное меню')
async def advertising(message: types.Message):
    await alfa_user.add_alfa_user(message, None)
    await alfa_user.delete_dialog(message)
    aaa = await message.answer('Это мое главное меню. Чтобы вы хотели сделать?', reply_markup=menu_start)
    await alfa_user.add_msg_id(message, aaa)


@dp.message_handler(text='Главное меню', state=all_states)
async def go_main(message: types.Message, state: FSMContext):
    await alfa_user.delete_dialog(message)
    aaa = await message.answer('Давайте вернемся в главное меню. Выберите, что вас интересует', reply_markup=menu_start)
    await alfa_user.add_msg_id(message, aaa)
    await state.finish()


# Проверка заказов -----------------------------------------------

@dp.message_handler(text='Мои заявки')
async def my_orders(message: types.Message, state: FSMContext):
    alfa_user.intent = 'мои заказы'
    alfa_user.update_alfa_user(message, alfa_user.intent)

    if alfa_user.name is None or alfa_user.city is None:
        await meetings0(message)

    else:
        await Order.Order_my.set()
        await alfa_user.show_user_orders(message, state)


# Возвращение в главное меню после кнопки не сохранять изменения -----------------------------------------------

@dp.callback_query_handler(text='dont_change', state=all_states)
async def answer7(message: types.Message, state: FSMContext):
    """ 'No' button in menu for user fiedls """
    await alfa_user.delete_dialog(message)
    aaa = await bot.send_message(message.from_user.id, text='Возвращаемся в главное меню',
                                 reply_markup=menu_start)
    await alfa_user.add_msg_id(message, aaa)
    await state.finish()


@dp.callback_query_handler(text='dont_change')
async def answer7(message: types.Message, state: FSMContext):
    """ 'No' button in menu for user fiedls """
    await alfa_user.delete_dialog(message)
    aaa = await bot.send_message(message.from_user.id, text='Возвращаемся в главное меню',
                                 reply_markup=menu_start)
    await alfa_user.add_msg_id(message, aaa)
    await state.finish()
