from aiogram import types
from bottons import menu_main
from loader import dp, bot
from DB.add_log_db import add_new_log
from DB.add_people_db import add_new_people
from DB.check_user_in_db import check_user
from DB.find_id_by_username import find_user_id
from Intents.classes import Other, states_edit_other
from Intents.edit_self import edit_any_user
from inline_bottons import Specialties, list_specialities
from Intents.show_user_data import take_user_data
from aiogram.dispatcher.storage import FSMContext
from DB.add_spec_for_people import add_spec


new_people = {'name': '-', 'tg_username': '-', 'about': '-', 'country': '-', 'city': '-', 'id_user': '-'}

data_speciality = {'spec_name': '-', 'spec_about': '-', 'tg_username': '-'}


@dp.message_handler(text='Добавить/изменить другого')
async def add_people(message: types.Message):
    add_new_log(message.from_user.id, message.from_user.username, 'add people"')
    await bot.send_message(message.from_user.id, text='Напишите Username в Telegram этого человека',
                           reply_markup=menu_main)
    await Other.Other_tg.set()


@dp.message_handler(state=Other.Other_tg)
async def add_people2(message: types.Message, state: FSMContext):
    new_username = message.text
    new_people.update({'tg_username': new_username})

    if check_user(new_username) > 0:
        await message.answer('Человек с таким id уже существует. Вот, что я о нем знаю')
        await Other.Other_change.set()
        await take_user_data(new_username, message, state)  # Go to edit_self
        need_id = find_user_id(new_username)
        new_people.update({'id_user': need_id})

    else:
        await message.answer(f'Отлично, запомнил Username - @{new_username}')
        await message.answer('Напишите имя этого человека. Можете добавить фамилию и отчество')
        await Other.Other_name.set()


@dp.message_handler(state=Other.Other_name)
async def add_people3(message: types.Message):
    name = message.text
    new_people.update({'name': name})
    await message.answer(f'Отлично, запомнил имя - {name}')

    new_user_id = add_new_people(name, 'None', 'None', 'None', new_people['tg_username'], 'Алания')
    print('добавлен пользователь с id ', new_user_id)
    new_people.update({'id_user': new_user_id})

    await bot.send_message(message.from_user.id, text='Выберите услугу, которую может делать этот человек',
                           reply_markup=Specialties)
    await Other.Other_spec.set()


@dp.callback_query_handler(text=list_specialities, state=Other.Other_spec)
async def add_people4(message: types.Message, state: FSMContext):
    spec_name_new = str(dict(message).get('data'))
    data_speciality.update({'spec_name': spec_name_new})
    await bot.send_message(message.from_user.id, text=f'Хорошо, запомнил специализацию - {spec_name_new}')
    await bot.send_message(message.from_user.id, text='Добавьте описание этой услуги')
    await Other.Other_spec_about.set()


@dp.message_handler(state=Other.Other_spec_about)
async def add_people5(message: types.Message, state: FSMContext):
    text = message.text
    data_speciality.update({'spec_about': text})

    add_spec(new_people['id_user'], data_speciality['spec_name'], text, new_people['tg_username'])

    add_new_log(message.from_user.id, message.from_user.username, 'New user_spec added"')

    await message.answer('Давайте посмотрим, что я теперь я знаю об этом человеке')
    await take_user_data(new_people['tg_username'], message, state)


@dp.message_handler(state=states_edit_other)
async def edit_self(message: types.Message, state: FSMContext):
    mess = message
    await edit_any_user(new_people['tg_username'], mess, state)
