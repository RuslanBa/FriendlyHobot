from aiogram import types
from aiogram.dispatcher.storage import FSMContext
from DB.change_user_field import change_fields
from Classes.client_classes import betta_user


async def betta_user_edit(message: types.Message, state: FSMContext):
    """ Change difference fields in a user data """
    text = message.text
    current_state = await state.get_state()

    if current_state == 'Other:Other_change_name':
        await message.answer(f'Отлично, запомнил ваше имя - {text}')
        change_fields(betta_user.id_user, 'name', text)

    elif current_state == 'Other:Other_change_country':
        await message.answer(f'Отлично, запомнил вашу страну - {text}')
        change_fields(betta_user.id_user, 'country', text)

    elif current_state == 'Other:Other_change_city':
        await message.answer(f'Отлично, запомнил ваш город - {text}')
        change_fields(betta_user.id_user, 'city', text)

    elif current_state == 'Other:Other_change_about':
        await message.answer(f'Отлично, запомнил новую информацию о вас - {text}')
        change_fields(betta_user.id_user, 'about', text)

    elif current_state == 'Other:Other_change_birthday':
        await message.answer(f'Отлично, запомнил дату вашего рождения - {text}')
        change_fields(betta_user.id_user, 'birthdate', text)

    elif current_state == 'Other:Other_change_phone':
        await message.answer(f'Отлично, запомнил номер телефона - {text}')
        change_fields(betta_user.id_user, 'phone', text)

    await betta_user(message, state)
