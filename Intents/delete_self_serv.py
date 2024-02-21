from loader import dp, bot, msg_id
from Classes.states_classes import Delete, states_edit_self_list
from Classes.client_classes import alfa_user
from aiogram.dispatcher.storage import FSMContext
from aiogram import types
from inline_bottons import yes_no, list_yes_no
from bottons import menu_start
from DB.find_id_by_username import find_user_id
from DB.find_spec_by_id import find_speciality
from Intents.OLD_show_user_data import take_user_data
from DB.delete_spec_db import delete_spec


service_delete = []


@dp.callback_query_handler(text_startswith='btn_delete', state=states_edit_self_list)
async def delete1(message: types.Message, state: FSMContext):
    text = str(dict(message).get('data'))
    data = text.split('_')             # btn_delete_{service_id}_{spec_id}_{id_user}
    service_id = data[2]
    service_delete.append(service_id)
    spec_id = data[3]
    data_spec = find_speciality(int(spec_id))
    spec_name = data_spec[2]
    print('Услуга к удалению - ', spec_name)

    await alfa_user.delete_dialog(message)

    aaa = await bot.send_message(message.from_user.id, text=f'Вы уверены, что хотите удалить услугу "{spec_name}"?',
                                 reply_markup=yes_no)
    msg_id.append(aaa.message_id)

    await Delete.Delete_self_spec.set()


@dp.callback_query_handler(text=list_yes_no, state=Delete.Delete_self_spec)
async def delete2(message: types.Message, state: FSMContext):
    text = str(dict(message).get('data'))

    await alfa_user.delete_dialog(message)

    if text == 'yes':
        delete_spec(alfa_user.id_user, spec_id=service_delete[0])
        service_delete.clear()
        await bot.send_message(message.from_user.id, text='Хорошо, такой услуги в вашем портфолио больше нет))'
                                                          '\nДавайте посмотрим, что я теперь знаю о вас')
        await alfa_user.show_user_data(message, state)

    else:
        await bot.send_message(message.from_user.id,
                               text='Давайте вернемся в главное меню))\nВыберете, что вас интересует',
                               reply_markup=menu_start)
        await state.finish()
