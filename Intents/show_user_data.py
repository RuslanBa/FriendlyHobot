from DB.from_db_user_data import user_data_tg, user_spec
from loader import bot
from aiogram import types
from inline_bottons import save_self, save_other
from aiogram.dispatcher.storage import FSMContext
from Intents.classes import states_edit_self_list, states_edit_other_list


async def take_user_data(tg_username, message: types.Message, state: FSMContext):
    user_data = user_data_tg(tg_username)
    user_data = list(user_data)
    name = user_data[0]
    tg_id = user_data[1]
    tg_name = user_data[2]
    tg_surname = user_data[3]
    tg_username = user_data[4]
    about = user_data[5]
    archetype = user_data[6]
    city = user_data[7]
    birthdate = user_data[8]
    speciality_need = user_data[9]

    await bot.send_message(message.from_user.id, text=f'Имя - {name}\n'
                                                      f'Город - {city}\n'
                                                      f'Общая информация - {about}\n'
                                                      f'Дата рождения - {birthdate}\n')

    us_spec = user_spec(tg_username)
    for item in us_spec:
        name_spec = item['name']
        about_spec = item['about']
        text_spec = 'Cпециальность - ' + name_spec + '\nОписание услуги - ' + about_spec
        await message.answer(text_spec)

    current_state = await state.get_state()

    if current_state in states_edit_self_list:
        await message.answer('Желаете что-то изменить в своих данных?', reply_markup=save_self)
    elif current_state in states_edit_other_list:
        await message.answer('Желаете что-то изменить в данных этого человека?', reply_markup=save_other)
