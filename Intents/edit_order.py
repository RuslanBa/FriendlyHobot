from loader import dp, bot
from aiogram.dispatcher.storage import FSMContext
from aiogram import types
from Classes.states_classes import all_states, Edit
from Classes.order_classes import betta_order
from Classes.client_classes import alfa_user


@dp.callback_query_handler(text_startswith='btn_order_edit', state=all_states)
async def edit_order1(message: types.Message, state: FSMContext):
    text = str(dict(message).get('data'))
    data = text.split('_')      # btn_order_edit_{order_id}_{id_user}
    betta_order.id_user = data[4]
    betta_order.id_order = data[3]
    print('Order for editing - ', data[3])

    await bot.send_message(message.from_user.id, text='Напишите новый текст для заказа')
    await Edit.Edit_order.set()


@dp.message_handler(state=Edit.Edit_order)
async def edit_order2(message: types.Message, state: FSMContext):
    text = message.text
    betta_order.change_betta_order('description', text)

    await message.answer('Итак давайте посмотрим на те заказы, которые у вас есть')
    await alfa_user.show_user_orders(message, state)
