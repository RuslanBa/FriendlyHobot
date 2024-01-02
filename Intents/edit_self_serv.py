from loader import dp, bot
from Classes.states_classes import all_states, Edit
from aiogram.dispatcher.storage import FSMContext
from aiogram import types
from Intents.show_user_data import take_user_data
from DB.edit_spec_db import edit_spec
from Checks_text.Check_info_about import check_info_about


data_need = {'id_user': None, 'spec_id': None}


@dp.callback_query_handler(text_startswith='btn_edit', state=all_states)
async def edit_serv1(message: types.Message, state: FSMContext):
    text = str(dict(message).get('data'))
    data = text.split('_')
    print(data)
    data_need['id_user'] = data[3]
    data_need['spec_id'] = data[2]
    print('Услуга к редактированию - ', data[2])
    await bot.send_message(message.from_user.id, text='Напишите новый текст для услуги')
    await Edit.Edit_spec_about.set()
    current_state = await state.get_state()
    print('state =', current_state)


@dp.message_handler(state=Edit.Edit_spec_about)
async def edit_serv2(message: types.Message, state: FSMContext):
    text = str(message.text)
    text = check_info_about(text)

    print(f'Task for change {data_need}')
    edit_spec(data_need['id_user'], data_need['spec_id'], text)

    await bot.send_message(message.from_user.id, text='Отлично, текст я заменил'
                                                      '\nДавайте посмотрим, что я теперь знаю:')
    await take_user_data(data_need['id_user'], message, state)
