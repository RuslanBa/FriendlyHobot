from loader import dp, bot
from Classes.states_classes import Delete, states_edit_self_list
from Classes.client_classes import alfa_user
from aiogram.dispatcher.storage import FSMContext
from aiogram import types
from inline_bottons import yes_no, list_yes_no
from bottons import menu_start
from DB.find_id_by_username import find_user_id
from Intents.OLD_show_user_data import take_user_data
from DB.delete_spec_db import delete_spec


spec_delete = []


@dp.callback_query_handler(text_startswith='btn_delete', state=states_edit_self_list)
async def delete1(message: types.Message, state: FSMContext):
    text = str(dict(message).get('data'))
    data = text.split('_')
    find_id = data[2]
    spec_delete.append(find_id)
    print('Услуга к удалению - ', spec_delete)
    await bot.send_message(message.from_user.id, text='Вы уверены, что хотите удалить услугу?', reply_markup=yes_no)
    await Delete.Delete_self_spec.set()


@dp.callback_query_handler(text=list_yes_no, state=Delete.Delete_self_spec)
async def delete2(message: types.Message, state: FSMContext):
    text = str(dict(message).get('data'))

    if text == 'yes':
        tg_username = str(message.from_user.username)
        need_id = find_user_id(tg_username)
        delete_spec(need_id, spec_id=spec_delete[0])
        spec_delete.clear()
        await bot.send_message(message.from_user.id, text='Хорошо, такой услуги в вашем портфолио больше нет))'
                                                          '\nДавайте посмотрим, что я теперь знаю о вас')
        await alfa_user.show_user_data(message, state)

    else:
        await bot.send_message(message.from_user.id,
                               text='Давайте вернемся в главное меню))\nВыберете, что вас интересует',
                               reply_markup=menu_start)
        await state.finish()
