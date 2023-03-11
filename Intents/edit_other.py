from inline_bottons import list_fields, Specialties, selfabout_fields
from bottons import menu_start
from loader import dp, bot
from aiogram import types
from Intents.classes import Other, states_edit_other, all_states
from Intents.edit_func import edit_any_user
from aiogram.dispatcher.storage import FSMContext
from DB.add_log_db import add_new_log


@dp.callback_query_handler(text='edit_other', state=all_states)
async def answer9(message: types.Message):
    """ Edit button in menu for user fiedls """
    add_new_log(message.from_user.id, message.from_user.username, 'Edit user"')
    await bot.send_message(message.from_user.id, text='Какое поле для другого человека хотите отредактировать?',
                           reply_markup=selfabout_fields)


@dp.callback_query_handler(text=list_fields, state=states_edit_other)
async def list_fields2(message: types.Message, state: FSMContext):
    """ Edit information about other user from button edit """
    field = str(dict(message).get('data'))

    if field == 'name':
        await bot.send_message(message.from_user.id, text='Введите новое имя другого человека')
        await Other.Other_change_name.set()

    elif field == 'city':
        await bot.send_message(message.from_user.id, text='Введите новый город')
        await Other.Other_change_city.set()

    elif field == 'about':
        await bot.send_message(message.from_user.id, text='Введите новый текст о себе')
        await Other.Other_change_about.set()

    elif field == 'birthdate':
        await bot.send_message(message.from_user.id, text='Введите новую дату рождения')
        await Other.Other_change_birthday.set()

    elif field == 'spec_name':
        await bot.send_message(message.from_user.id, text='Выберите услугу, которую вы можете оказывать',
                               reply_markup=Specialties)
        await Other.Other_spec.set()

    else:
        await bot.send_message(message.from_user.id, text='Отлично! Возвращаемся в главное меню',
                               reply_markup=menu_start)
        await state.finish()
