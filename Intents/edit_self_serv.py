from loader import dp, bot
from Classes.states_classes import all_states, Edit
from Classes.client_classes import alfa_user
from aiogram.dispatcher.storage import FSMContext
from aiogram import types
from DB.edit_spec_db import edit_spec
from Checks_text.Check_info_about import check_info_about
from bottons import menu_main
# from Intents.dialog import msg_id, delete_dialog


data_need = {'service_id': None, 'spec_name': None, 'about': None}


@dp.callback_query_handler(text_startswith='btn_edit', state=all_states)
async def edit_serv1(message: types.Message, state: FSMContext):
    text = str(dict(message).get('data'))
    data = text.split('_')              # btn_edit_{service_id}_{spec_id}_{id_user}
    print(data)
    data_need['service_id'] = data[2]
    print('Услуга к редактированию - ', data[2])

    await alfa_user.delete_dialog(message)

    print(alfa_user.services)

    for services in alfa_user.services:
        print(services)
        if services['service_id'] == int(data[2]):
            data_need['spec_name'] = services['spec_name']
            data_need['about'] = services['about']

    await bot.send_message(message.from_user.id, text=f'<b>Услуга</b> - {data_need["spec_name"]}\n'
                                                      f'<b>Текущее описние</b>:\n'
                                                      f'{data_need["about"]}\n\n'
                                                      f'Напишите новый текст для услуги',
                           parse_mode='HTML',
                           reply_markup=menu_main)
    await Edit.Edit_spec_about.set()
    current_state = await state.get_state()
    print('state =', current_state)


@dp.message_handler(state=Edit.Edit_spec_about)
async def edit_serv2(message: types.Message, state: FSMContext):
    text = str(message.text)
    text = check_info_about(text)

    print(f'Task for change {data_need}')
    edit_spec(alfa_user.id_user, data_need['service_id'], text)

    await bot.send_message(message.from_user.id, text='Отлично, текст я заменил'
                                                      '\nДавайте посмотрим, что я теперь знаю:')
    await alfa_user.show_user_data(message, state)
