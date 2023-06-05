from aiogram import types
from loader import dp, bot
from inline_bottons import yes_no, list_yes_no, Specialties, list_specialities
from bottons import menu_start, menu_main
from aiogram.dispatcher.storage import FSMContext
from Intents.classes import About
from DB.add_people_db import add_new_people
from DB.add_log_db import add_new_log
from DB.add_spec_for_people import add_spec
from DB.check_user_in_db import check_user
from DB.find_id_by_username import find_user_id
from Intents.show_user_data import take_user_data


data_people = {'name': '-', 'tg_id': '-', 'tg_name': '-', 'tg_surname': '-', 'tg_username': '-',
               'about': '-', 'country': '-', 'city': '-', 'id_user': '-'}

data_speciality = {'spec_name': None, 'spec_about': None, 'spec_city': None, 'tg_username': None}


@dp.message_handler(text='Ваши услуги и резюме')
async def answer(message: types.Message, state: FSMContext):
    tg_username = str(message.from_user.username)

    add_new_log(message.from_user.id, message.from_user.username, 'Аbout yourself"')

    if check_user(tg_username) > 0:
        await message.answer('Видимо, мы уже знакомы)) Вот, что я о вас знаю', reply_markup=menu_main)
        await About.AB_know.set()
        await take_user_data(tg_username, message, state)
        need_id = find_user_id(tg_username)
        data_people.update({'id_user': need_id})

    else:
        await message.answer(text='Давайте познакомимся поближе))', reply_markup=menu_main)
        await message.answer(text='Мне нужно задать вам несколько вопросов, чтобы я мог рассказать о вас. '
                                  'После вопросов я покажу, как будет выглядеть информация о вас для других людей. '
                                  'Вы всегда сможете ее скорректировать. Поехали?', reply_markup=yes_no)
        await About.AB_go.set()


@dp.callback_query_handler(text=list_yes_no, state=About.AB_go)
async def answer1(message: types.Message, state: FSMContext):
    text = str(dict(message).get('data'))

    if text == 'yes':
        await bot.send_message(message.from_user.id, text='Как вас зовут? Вы можете написать как только имя, так и '
                                                          'добавить к нему фамилию или отчество. Их будут видеть '
                                                          'другие люди')
        await About.AB_name.set()
    else:
        await bot.send_message(message.from_user.id, text='Давайте вернемся в главное меню))\n'
                                                          'Выберете, что вас интересует', reply_markup=menu_start)
        await state.finish()


@dp.message_handler(state=About.AB_name)
async def answer2(message: types.Message, state: FSMContext):
    name_new = message.text
    tg_id_new = message.from_user.id
    tg_name_new = message.from_user.first_name
    tg_surname_new = message.from_user.last_name
    tg_username_new = message.from_user.username
    data_people.update({'name': name_new, 'tg_id': tg_id_new, 'tg_name': tg_name_new, 'tg_surname': tg_surname_new,
                        'tg_username': tg_username_new, 'country': 'Страна не указана', 'city': 'Город не указан'})

    new_user_id = add_new_people(name_new, tg_id_new, tg_name_new, tg_surname_new, tg_username_new, 'Алания')
    print('добавлен пользователь с id ', new_user_id)
    data_people.update({'id_user': new_user_id})

    await message.answer(f'Отлично, запомнил ваше имя - {name_new}')
    await bot.send_message(message.from_user.id,
                           text='В какой категории услуг вы можете быть полезным другим людям?',
                           reply_markup=Specialties)
    await About.AB_spec.set()


@dp.callback_query_handler(text=list_specialities, state=About.AB_spec)
async def answer3(message: types.Message, state: FSMContext):
    spec_name_new = str(dict(message).get('data'))
    data_speciality.update({'spec_name': spec_name_new})

    await bot.send_message(message.from_user.id,
                           f'Хорошо, запомнил вашу специализацию - {spec_name_new}')
    await bot.send_message(message.from_user.id,
                           text='Напишите о своем предложении')
    await About.AB_about.set()


@dp.message_handler(state=About.AB_about)
async def answer4(message: types.Message, state: FSMContext):
    text = message.text
    data_speciality.update({'spec_about': text})
    await message.answer(f'Запомнил описание вашей услуги - {text}\n'
                         f'Напишите в каком городе вы готовы оказывать данную услугу')
    await About.AB_city.set()


@dp.message_handler(state=About.AB_city)
async def answer5(message: types.Message, state: FSMContext):
    text = message.text
    tg_username = str(message.from_user.username)
    data_speciality.update({'spec_city': text})

    add_spec(data_people['id_user'], data_speciality['spec_name'], data_speciality['spec_about'],
             data_speciality['spec_city'], tg_username)

    add_new_log(message.from_user.id, message.from_user.username, 'All questions done"')

    await message.answer('Давайте посмотрим, что я теперь о вас знаю')
    await take_user_data(tg_username, message, state)
