from loader import bot, msg_id
from aiogram import types
from aiogram.dispatcher.storage import FSMContext
from DB.check_user_db_tgid import check_user_tgid
from DB.find_id_by_username import find_user_id
from DB.check_user_in_db import check_user
from DB.change_user_field import change_fields
from DB.add_people_db import add_new_people
from DB.add_spec_for_people import add_spec
from DB.find_orders_by_user import find_orders_db
from DB.from_db_user_data import user_data_by_id, user_spec
from DB.find_spec_id_by_spec_name import find_spec_id
from inline_bottons import dont_change_menu, save_self, save_other, edit_services_btn, edit_order_btn
from Classes.states_classes import states_edit_self_list, states_edit_other_list


class Client:
    """Base class for all clients"""

    def __init__(self):
        self.tg_id = None
        self.tg_name = None
        self.tg_surname = None
        self.tg_username = None
        self.intent = None
        self.name = None
        self.about = None
        self.archetype = None
        self.city = None
        self.birthdate = None
        self.speciality_need = None
        self.id_user = None
        self.country = None
        self.phone = None

    def add_to_db(self):
        self.id_user = add_new_people(self.name, self.tg_id, self.tg_name, self.tg_surname, self.tg_username,
                                      self.city, self.phone)
        print('[add_to_db] After saving user in DB his self.id_user =', self.id_user)

    def add_user_spec(self, spec_id, spec_about, spec_city):
        add_spec(self.id_user, spec_id, spec_about, spec_city, self.tg_username)
        print('[add_user_spec] Trying to save user_spec in DB with self.id_user =', self.id_user)

    def find_id_user_by_tg(self):
        aaa = check_user(betta_user.tg_username)
        if aaa > 0:
            self.id_user = find_user_id(self.tg_username)
        else:
            self.id_user = None

    def update_alfa_user(self, message: types.Message, intent):
        self.intent = intent
        self.tg_id = message.from_user.id
        self.tg_username = message.from_user.username
        self.tg_name = message.from_user.first_name
        self.tg_surname = message.from_user.last_name

        alfa = check_user_tgid(self.tg_id)
        print('Найден пользователь с данными:', {alfa})

        if alfa is None:
            user_by_username = find_user_id(self.tg_username)

            if user_by_username is None:
                print(f'Пользователь не найден ни по tg_id {self.tg_id}, ни по tg_username {self.tg_username}')
                add_new_people(None, self.tg_id, self.tg_name, self.tg_surname, self.tg_username, None, None)

            else:
                change_fields(user_by_username, 'tg_id', self.tg_id)
                print(f'для пользователя с tg_username {self.tg_username} добавлен tg_id {self.tg_id}')

            alfa = check_user_tgid(self.tg_id)

        self.name = alfa[0]
        self.about = alfa[5]
        self.archetype = alfa[6]
        self.city = alfa[7]
        self.birthdate = alfa[8]
        self.speciality_need = alfa[9]
        self.id_user = alfa[10]
        self.country = alfa[11]
        self.phone = alfa[12]

    def change_user_data(self, user_field, new_value):
        change_fields(self.id_user, user_field, new_value)

    async def show_user_data(self, message: types.Message, state: FSMContext):
        if self.id_user is None and self.tg_username:
            self.id_user = find_user_id(self.tg_username)
        elif self.id_user is None and self.tg_username is None:
            print('[show_user_data] no id and username for searching user')

        xxx = user_data_by_id(self.id_user)
        self.name = xxx[0]
        self.tg_id = xxx[1]
        self.tg_name = xxx[2]
        self.tg_surname = xxx[3]
        self.tg_username = xxx[4]
        self.about = xxx[5]
        self.archetype = xxx[6]
        self.city = xxx[7]
        self.birthdate = xxx[8]
        self.speciality_need = xxx[9]
        self.country = xxx[10]
        self.phone = xxx[11]

        us_spec = user_spec(self.tg_username)
        print('us_spec =', us_spec)

        current_state = await state.get_state()
        ttt = None
        if current_state in states_edit_self_list:
            ttt = save_self
        elif current_state in states_edit_other_list:
            ttt = save_other

        aaa = await bot.send_message(message.from_user.id,
                                     text=f'<b>Имя</b> - {self.name}\n'
                                          f'<b>Cтрана</b> - {self.country}\n'
                                          f'<b>Город исполнителя</b> - {self.city}\n'
                                          f'<b>Общая информация</b> - {self.about}\n'
                                          f'<b>Дата рождения</b> - {self.birthdate}\n'
                                          f'<b>Телефон</b> - {self.phone}', parse_mode='HTML',
                                     reply_markup=ttt)
        msg_id.append(aaa.message_id)

        for item in us_spec:
            spec_name = item['spec_name']
            about_spec = item['about']
            service_id = item['service_id']
            spec_id = item['spec_id']
            text_spec = '<b>Услуги</b>\nCпециальность:\n' + spec_name + '\nОписание услуги:\n' + about_spec
            await bot.send_message(message.from_user.id,
                                   text=text_spec,
                                   parse_mode='HTML',
                                   reply_markup=edit_services_btn(service_id, self.id_user, spec_id))

        await bot.send_message(message.from_user.id, text='Проверьте все ли указано корректно у этого пользователя?',
                               reply_markup=dont_change_menu)

    async def show_user_orders(self, message: types.Message, state: FSMContext):
        data_orders = find_orders_db(self.id_user)
        print('for user - ', self.id_user, 'found orders:', data_orders)

        if not data_orders:
            await message.answer('У вас нет размещенных задач на поиск исполнителя.\n'
                                 'Возвращаемся в главное меню.')
            await state.finish()

        else:
            for xxx in data_orders:
                id_user = xxx['id_user']
                id_order = xxx['id_order']
                city = xxx['city']
                spec_id = xxx['spec_id']
                description = xxx['description']
                await bot.send_message(message.from_user.id,
                                       text=f'Город - {city}\n'
                                            f'Категория - {spec_id}\n'
                                            f'Описание задачи:\n'
                                            f'{description}',
                                       reply_markup=edit_order_btn(id_order, id_user))
            await bot.send_message(message.from_user.id, text='Проверьте все ли указано корректно?',
                                   reply_markup=dont_change_menu)


alfa_user = Client()
betta_user = Client()
