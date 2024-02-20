from DB.from_db_user_data import user_data_by_id, user_spec
from loader import bot
from aiogram import types
from inline_bottons import save_self, save_other, dont_change_menu, edit_services_btn
from aiogram.dispatcher.storage import FSMContext
from Classes.states_classes import states_edit_self_list, states_edit_other_list


async def take_user_data(id_user, message: types.Message, state: FSMContext):
    user_data = user_data_by_id(id_user)
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
    phone = user_data[11]

    us_spec = user_spec(tg_username)
    current_state = await state.get_state()

    if current_state in states_edit_self_list:
        await bot.send_message(message.from_user.id, text=f'<b>Имя</b> - {name}\n'
                                                          f'<b>Cтрана</b> - {country}\n'
                                                          f'<b>Город, где вы находитесь</b> - {city}\n'
                                                          f'<b>Общая информация</b> - {about}\n'
                                                          f'<b>Дата рождения</b> - {birthdate}\n'
                                                          f'<b>Телефон</b> - {phone}', parse_mode='HTML',
                               reply_markup=save_self)

        for item in us_spec:
            print('us_spec = ', us_spec)
            name_spec = item['name']
            about_spec = item['about']
            spec_id = item['spec_id']
            text_spec = '<b>Ваши услуги</b>\nCпециальность:\n' + name_spec + '\nОписание услуги:\n' + about_spec
            await bot.send_message(message.from_user.id,
                                   text=text_spec,
                                   parse_mode='HTML',
                                   reply_markup=edit_services_btn(spec_id, id_user))

        await bot.send_message(message.from_user.id, text='Проверьте все ли указано корректно?',
                               reply_markup=dont_change_menu)

    elif current_state in states_edit_other_list:
        await bot.send_message(message.from_user.id, text=f'<b>Имя</b> - {name}\n'
                                                          f'<b>Cтрана</b> - {country}\n'
                                                          f'<b>Город, где находится исполнитель</b> - {city}\n'
                                                          f'<b>Общая информация</b> - {about}\n'
                                                          f'<b>Дата рождения</b> - {birthdate}\n'
                                                          f'<b>Телефон</b> - {phone}', parse_mode='HTML',
                               reply_markup=save_other)

        for item in us_spec:
            name_spec = item['name']
            about_spec = item['about']
            spec_id = item['spec_id']
            text_spec = '<b>Услуги</b>\nCпециальность:\n' + name_spec + '\nОписание услуги:\n' + about_spec
            await bot.send_message(message.from_user.id,
                                   text=text_spec,
                                   parse_mode='HTML',
                                   reply_markup=edit_services_btn(spec_id, id_user))

        await bot.send_message(message.from_user.id, text='Проверьте все ли указано корректно у этого пользователя?',
                               reply_markup=dont_change_menu)

    else:
        await bot.send_message(message.from_user.id,
                               text=f'Хм... Не получилось разобраться с вашим намерением. '
                                    f'Передал информацию разработчикам. Попробуйте еще раз чуть позже')
        print('[INFO take_user_data] определен state, который не попадает в группы '
              'states_edit_other_list и states_edit_self_list' + current_state)
        await state.finish()
