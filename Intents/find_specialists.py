from aiogram import types
from loader import dp, bot
from bottons import menu_main, menu_start
from DB.add_log_db import add_new_log
from DB.find_specialists_db import find_masters
from DB.find_people_by_id import find_people
from DB.find_quan_people_by_city import find_people_by_city
from classes import Find
from inline_bottons import Specialties, Cities, list_specialities, list_cities, Driver_menu, Food_services_menu, \
     Beauty_menu, Events_menu, Helper_menu, Repair_menu, Equipment_repair_menu, Tutor_menu, Housekeepers_menu, \
     Photo_video_audio_menu, Language_menu, Lawyer_menu
from aiogram.dispatcher.storage import FSMContext
from Intents.show_catalog import show_specialists_by_filter
from Intents_admin.show_catalog_admin import catalog_for_admin
from loader import admin_id


data_masters = {'user': None, 'city': None, 'spec_name': None}
msg_id = []


@dp.message_handler(text='Найти исполнителя')
async def answer(message: types.Message):
    add_new_log(message.from_user.id, message.from_user.username, 'find specialist"')
    await message.answer(text='Давайте подберем того, кто сможет вам помочь', reply_markup=menu_main)
    aaa = await message.answer(text='В каком городе вы ищете исполнителя?',
                               reply_markup=Cities)

    msg_id.clear()
    msg_id.append(aaa.message_id)

    await Find.Find_city.set()


@dp.message_handler(text='Редактировать в каталоге')
async def answer_adm(message: types.Message):
    add_new_log(message.from_user.id, message.from_user.username, 'find specialist"')
    id = message.from_user.id
    if id in admin_id:
        data_masters.update({'user': 'admin'})
    await message.answer(text='Давайте подберем того, кто сможет вам помочь', reply_markup=menu_main)
    aaa = await message.answer(text='В каком городе вы ищете исполнителя?', reply_markup=Cities)

    msg_id.clear()
    msg_id.append(aaa.message_id)

    await Find.Find_city.set()


@dp.message_handler(state=Find.Find_city)
async def answer1(message: types.Message):
    add_new_log(message.from_user.id, message.from_user.username, 'find specialist"')
    city = message.text
    data_masters.update({'city': city})
    number = find_people_by_city(city)

    await bot.delete_message(message.from_user.id, message_id=int(msg_id[0]))
    msg_id.clear()

    aaa = await bot.send_message(message.from_user.id,
                           f'Отлично! В городе {city} в моей базе зарергистрировано {number} предложений от разных '
                           f'специалистов. '
                           f'\nВыберите категорию:', reply_markup=Specialties)
    msg_id.append(aaa.message_id)

    await Find.Find_spec.set()


@dp.callback_query_handler(text=list_cities, state=Find.Find_city)
async def answer2(message: types.Message):
    city = str(dict(message).get('data'))
    data_masters.update({'city': city})
    number = find_people_by_city(city)

    await bot.delete_message(message.from_user.id, message_id=int(msg_id[0]))
    msg_id.clear()

    aaa = await bot.send_message(message.from_user.id,
                           f'Отлично! В городе {city} в моей базе зарергистрировано {number} предложений от разных '
                           f'специалистов. '
                           f'\nВыберите категорию:', reply_markup=Specialties)
    msg_id.append(aaa.message_id)

    await Find.Find_spec.set()


@dp.callback_query_handler(text=list_specialities, state=Find.Find_spec)
async def answer3(message: types.Message, state: FSMContext):
    spec_name = str(dict(message).get('data'))

    print('spec_name=', spec_name)

    if msg_id:
        await bot.delete_message(message.from_user.id, message_id=int(msg_id[0]))
        msg_id.clear()

    if spec_name == 'Водители / перевозки / авто':
        aaa = await bot.send_message(message.from_user.id, 'Выберите подкатегорию', reply_markup=Driver_menu)
        msg_id.append(aaa.message_id)

    elif spec_name == 'Доставка и приготовление еды':
        aaa = await bot.send_message(message.from_user.id, 'Выберите подкатегорию', reply_markup=Food_services_menu)
        msg_id.append(aaa.message_id)

    elif spec_name == 'Красота и здоровье':
        aaa = await bot.send_message(message.from_user.id, 'Выберите подкатегорию', reply_markup=Beauty_menu)
        msg_id.append(aaa.message_id)

    elif spec_name == 'Мероприятия':
        aaa = await bot.send_message(message.from_user.id, 'Выберите подкатегорию', reply_markup=Events_menu)
        msg_id.append(aaa.message_id)

    elif spec_name == 'Помощь с детьми и близкими':
        aaa = await bot.send_message(message.from_user.id, 'Выберите подкатегорию', reply_markup=Helper_menu)
        msg_id.append(aaa.message_id)

    elif spec_name == 'Ремонт и строительство':
        aaa = await bot.send_message(message.from_user.id, 'Выберите подкатегорию', reply_markup=Repair_menu)
        msg_id.append(aaa.message_id)

    elif spec_name == 'Ремонт техники':
        aaa = await bot.send_message(message.from_user.id, 'Выберите подкатегорию', reply_markup=Equipment_repair_menu)
        msg_id.append(aaa.message_id)

    elif spec_name == 'Репетиторы и обучение':
        aaa = await bot.send_message(message.from_user.id, 'Выберите подкатегорию', reply_markup=Tutor_menu)
        msg_id.append(aaa.message_id)

    elif spec_name == 'Языки':
        aaa = await bot.send_message(message.from_user.id, 'Какой язык вас интересует?', reply_markup=Language_menu)
        msg_id.append(aaa.message_id)

    elif spec_name == 'Уборка и помощь по хозяйству':
        aaa = await bot.send_message(message.from_user.id, 'Выберите подкатегорию', reply_markup=Housekeepers_menu)
        msg_id.append(aaa.message_id)

    elif spec_name == 'Фото, видео, аудио':
        aaa = await bot.send_message(message.from_user.id, 'Выберите подкатегорию', reply_markup=Photo_video_audio_menu)
        msg_id.append(aaa.message_id)

    elif spec_name == 'Юриcты, переводы, бухгалтерия':
        aaa = await bot.send_message(message.from_user.id, 'Выберите подкатегорию', reply_markup=Lawyer_menu)
        msg_id.append(aaa.message_id)

    else:
        data_masters.update({'spec_name': spec_name})

        if data_masters['user'] == 'admin':
            print('Администратор ищет - ', data_masters)
            data_masters.update({'user': None})
            await catalog_for_admin(spec_name, data_masters['city'], state, message)
        else:
            print('Пользователь ищет - ', data_masters)
            await show_specialists_by_filter(spec_name, data_masters['city'], state, message)
