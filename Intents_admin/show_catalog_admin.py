from loader import bot
from aiogram.dispatcher.storage import FSMContext
from DB.find_specialists_db import find_masters
from DB.find_people_by_id import find_people
from inline_bottons import edit_services_btn, menu_start
from Classes.states_classes import Other


async def catalog_for_admin(spec_name, city, state: FSMContext, message):

    base_data = find_masters(city, spec_name)
    print('these people was found -', base_data)

    if base_data[0] == 'n':
        await bot.send_message(message.from_user.id, text='Никого не нашел. Попробуйте позже. '
                                                          'Возвращаемся в главное меню', reply_markup=menu_start)
        await state.finish()

    else:
        await Other.Other_catalog.set()

        for item in base_data:
            id_user = int(item[0])
            spec_name = item[1]
            spec_about = item[4]
            spec_id = item[6]
            user_data = find_people(id_user)
            name = user_data[0]
            tg_username = user_data[4]
            about = user_data[5]
            archetype = user_data[6]
            city = user_data[7]
            birthdate = user_data[8]
            country = user_data[10]
            phone = user_data[11]

            await bot.send_message(message.from_user.id, text=f'<b>Имя</b> - {name}\n'
                                                              f'<b>Cтрана</b> - {country}\n'
                                                              f'<b>Город</b> - {city}\n'
                                                              f'<b>О специалисте</b> - {about}\n'
                                                              f'<b>Услуга</b> - {spec_name}\n'
                                                              f'<b>Описание услуги</b>:\n{spec_about}\n'
                                                              f'<b>Телефон</b>:{phone}\n'
                                                              f'<b>Написать специалисту</b> - @{tg_username}',
                                   parse_mode="HTML",
                                   reply_markup=edit_services_btn(spec_id, id_user))
