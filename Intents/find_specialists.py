from aiogram import types
from loader import dp, bot
from bottons import menu_main, menu_start
from inline_bottons import Specialties
from DB.add_log_db import add_new_log
from DB.find_specialists_db import find_masters
from DB.find_people_by_id import find_people
from Intents.classes import Find
from inline_bottons import list_specialities
from aiogram.dispatcher.storage import FSMContext


data_masters = {'spec_name': None}


@dp.message_handler(text='Найти специалиста')
async def answer(message: types.Message):
    add_new_log(message.from_user.id, message.from_user.username, 'find specialist"')
    await message.answer(text='Давайте подберем того, кто сможет вам помочь', reply_markup=menu_main)
    await message.answer('Выберите категорию', reply_markup=Specialties)
    await Find.Find_spec.set()


@dp.callback_query_handler(text=list_specialities, state=Find.Find_spec)
async def answer2(message: types.Message, state: FSMContext):
    spec_name = str(dict(message).get('data'))
    data_masters.update({'spec_name': spec_name})

    base_data = find_masters(spec_name)
    print(base_data)

    if base_data[0] == 'n':
        await bot.send_message(message.from_user.id, text='Никого не нашел. Попробуйте позже. '
                                                          'Возвращаемся в главное меню', reply_markup=menu_start)

    else:
        for item in base_data:
            id_user = int(item[0])
            spec_name = item[1]
            spec_about = item[4]
            people = find_people(id_user)
            name = people[0]
            city = people[2]
            username = people[3]
            await bot.send_message(message.from_user.id, text=f'Имя - {name}\n'
                                                              f'Город - {city}\n'
                                                              f'Услуга - {spec_name}\n'
                                                              f'Описание услуги - {spec_about}\n'
                                                              f'Написать специалисту - @{username}')
    await state.finish()
