from inline_bottons import list_self, Specialties, selfabout_fields
from bottons import menu_start
from loader import dp, bot
from Classes.states_classes import Edit, About, all_states, states_edit_self
from DB.add_log_db import add_new_log
from aiogram import types
from aiogram.dispatcher.storage import FSMContext
from DB.change_user_field import change_fields
from Classes.client_classes import alfa_user


@dp.callback_query_handler(text='edit_self', state=all_states)
async def edit_self1(message: types.Message):
    """ Edit button in menu for user fiedls """
    add_new_log(message.from_user.id, message.from_user.username, 'Edit user"')
    await bot.send_message(message.from_user.id, text='Какое поле вы хотите отредактировать?',
                           reply_markup=selfabout_fields)


@dp.callback_query_handler(text=list_self, state=states_edit_self)
async def edit_self2(message: types.Message, state: FSMContext):
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

    elif field == 'Телефон':
        await bot.send_message(message.from_user.id, text='Введите новый телефон')
        await Edit.Edit_phone.set()

    else:
        await bot.send_message(message.from_user.id, text='Отлично! Возвращаемся в главное меню',
                               reply_markup=menu_start)
        await state.finish()


@dp.callback_query_handler(text='spec_name', state=states_edit_self)
async def edit_self4(message: types.Message, state: FSMContext):
    await bot.send_message(message.from_user.id, text='Выберите услугу, которую вы можете оказывать',
                           reply_markup=Specialties)
    await About.AB_spec.set()


@dp.message_handler(state=states_edit_self)
async def edit_self5(message: types.Message, state: FSMContext):
    """ Change difference fields in a user data """
    text = message.text
    current_state = await state.get_state()

    if current_state == 'Edit:Edit_name':
        await message.answer(f'Отлично, запомнил ваше имя - {text}')
        change_fields(alfa_user.id_user, 'name', text)

    elif current_state == 'Edit:Edit_country':
        await message.answer(f'Отлично, запомнил вашу страну - {text}')
        change_fields(alfa_user.id_user, 'country', text)

    elif current_state == 'Edit:Edit_city':
        await message.answer(f'Отлично, запомнил ваш город - {text}')
        change_fields(alfa_user.id_user, 'city', text)

    elif current_state == 'Edit:Edit_about':
        await message.answer(f'Отлично, запомнил новую информацию о вас - {text}')
        change_fields(alfa_user.id_user, 'about', text)

    elif current_state == 'Edit:Edit_birthdate':
        await message.answer(f'Отлично, запомнил дату вашего рождения - {text}')
        change_fields(alfa_user.id_user, 'birthdate', text)

    elif current_state == 'Edit:Edit_phone':
        await message.answer(f'Отлично, запомнил номер телефона - {text}')
        change_fields(alfa_user.id_user, 'phone', text)

    await alfa_user.show_user_data(message, state)
