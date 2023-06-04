from aiogram import types
from loader import dp, bot
from bottons import menu_main, menu_start
from DB.add_log_db import add_new_log
from DB.find_specialists_db import find_masters
from DB.find_people_by_id import find_people
from Intents.classes import Find
from inline_bottons import Specialties, Cities, list_specialities, list_cities
from aiogram.dispatcher.storage import FSMContext


data_masters = {'city': None, 'spec_name': None}


@dp.message_handler(text='Найти специалиста')
async def answer(message: types.Message):
    add_new_log(message.from_user.id, message.from_user.username, 'find specialist"')
    await message.answer(text='Давайте подберем того, кто сможет вам помочь', reply_markup=menu_main)
    await message.answer(text='В каком городе вы ищете исполнителя? (пока я могу поискать только ним)',
                         reply_markup=Cities)
    await Find.Find_city.set()


@dp.callback_query_handler(text=list_cities, state=Find.Find_city)
async def answer2(message: types.Message):
    city = str(dict(message).get('data'))
    data_masters.update({'city': city})
    await bot.send_message(message.from_user.id, 'Запомнил ваш город. Выберите категорию', reply_markup=Specialties)
    await Find.Find_spec.set()


@dp.callback_query_handler(text=list_specialities, state=Find.Find_spec)
async def answer3(message: types.Message, state: FSMContext):
    spec_name = str(dict(message).get('data'))
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

            await bot.send_message(message.from_user.id, text=f'Имя - {name}\n'
                                                              f'Cтрана - {country}\n'
                                                              f'Город - {city}\n'
                                                              f'О специалисте - {about}\n'
                                                              f'Услуга - {spec_name}\n'
                                                              f'Описание услуги - {spec_about}\n'
                                                              f'Написать специалисту - @{tg_username}')
    await state.finish()
