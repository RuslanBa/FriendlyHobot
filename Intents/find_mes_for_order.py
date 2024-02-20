from aiogram import types
from loader import dp, bot
from Classes.states_classes import all_states
from aiogram.dispatcher.storage import FSMContext
from DB.find_mes_for_user_db import find_mes_for_user_db


@dp.callback_query_handler(text_startswith='btn_find_orders', state=all_states)
async def find_mes_order1(message: types.Message, state: FSMContext):
    text = str(dict(message).get('data'))
    data = text.split('_')                  # btn_find_orders_{service_id}_{spec_id}_{id_user}
    service_id = data[3]
    spec_id = data[4]
    id_user = data[5]
    print(f'Ask orders for service_id - {service_id}, spec_id - {spec_id} for id_user - {id_user}')

    result_mes = find_mes_for_user_db('need_specialist', spec_id)

    await bot.send_message(message.from_user.id, text=result_mes)
