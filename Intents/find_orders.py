from aiogram import types
from loader import dp, bot, msg_id
from inline_bottons import yes_no, list_yes_no, Specialties, Cities, list_specialities, list_cities, Driver_menu, \
     Food_services_menu, Beauty_menu, Events_menu, Helper_menu, Repair_menu, Equipment_repair_menu, Tutor_menu, \
     Housekeepers_menu, Photo_video_audio_menu, Language_menu, Lawyer_menu
from bottons import menu_start, menu_main
from aiogram.dispatcher.storage import FSMContext
from Classes.states_classes import About
from Classes.client_classes import alfa_user
from DB.add_log_db import add_new_log
from DB.find_spec_id_by_spec_name import find_spec_id
from Checks_text.Check_info_about import check_info_about
from Intents.meeting_user import meetings0


data_speciality = {'spec_about': None, 'spec_city': None, 'spec_id': None}


@dp.message_handler(text='Найти заказы')
async def answer(message: types.Message, state: FSMContext):
    add_new_log(message.from_user.id, message.from_user.username, 'find orders"')

    alfa_user.intent = 'найти заказы'
    alfa_user.update_alfa_user(message, alfa_user.intent)

    if alfa_user.name is None or alfa_user.city is None:
        await meetings0(message)

    else:
        aaa = await message.answer('Видимо, мы уже знакомы)) Вот, что я о вас знаю', reply_markup=menu_main)
        msg_id.append(aaa.message_id)
        await About.AB_know.set()
        await alfa_user.show_user_data(message, state)


@dp.callback_query_handler(text=list_specialities, state=About.AB_spec)
async def answer3(message: types.Message, state: FSMContext):
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
        spec_id = find_spec_id(spec_name)
        data_speciality.update({'spec_id': spec_id})
        await bot.send_message(message.from_user.id, f'Хорошо, запомнил вашу специализацию - {spec_name}')
        await bot.send_message(message.from_user.id, text='Напишите о своем предложении')
        await About.AB_about.set()


@dp.message_handler(state=About.AB_about)
async def answer4(message: types.Message, state: FSMContext):
    text = message.text
    text_new = check_info_about(text)
    data_speciality.update({'spec_about': text_new})
    await message.answer(f'Запомнил описание вашей услуги - {text}\n'
                         f'Напишите или выберите, в каком городе вы готовы оказывать данную услугу',
                         reply_markup=Cities)
    await About.AB_city.set()


@dp.callback_query_handler(text=list_cities, state=About.AB_city)
async def answer5(message: types.Message, state: FSMContext):
    city_new = str(dict(message).get('data'))
    data_speciality.update({'spec_city': city_new})

    alfa_user.add_user_spec(data_speciality['spec_id'], data_speciality['spec_about'], data_speciality['spec_city'])

    await bot.send_message(message.from_user.id, 'Давайте посмотрим, что я теперь о вас знаю')
    await alfa_user.show_user_data(message, state)


@dp.message_handler(state=About.AB_city)
async def answer6(message: types.Message, state: FSMContext):
    city_new = message.text
    data_speciality.update({'spec_city': city_new})

    alfa_user.add_user_spec(data_speciality['spec_id'], data_speciality['spec_about'], data_speciality['spec_city'])

    await bot.send_message(message.from_user.id, 'Давайте посмотрим, что я теперь о вас знаю')
    await alfa_user.show_user_data(message, state)
