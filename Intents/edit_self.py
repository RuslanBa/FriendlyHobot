from inline_bottons import list_fields, Specialties, selfabout_fields
from bottons import menu_start
from loader import dp, bot
from aiogram import types
from Intents.classes import Edit, About, Other, all_states, states_edit_self, states_edit_other
from Intents.edit_func import edit_any_user
from aiogram.dispatcher.storage import FSMContext
from DB.add_log_db import add_new_log


@dp.callback_query_handler(text='edit_self', state=all_states)
async def answer9(message: types.Message):
    """ Edit button in menu for user fiedls """
    add_new_log(message.from_user.id, message.from_user.username, 'Edit user"')
    await bot.send_message(message.from_user.id, text='Какое поле вы хотите отредактировать?',
                           reply_markup=selfabout_fields)


@dp.callback_query_handler(text=list_fields, state=states_edit_self)
async def list_fields1(message: types.Message, state: FSMContext):
    """ Edit self information from button edit """
    field = str(dict(message).get('data'))

    if field == 'name':
        await bot.send_message(message.from_user.id, text='Введите новое имя')
        await Edit.Edit_name.set()

    elif field == 'country':
        await bot.send_message(message.from_user.id, text='Введите название страны')
        await Edit.Edit_country.set()

    elif field == 'city':
        await bot.send_message(message.from_user.id, text='Введите новый город')
        await Edit.Edit_city.set()

    elif field == 'about':
        await bot.send_message(message.from_user.id, text='Введите новый текст о себе')
        await Edit.Edit_about.set()

    elif field == 'birthdate':
        await bot.send_message(message.from_user.id, text='Введите новую дату рождения')
        await Edit.Edit_birthdate.set()

    elif field == 'spec_name':
        await bot.send_message(message.from_user.id, text='Выберите услугу, которую вы можете оказывать',
                               reply_markup=Specialties)
        await About.AB_spec.set()

    else:
        await bot.send_message(message.from_user.id, text='Отлично! Возвращаемся в главное меню',
                               reply_markup=menu_start)
        await state.finish()


@dp.message_handler(state=states_edit_self)
async def edit_self(message: types.Message, state: FSMContext):
    tg_username = str(message.from_user.username)
    mess = message
    await edit_any_user(tg_username, mess, state)  # go to edit_func
