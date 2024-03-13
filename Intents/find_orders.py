from aiogram import types
from loader import dp, bot
# from Intents.dialog import msg_id, delete_dialog
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


@dp.message_handler(text='Найти заказы')
async def answer(message: types.Message, state: FSMContext):
    add_new_log(message.from_user.id, message.from_user.username, 'find orders"')

    await alfa_user.add_alfa_user(message, 'найти заказы')

    if alfa_user.users[message.from_user.id]['name'] is None or alfa_user.users[message.from_user.id]['city'] is None:
        await meetings0(message)

    else:
        aaa = await message.answer('Видимо, мы уже знакомы)) Вот, что я о вас знаю', reply_markup=menu_main)
        await alfa_user.add_msg_id(message, aaa)
        await About.AB_know.set()
        await alfa_user.show_user_data(message, state)


@dp.callback_query_handler(text=list_specialities, state=About.AB_spec)
async def answer3(message: types.Message, state: FSMContext):
    spec_name = str(dict(message).get('data'))
    alfa_user.users[message.from_user.id]['new_spec_name'] = spec_name

    await alfa_user.delete_dialog(message)

    if spec_name == 'Водители / перевозки / авто':
        aaa = await bot.send_message(message.from_user.id, 'Выберите подкатегорию', reply_markup=Driver_menu)
        await alfa_user.add_msg_id(message, aaa)

    elif spec_name == 'Доставка и приготовление еды':
        aaa = await bot.send_message(message.from_user.id, 'Выберите подкатегорию', reply_markup=Food_services_menu)
        await alfa_user.add_msg_id(message, aaa)

    elif spec_name == 'Красота и здоровье':
        aaa = await bot.send_message(message.from_user.id, 'Выберите подкатегорию', reply_markup=Beauty_menu)
        await alfa_user.add_msg_id(message, aaa)

    elif spec_name == 'Мероприятия':
        aaa = await bot.send_message(message.from_user.id, 'Выберите подкатегорию', reply_markup=Events_menu)
        await alfa_user.add_msg_id(message, aaa)

    elif spec_name == 'Помощь с детьми и близкими':
        aaa = await bot.send_message(message.from_user.id, 'Выберите подкатегорию', reply_markup=Helper_menu)
        await alfa_user.add_msg_id(message, aaa)

    elif spec_name == 'Ремонт и строительство':
        aaa = await bot.send_message(message.from_user.id, 'Выберите подкатегорию', reply_markup=Repair_menu)
        await alfa_user.add_msg_id(message, aaa)

    elif spec_name == 'Ремонт техники':
        aaa = await bot.send_message(message.from_user.id, 'Выберите подкатегорию', reply_markup=Equipment_repair_menu)
        await alfa_user.add_msg_id(message, aaa)

    elif spec_name == 'Репетиторы и обучение':
        aaa = await bot.send_message(message.from_user.id, 'Выберите подкатегорию', reply_markup=Tutor_menu)
        await alfa_user.add_msg_id(message, aaa)

    elif spec_name == 'Языки':
        aaa = await bot.send_message(message.from_user.id, 'Какой язык вас интересует?', reply_markup=Language_menu)
        await alfa_user.add_msg_id(message, aaa)

    elif spec_name == 'Уборка и помощь по хозяйству':
        aaa = await bot.send_message(message.from_user.id, 'Выберите подкатегорию', reply_markup=Housekeepers_menu)
        await alfa_user.add_msg_id(message, aaa)

    elif spec_name == 'Фото, видео, аудио':
        aaa = await bot.send_message(message.from_user.id, 'Выберите подкатегорию', reply_markup=Photo_video_audio_menu)
        await alfa_user.add_msg_id(message, aaa)

    elif spec_name == 'Юриcты, переводы, бухгалтерия':
        aaa = await bot.send_message(message.from_user.id, 'Выберите подкатегорию', reply_markup=Lawyer_menu)
        await alfa_user.add_msg_id(message, aaa)

    else:
        spec_id = find_spec_id(spec_name)
        alfa_user.users[message.from_user.id]['new_spec_id'] = spec_id
        await bot.send_message(message.from_user.id, f'Хорошо, запомнил вашу специализацию - {spec_name}')
        await bot.send_message(message.from_user.id, text='Напишите о своем предложении')
        await About.AB_about.set()


@dp.message_handler(state=About.AB_about)
async def answer4(message: types.Message, state: FSMContext):
    text = message.text
    text_new = check_info_about(text)
    alfa_user.users[message.from_user.id]['new_spec_about'] = text_new
    aaa = await message.answer(f'Запомнил описание вашей услуги - {text}\n'
                               f'Напишите или выберите, в каком городе вы готовы оказывать данную услугу',
                               reply_markup=Cities)
    await alfa_user.add_msg_id(message, aaa)
    await About.AB_city.set()


@dp.callback_query_handler(text=list_cities, state=About.AB_city)
async def answer5(message: types.Message, state: FSMContext):
    city_new = str(dict(message).get('data'))
    alfa_user.users[message.from_user.id]['new_spec_city'] = city_new

    await alfa_user.delete_dialog(message)

    alfa_user.add_user_spec(message,
                            alfa_user.users[message.from_user.id]['new_spec_id'],
                            alfa_user.users[message.from_user.id]['new_spec_about'],
                            alfa_user.users[message.from_user.id]['new_spec_city'])

    await bot.send_message(message.from_user.id, 'Давайте посмотрим, что я теперь о вас знаю')
    await alfa_user.show_user_data(message, state)


@dp.message_handler(state=About.AB_city)
async def answer6(message: types.Message, state: FSMContext):
    city_new = message.text
    alfa_user.users[message.from_user.id]['new_spec_city'] = city_new

    await alfa_user.delete_dialog(message)

    alfa_user.add_user_spec(alfa_user.users[message.from_user.id]['new_spec_id'],
                            alfa_user.users[message.from_user.id]['new_spec_about'],
                            alfa_user.users[message.from_user.id]['new_spec_city'])

    await bot.send_message(message.from_user.id, 'Давайте посмотрим, что я теперь о вас знаю')
    await alfa_user.show_user_data(message, state)


@dp.callback_query_handler(text='Назад', state=About.AB_spec)
async def back_order(message: types.Message, state: FSMContext):

    if alfa_user.users[message.from_user.id]['new_spec_name'] is None:
        await alfa_user.delete_dialog(message)
        await bot.send_message(message.from_user.id, text='Давайте вернемся в главное меню))\n'
                                                          'Выберете, что вас интересует', reply_markup=menu_start)
        await state.finish()

    elif alfa_user.users[message.from_user.id]['new_spec_name'] in list_specialities:
        alfa_user.users[message.from_user.id]['new_spec_name'] = None
        await alfa_user.delete_dialog(message)
        aaa = await bot.send_message(message.from_user.id, text='Выберите категорию:', reply_markup=Specialties)
        await alfa_user.add_msg_id(message, aaa)
