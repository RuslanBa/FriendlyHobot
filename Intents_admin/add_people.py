from aiogram import types
from bottons import menu_main
from loader import dp, bot
from DB.add_log_db import add_new_log
from Classes.states_classes import Other, states_edit_other
from Classes.client_classes import betta_user
from inline_bottons import Specialties, list_specialities, Driver_menu, Food_services_menu, Beauty_menu, Events_menu, \
     Helper_menu, Repair_menu, Equipment_repair_menu, Tutor_menu, Housekeepers_menu, Photo_video_audio_menu, \
     Language_menu, Cities, list_cities, users_identifiers, list_identifiers, Lawyer_menu
from aiogram.dispatcher.storage import FSMContext
from Checks_text.Check_add_username import check_username
from Checks_text.Check_info_about import check_info_about
from Intents_admin.edit_other_func import betta_user_edit


data_speciality = {'spec_name': '-', 'spec_city': '-', 'spec_about': '-', 'tg_username': '-'}


@dp.message_handler(text='Добавить/изменить другого')
async def add_people(message: types.Message):
    add_new_log(message.from_user.id, message.from_user.username, 'add people"')
    await message.answer('Пользователя можно добавить или отредактировать, указав какой-то идентификатор',
                         reply_markup=menu_main)
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
    betta_user.phone = message.text
    print('администратор добавил пользователя с телефоном', betta_user.phone)

    await message.answer(f'Отлично, запомнил телефон - {betta_user.phone}')
    await message.answer('Напишите имя этого человека. Можете добавить фамилию и отчество')
    await Other.Other_name.set()


@dp.message_handler(state=Other.Other_tg)
async def add_people3(message: types.Message, state: FSMContext):
    new_username = message.text
    betta_user.tg_username = check_username(new_username)
    print('администратор добавил пользователя с username @', betta_user.tg_username)

    betta_user.find_id_user_by_tg()
    if betta_user.id_user is not None:
        await message.answer('Человек с таким id уже существует. Вот, что я о нем знаю')
        await Other.Other_change.set()
        await betta_user.show_user_data(message, state)
    else:
        await message.answer(f'Отлично, запомнил Username - @{betta_user.tg_username}')
        await message.answer('Напишите имя этого человека. Можете добавить фамилию и отчество')
        await Other.Other_name.set()


@dp.message_handler(state=Other.Other_name)
async def add_people4(message: types.Message):
    betta_user.name = message.text
    await message.answer(f'Отлично, запомнил имя - {betta_user.name}')

    betta_user.add_to_db()
    print('добавлен пользователь с id ', betta_user.id_user)

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

    elif spec_name == 'Юриcты, переводы, бухгалтерия':
        await bot.send_message(message.from_user.id, 'Выберите подкатегорию', reply_markup=Lawyer_menu)

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

    betta_user.add_user_spec(spec_name=data_speciality['spec_name'],
                             spec_about=data_speciality['spec_about'],
                             spec_city=data_speciality['spec_city'])

    add_new_log(message.from_user.id, message.from_user.username, 'New user_spec added"')

    await bot.send_message(message.from_user.id, 'Давайте посмотрим, что я теперь я знаю об этом человеке')
    await betta_user.show_user_data(message, state)


@dp.message_handler(state=Other.Other_spec_city)
async def add_people8(message: types.Message, state: FSMContext):
    text = message.text
    data_speciality.update({'spec_city': text})

    betta_user.add_user_spec(spec_name=data_speciality['spec_name'],
                             spec_about=data_speciality['spec_about'],
                             spec_city=data_speciality['spec_city'])

    add_new_log(message.from_user.id, message.from_user.username, 'New user_spec added"')

    await message.answer('Давайте посмотрим, что я теперь я знаю об этом человеке')
    await betta_user.show_user_data(message, state)


@dp.message_handler(state=states_edit_other)
async def edit_self(message: types.Message, state: FSMContext):
    mess = message
    await betta_user_edit(mess, state)
