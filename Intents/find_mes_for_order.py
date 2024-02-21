from aiogram import types
from loader import dp, bot, msg_id
from Classes.states_classes import all_states
from Classes.client_classes import alfa_user
from aiogram.dispatcher.storage import FSMContext
from DB.find_mes_for_user_db import find_mes_for_user_db
from bottons import menu_main


@dp.callback_query_handler(text_startswith='btn_find_orders', state=all_states)
async def find_mes_order1(message: types.Message, state: FSMContext):
    text = str(dict(message).get('data'))
    data = text.split('_')                  # btn_find_orders_{service_id}_{spec_id}_{id_user}
    service_id = data[3]
    spec_id = data[4]
    id_user = data[5]
    print(f'Ask orders for service_id - {service_id}, spec_id - {spec_id} for id_user - {id_user}')

    await alfa_user.delete_dialog(message)

    result_mes = find_mes_for_user_db('need_specialist', spec_id)

    aaa = await bot.send_message(message.from_user.id, text=f'Давайте посмотрим заявки для вашей услуги:',
                                 reply_markup=menu_main)
    msg_id.append(aaa.message_id)

    if not result_mes:
        bbb = await bot.send_message(message.from_user.id,
                                     text='Сообщений в данной тематике нет, попробуйте проверить позже')
        msg_id.append(bbb.message_id)

    else:
        for elements in result_mes:
            link = 'https://t.me/'+elements[11]+'/'+elements[0]
            date = elements[2]
            time = elements[3]
            text = elements[6]
            bbb = await bot.send_message(message.from_user.id, text=f'{date}\n'
                                                                    f'{time}\n'
                                                                    f'{link}\n'
                                                                    f'{text}', disable_web_page_preview=True)
            msg_id.append(bbb.message_id)
