from loader import dp, bot, msg_id
from Classes.states_classes import Delete, all_states
from Classes.order_classes import betta_order
from Classes.client_classes import alfa_user
from aiogram.dispatcher.storage import FSMContext
from aiogram import types
from inline_bottons import yes_no, list_yes_no
from bottons import menu_start


@dp.callback_query_handler(text_startswith='btn_order_delete', state=all_states)
async def delete_ord1(message: types.Message, state: FSMContext):
    await alfa_user.delete_dialog(message)
    text = str(dict(message).get('data'))
    data = text.split('_')      # 'btn_order_delete_{order_id}_{id_user}
    betta_order.id_user = data[4]
    betta_order.id_order = data[3]

    for orders in alfa_user.orders:
        if orders['id_order'] == int(data[3]):
            service_need = orders['spec_name']
            now_about = orders['description']

    aaa = await bot.send_message(message.from_user.id, text=f'<b>Услуга в заявке</b> - {service_need}\n'
                                                            f'<b>Текущее описание</b>:\n'
                                                            f'{now_about}\n\n'
                                                            f'Вы уверены, что хотите удалить заявку?',
                                 parse_mode='HTML',
                                 reply_markup=yes_no)
    msg_id.append(aaa.message_id)
    print(f'Order for deleting - {betta_order.id_order} for user - {betta_order.id_user}')
    await Delete.Delete_self_order.set()


@dp.callback_query_handler(text=list_yes_no, state=Delete.Delete_self_order)
async def delete_ord2(message: types.Message, state: FSMContext):
    await alfa_user.delete_dialog(message)
    text = str(dict(message).get('data'))

    if text == 'yes':
        betta_order.delete_betta_order()
        await bot.send_message(message.from_user.id, text='Хорошо, такого заказа больше нет))\n'
                                                          'Давайте посмотрим, какие заказы у вас остались')
        await alfa_user.show_user_orders(message, state)

    else:
        await bot.send_message(message.from_user.id,
                               text='Давайте вернемся в главное меню))\nВыберете, что вас интересует',
                               reply_markup=menu_start)
        await state.finish()
