from loader import dp, bot
from Classes.states_classes import Delete, states_edit_other_list
from aiogram.dispatcher.storage import FSMContext
from aiogram import types
from inline_bottons import yes_no, list_yes_no
from bottons import menu_start
from DB.delete_spec_db import delete_spec
from Intents.show_user_data import take_user_data


data_need = {'id_user': None, 'spec_id': None}


@dp.callback_query_handler(text_startswith='btn_delete', state=states_edit_other_list)
async def delete_other_1(message: types.Message, state: FSMContext):
    text = str(dict(message).get('data'))
    data = text.split('_')
    data_need['spec_id'] = data[2]
    data_need['id_user'] = data[3]
    print('Админ планирует удалить эти данные - ', data_need)
    await bot.send_message(message.from_user.id, text='Вы уверены, что хотите удалить услугу?', reply_markup=yes_no)
    await Delete.Delete_other_spec.set()


@dp.callback_query_handler(text_startswith=list_yes_no, state=Delete.Delete_other_spec)
async def delete_other_2(message: types.Message, state: FSMContext):
    text = str(dict(message).get('data'))

    if text == 'yes':
        delete_spec(id_user=data_need['id_user'], spec_id=data_need['spec_id'])
        await bot.send_message(message.from_user.id, text='Хорошо, такой услуги у юзера больше нет))'
                                                          '\nДавайте посмотрим, что получилось:')
        await take_user_data(data_need['id_user'], message, state)

    else:
        await bot.send_message(message.from_user.id,
                               text='Давайте вернемся в главное меню))\nВыберете, что вас интересует',
                               reply_markup=menu_start)
        await state.finish()
