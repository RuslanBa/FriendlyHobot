from loader import dp, bot
# from Intents.dialog import msg_id, delete_dialog
from Classes.states_classes import Delete, all_states
from Classes.order_classes import betta_order
from Classes.client_classes import alfa_user
from aiogram.dispatcher.storage import FSMContext
from aiogram import types
from inline_bottons import yes_no, list_yes_no
from inline_bottons import menu_start


@dp.callback_query_handler(text_startswith='btn_order_delete', state=all_states)
async def delete_ord1(message: types.Message, state: FSMContext):
    await alfa_user.delete_dialog(message)
    text = str(dict(message).get('data'))
    data = text.split('_')      # btn_order_delete_{order_id}_{spec_id}_{id_user}

    await betta_order.add_alfa_order(message)
    betta_order.orders[message.from_user.id]['id_order'] = data[3]
    betta_order.orders[message.from_user.id]['id_user'] = data[5]

    for orders in alfa_user.users[message.from_user.id]['orders']:
        if orders['id_order'] == int(data[3]):
            service_need = orders['spec_name']
            now_about = orders['description']

    aaa = await bot.send_message(message.from_user.id, text=f'<b>Услуга в заявке</b> - {service_need}\n'
                                                            f'<b>Текущее описание</b>:\n'
                                                            f'{now_about}\n\n'
                                                            f'Вы уверены, что хотите удалить заявку?',
                                 parse_mode='HTML',
                                 reply_markup=yes_no)
    await alfa_user.add_msg_id(message, aaa)
    print(f'Order for deleting - {betta_order.orders[message.from_user.id]["id_order"]} '
          f'for user - {betta_order.orders[message.from_user.id]["id_user"]}')
    await Delete.Delete_self_order.set()


@dp.callback_query_handler(text=list_yes_no, state=Delete.Delete_self_order)
async def delete_ord2(message: types.Message, state: FSMContext):
    await alfa_user.delete_dialog(message)
    text = str(dict(message).get('data'))

    if text == 'yes':
        betta_order.delete_betta_order(message)
        await alfa_user.show_user_orders(message, state)

    else:
        aaa = await bot.send_message(message.from_user.id,
                                     text='Давайте вернемся в главное меню))\nВыберете, что вас интересует',
                                     reply_markup=menu_start)
        await alfa_user.add_msg_id(message, aaa)
        await state.finish()
