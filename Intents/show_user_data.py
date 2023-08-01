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
    country = user_data[10]

    await bot.send_message(message.from_user.id, text=f'<b>Имя</b> - {name}\n'
                                                      f'<b>Cтрана</b> - {country}\n'
                                                      f'<b>Город, где находится исполнитель</b> - {city}\n'
                                                      f'<b>Общая информация</b> - {about}\n'
                                                      f'<b>Дата рождения</b> - {birthdate}\n', parse_mode='HTML')

    us_spec = user_spec(tg_username)
    for item in us_spec:
        name_spec = item['name']
        about_spec = item['about']
        text_spec = 'Cпециальность - ' + name_spec + '\nОписание услуги - ' + about_spec
        await bot.send_message(message.from_user.id, text=text_spec)

    current_state = await state.get_state()

    if current_state in states_edit_self_list:
        await bot.send_message(message.from_user.id, 'Желаете что-то изменить в своих данных?', reply_markup=save_self)
    elif current_state in states_edit_other_list:
        await bot.send_message(message.from_user.id, 'Желаете что-то изменить в данных этого человека?',
                               reply_markup=save_other)
    else:
        print('Не нашел реакции на текущий state: ', current_state)
