from inline_bottons import list_self, Specialties, selfabout_fields, menu_start
from loader import dp, bot
from aiogram import types
from Classes.states_classes import Other, states_edit_other, all_states
from aiogram.dispatcher.storage import FSMContext
from DB.add_log_db import add_new_log


@dp.callback_query_handler(text='edit_other', state=all_states)
async def answer9(message: types.Message):
    """ Edit button in menu for user fiedls """
    add_new_log(message.from_user.id, message.from_user.username, 'Edit user"')
    await bot.send_message(message.from_user.id, text='Какое поле для другого человека хотите отредактировать?',
                           reply_markup=selfabout_fields)


@dp.callback_query_handler(text=list_self, state=states_edit_other)
async def list_fields2(message: types.Message, state: FSMContext):
    """ Edit information about other user from button edit """
    field = str(dict(message).get('data'))

    if field == 'name':
        await bot.send_message(message.from_user.id, text='Введите новое имя другого человека')
        await Other.Other_change_name.set()

    elif field == 'country':
        await bot.send_message(message.from_user.id, text='Введите название страны')
        await Other.Other_change_country.set()

    elif field == 'city':
        await bot.send_message(message.from_user.id, text='Введите новый город')
        await Other.Other_change_city.set()

    elif field == 'about':
        await bot.send_message(message.from_user.id, text='Введите новый текст о себе')
        await Other.Other_change_about.set()

    elif field == 'birthdate':
        await bot.send_message(message.from_user.id, text='Введите новую дату рождения')
        await Other.Other_change_birthday.set()

    elif field == 'Телефон':
        await bot.send_message(message.from_user.id, text='Введите телефон')
        await Other.Other_change_phone.set()

    else:
        await bot.send_message(message.from_user.id, text='Отлично! Возвращаемся в главное меню',
                               reply_markup=menu_start)
        await state.finish()


@dp.callback_query_handler(text='spec_name', state=states_edit_other)
async def list_fields2(message: types.Message, state: FSMContext):
    await bot.send_message(message.from_user.id, text='Выберите услугу, которую исполнитель может оказать',
                           reply_markup=Specialties)
    await Other.Other_spec.set()
