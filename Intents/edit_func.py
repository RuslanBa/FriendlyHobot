from aiogram import types
from aiogram.dispatcher.storage import FSMContext
from Intents.show_user_data import take_user_data
from DB.change_user_field import change_fields


async def edit_any_user(tg_username, message: types.Message, state: FSMContext):
    """ Change difference fields in a user data """
    text = message.text
    current_state = await state.get_state()

    if current_state == 'Edit:Edit_name' or current_state == 'Other:Other_change_name':
        await message.answer(f'Отлично, запомнил ваше имя - {text}')
        change_fields(tg_username, 'name', text)

    elif current_state == 'Edit:Edit_country' or current_state == 'Other:Other_change_country':
        await message.answer(f'Отлично, запомнил вашу страну - {text}')
        change_fields(tg_username, 'country', text)

    elif current_state == 'Edit:Edit_city' or current_state == 'Other:Other_change_city':
        await message.answer(f'Отлично, запомнил ваш город - {text}')
        change_fields(tg_username, 'city', text)

    elif current_state == 'Edit:Edit_about' or current_state == 'Other:Other_change_about':
        await message.answer(f'Отлично, запомнил новую информацию о вас - {text}')
        change_fields(tg_username, 'about', text)

    elif current_state == 'Edit:Edit_birthdate' or current_state == 'Other:Other_change_birthday':
        await message.answer(f'Отлично, запомнил дату вашего рождения - {text}')
        change_fields(tg_username, 'birthdate', text)

    await take_user_data(tg_username, message, state)
