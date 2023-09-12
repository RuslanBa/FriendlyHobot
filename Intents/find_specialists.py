from aiogram import types
from loader import dp, bot
from bottons import menu_main, menu_start
from DB.add_log_db import add_new_log
from DB.find_specialists_db import find_masters
from DB.find_people_by_id import find_people
from DB.find_quan_people_by_city import find_people_by_city
from Intents.classes import Find
from inline_bottons import Specialties, Cities, list_specialities, list_cities, Driver_menu, Food_services_menu, \
     Beauty_menu, Events_menu, Helper_menu, Repair_menu, Equipment_repair_menu, Tutor_menu, Housekeepers_menu, \
     Photo_video_audio_menu, Language_menu
from aiogram.dispatcher.storage import FSMContext


data_masters = {'city': None, 'spec_name': None}


@dp.message_handler(text='Найти исполнителя')
async def answer(message: types.Message):
    add_new_log(message.from_user.id, message.from_user.username, 'find specialist"')
    await message.answer(text='Давайте подберем того, кто сможет вам помочь', reply_markup=menu_main)
    await message.answer(text='В каком городе вы ищете исполнителя? (пока я могу поискать только ним)',
                         reply_markup=Cities)
    await Find.Find_city.set()


@dp.message_handler(state=Find.Find_city)
async def answer1(message: types.Message):
    add_new_log(message.from_user.id, message.from_user.username, 'find specialist"')
    city = message.text
    data_masters.update({'city': city})
    number = find_people_by_city(city)
    await bot.send_message(message.from_user.id,
                           f'Отлично! В городе {city} в моей базе зарергистрировано {number} предложений от разных '
                           f'специалистов. '
                           f'\nВыберите категорию:', reply_markup=Specialties)
    await Find.Find_spec.set()


@dp.callback_query_handler(text=list_cities, state=Find.Find_city)
async def answer2(message: types.Message):
    city = str(dict(message).get('data'))
    data_masters.update({'city': city})
    number = find_people_by_city(city)
    await bot.send_message(message.from_user.id,
                           f'Отлично! В городе {city} в моей базе зарергистрировано {number} предложений от разных '
                           f'специалистов. '
                           f'\nВыберите категорию:', reply_markup=Specialties)
    await Find.Find_spec.set()


@dp.callback_query_handler(text=list_specialities, state=Find.Find_spec)
async def answer3(message: types.Message, state: FSMContext):
    spec_name = str(dict(message).get('data'))

    print('spec_name=', spec_name)

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
        await show_specialists_by_filter(spec_name, state, message)


async def show_specialists_by_filter(spec_name, state: FSMContext, message):

    data_masters.update({'spec_name': spec_name})
    print('Пользователь ищет - ', data_masters)

    base_data = find_masters(data_masters['city'], data_masters['spec_name'])
    print('these people was found -', base_data)

    if base_data[0] == 'n':
        await bot.send_message(message.from_user.id, text='Никого не нашел. Попробуйте позже. '
                                                          'Возвращаемся в главное меню', reply_markup=menu_start)

    else:
        for item in base_data:
            id_user = int(item[0])
            spec_name = item[1]
            spec_about = item[4]
            user_data = find_people(id_user)
            name = user_data[0]
            tg_username = user_data[4]
            about = user_data[5]
            archetype = user_data[6]
            city = user_data[7]
            birthdate = user_data[8]
            country = user_data[10]
            phone = user_data[11]

            await bot.send_message(message.from_user.id, text=f'<b>Имя</b> - {name}\n'
                                                              f'<b>Cтрана</b> - {country}\n'
                                                              f'<b>Город</b> - {city}\n'
                                                              f'<b>О специалисте</b> - {about}\n'
                                                              f'<b>Услуга</b> - {spec_name}\n'
                                                              f'<b>Описание услуги</b>:\n{spec_about}\n'
                                                              f'<b>Телефон</b>:{phone}\n'
                                                              f'<b>Написать специалисту</b> - @{tg_username}',
                                   parse_mode="HTML")
    await state.finish()
