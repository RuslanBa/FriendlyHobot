from aiogram import types
from bottons import menu_main
from loader import dp, bot
from DB.add_log_db import add_new_log
from DB.add_people_db import add_new_people
from DB.check_user_in_db import check_user
from DB.find_id_by_username import find_user_id
from Intents.classes import Other, states_edit_other
from Intents.edit_self import edit_any_user
from inline_bottons import Specialties, list_specialities, Driver_menu, Food_services_menu, Beauty_menu, Events_menu, \
     Helper_menu, Repair_menu, Equipment_repair_menu, Tutor_menu, Housekeepers_menu, Photo_video_audio_menu, \
     Language_menu, Cities, list_cities, users_identifiers, list_identifiers
from Intents.show_user_data import take_user_data
from aiogram.dispatcher.storage import FSMContext
from DB.add_spec_for_people import add_spec
from Checks_text.Check_add_username import check_username
from Checks_text.Check_info_about import check_info_about


new_people = {'name': '-', 'tg_username': '-', 'about': '-', 'country': '-', 'city': '-', 'id_user': '-', 'phone': '-'}

data_speciality = {'spec_name': '-', 'spec_city': '-', 'spec_about': '-', 'tg_username': '-'}


@dp.message_handler(text='Добавить/изменить другого')
async def add_people(message: types.Message):
    add_new_log(message.from_user.id, message.from_user.username, 'add people"')
    await message.answer('Пользователя можно добавить, указав какой-то идентификатор', reply_markup=menu_main)
    await bot.send_message(message.from_user.id, text='Выберите идентификатор для нового пользователя: ',
                           reply_markup=users_identifiers)
    await Other.Other_identifiers.set()


@dp.callback_query_handler(text=list_identifiers, state=Other.Other_identifiers)
async def add_people1(message: types.Message, state: FSMContext):
    ident = str(dict(message).get('data'))

    if ident == 'Telegram id':
        await bot.send_message(message.from_user.id, text='Напишите Username в Telegram этого человека')
        await Other.Other_tg.set()

    else:
        await bot.send_message(message.from_user.id, text='Напишите Телефон этого человека')
        await Other.Other_phone.set()


@dp.message_handler(state=Other.Other_phone)
async def add_people2(message: types.Message, state: FSMContext):
    new_phone = message.text
    print('администратор добавил пользователя с телефоном', new_phone)
    new_people.update({'phone': new_phone})

    await message.answer(f'Отлично, запомнил телефон - {new_phone}')
    await message.answer('Напишите имя этого человека. Можете добавить фамилию и отчество')
    await Other.Other_name.set()


@dp.message_handler(state=Other.Other_tg)
async def add_people3(message: types.Message, state: FSMContext):
    new_username = message.text
    new_username = check_username(new_username)
    print('администратор добавил пользователя с username @', new_username)
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
async def add_people4(message: types.Message):
    name = message.text
    new_people.update({'name': name})
    await message.answer(f'Отлично, запомнил имя - {name}')

    if new_people['tg_username'] != '-':
        new_user_id = add_new_people(name=name,
                                     tg_id='Не указана',
                                     tg_name='Не указана',
                                     tg_surname='Не указано',
                                     tg_username=new_people['tg_username'],
                                     city='Не указан',
                                     phone='Не указан')
    else:
        new_user_id = add_new_people(name=name,
                                     tg_id='Не указана',
                                     tg_name='Не указана',
                                     tg_surname='Не указано',
                                     tg_username='Не указан',
                                     city='Не указан',
                                     phone=new_people['phone'])

    print('добавлен пользователь с id ', new_user_id)
    new_people.update({'id_user': new_user_id})

    await bot.send_message(message.from_user.id, text='Выберите услугу, которую может делать этот человек',
                           reply_markup=Specialties)
    await Other.Other_spec.set()


@dp.callback_query_handler(text=list_specialities, state=Other.Other_spec)
async def add_people5(message: types.Message, state: FSMContext):
    spec_name = str(dict(message).get('data'))

    if spec_name == 'Водители / перевозки / авто':
        await bot.send_message(message.from_user.id, 'Выберите подкатегорию', reply_markup=Driver_menu)

    elif spec_name == 'Доставка и приготовление еды':
        await bot.send_message(message.from_user.id, 'Выберите подкатегорию', reply_markup=Food_services_menu)

    elif spec_name == 'Красота и здоровье':
        await bot.send_message(message.from_user.id, 'Выберите подкатегорию', reply_markup=Beauty_menu)

    elif spec_name == 'Мероприятия':
        await bot.send_message(message.from_user.id, 'Выберите подкатегорию', reply_markup=Events_menu)

    elif spec_name == 'Помощь с детьми и близкими':
        await bot.send_message(message.from_user.id, 'Выберите подкатегорию', reply_markup=Helper_menu)

    elif spec_name == 'Ремонт и строительство':
        await bot.send_message(message.from_user.id, 'Выберите подкатегорию', reply_markup=Repair_menu)

    elif spec_name == 'Ремонт техники':
        await bot.send_message(message.from_user.id, 'Выберите подкатегорию', reply_markup=Equipment_repair_menu)

    elif spec_name == 'Репетиторы и обучение':
        await bot.send_message(message.from_user.id, 'Выберите подкатегорию', reply_markup=Tutor_menu)

    elif spec_name == 'Языки':
        await bot.send_message(message.from_user.id, 'Какой язык вас интересует?', reply_markup=Language_menu)

    elif spec_name == 'Уборка и помощь по хозяйству':
        await bot.send_message(message.from_user.id, 'Выберите подкатегорию', reply_markup=Housekeepers_menu)

    elif spec_name == 'Фото, видео, аудио':
        await bot.send_message(message.from_user.id, 'Выберите подкатегорию', reply_markup=Photo_video_audio_menu)

    else:
        data_speciality.update({'spec_name': spec_name})
        await bot.send_message(message.from_user.id, text=f'Хорошо, запомнил специализацию - {spec_name}')
        await bot.send_message(message.from_user.id, text='Добавьте описание этой услуги')
        await Other.Other_spec_about.set()


@dp.message_handler(state=Other.Other_spec_about)
async def add_people6(message: types.Message, state: FSMContext):
    text = message.text
    text = check_info_about(text)
    print('администратор добавил описание услуги', text)
    data_speciality.update({'spec_about': text})
    await bot.send_message(message.from_user.id, text=f'Запомнил описание услуги - {text}')
    await message.answer('Напишите или выберите город, в котором пользователь может оказывать данную услугу',
                         reply_markup=Cities)
    await Other.Other_spec_city.set()


@dp.callback_query_handler(text=list_cities, state=Other.Other_spec_city)
async def add_people7(message: types.Message, state: FSMContext):
    city_new = str(dict(message).get('data'))
    data_speciality.update({'spec_city': city_new})

    if new_people['tg_username'] != '-':
        add_spec(id_user=new_people['id_user'],
                 spec_name=data_speciality['spec_name'],
                 spec_about=data_speciality['spec_about'],
                 spec_city=data_speciality['spec_city'],
                 tg_username=new_people['tg_username'])
    else:
        add_spec(id_user=new_people['id_user'],
                 spec_name=data_speciality['spec_name'],
                 spec_about=data_speciality['spec_about'],
                 spec_city=data_speciality['spec_city'],
                 tg_username='None')

    add_new_log(message.from_user.id, message.from_user.username, 'New user_spec added"')

    await bot.send_message(message.from_user.id, 'Давайте посмотрим, что я теперь я знаю об этом человеке')
    await take_user_data(new_people['id_user'], message, state)


@dp.message_handler(state=Other.Other_spec_city)
async def add_people8(message: types.Message, state: FSMContext):
    text = message.text
    data_speciality.update({'spec_city': text})

    add_spec(new_people['id_user'], data_speciality['spec_name'], data_speciality['spec_about'],
             data_speciality['spec_city'], new_people['tg_username'])

    add_new_log(message.from_user.id, message.from_user.username, 'New user_spec added"')

    await message.answer('Давайте посмотрим, что я теперь я знаю об этом человеке')
    await take_user_data(new_people['id_user'], message, state)


@dp.message_handler(state=states_edit_other)
async def edit_self(message: types.Message, state: FSMContext):
    mess = message
    await edit_any_user(new_people['id_user'], mess, state)
