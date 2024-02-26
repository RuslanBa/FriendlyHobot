from loader import dp, bot, msg_id
from aiogram.dispatcher.storage import FSMContext
from aiogram import types
from Classes.states_classes import all_states, Edit
from Classes.order_classes import betta_order
from Classes.client_classes import alfa_user
from bottons import menu_main


@dp.callback_query_handler(text_startswith='btn_order_edit', state=all_states)
async def edit_order1(message: types.Message, state: FSMContext):
    await alfa_user.delete_dialog(message)
    text = str(dict(message).get('data'))
    data = text.split('_')      # btn_order_edit_{order_id}_{id_user}
    betta_order.id_user = data[4]
    betta_order.id_order = data[3]
    print('Order for editing - ', data[3])

    for orders in alfa_user.orders:
        if orders['id_order'] == int(data[3]):
            service_need = orders['spec_name']
            now_about = orders['description']

    aaa = await bot.send_message(message.from_user.id, text=f'<b>Услуга в заявке</b> - {service_need}\n'
                                                            f'<b>Текущее описание</b>:\n'
                                                            f'{now_about}\n\n'
                                                            f'Напишите новый текст для услуги',
                                 parse_mode='HTML',
                                 reply_markup=menu_main)
    msg_id.append(aaa.message_id)
    await Edit.Edit_order.set()


@dp.message_handler(state=Edit.Edit_order)
async def edit_order2(message: types.Message, state: FSMContext):
    await alfa_user.delete_dialog(message)
    text = message.text
    betta_order.change_betta_order('description', text)

    await message.answer('Итак давайте посмотрим на те заказы, которые у вас есть')
    await alfa_user.show_user_orders(message, state)
