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
from DB.find_spec_by_id import find_speciality
from inline_bottons import dont_change_menu, save_self, save_other, edit_services_btn, edit_order_btn, yes_no, \
    finish_orders
from Classes.states_classes import states_edit_self_list, states_edit_other_list, Order
from bottons import menu_main


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
        self.services = None
        self.orders = None

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

    async def delete_dialog(self, message: types.Message):
        if msg_id:
            for id_messages in msg_id:
                await bot.delete_message(message.from_user.id, message_id=int(id_messages))
            msg_id.clear()
            print('msg_id cleaned and now is - ', msg_id)
        else:
            print("can't clean msg_id - it is clean")

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

        self.services = user_spec(self.tg_username)
        print('us_spec =', self.services)

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

        bbb = await bot.send_message(message.from_user.id, text='<b>Услуги</b>\n', parse_mode='HTML',
                                     reply_markup=menu_main)
        msg_id.append(bbb.message_id)

        for item in alfa_user.services:
            spec_name = item['spec_name']
            about_spec = item['about']
            service_id = item['service_id']
            spec_id = item['spec_id']
            text_spec = 'Cпециальность:\n' + spec_name + '\nОписание услуги:\n' + about_spec
            ccc = await bot.send_message(message.from_user.id,
                                         text=text_spec,
                                         parse_mode='HTML',
                                         reply_markup=edit_services_btn(service_id, self.id_user, spec_id))
            msg_id.append(ccc.message_id)

        ddd = await bot.send_message(message.from_user.id,
                                     text='Проверьте все ли указано корректно у этого пользователя?',
                                     reply_markup=dont_change_menu)
        msg_id.append(ddd.message_id)
        print('msg_id now is - ', msg_id)

    async def show_pers_data(self, message: types.Message):
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

        aaa = await bot.send_message(message.from_user.id,
                                     text=f'<b>Имя</b> - {self.name}\n'
                                          f'<b>Cтрана</b> - {self.country}\n'
                                          f'<b>Город исполнителя</b> - {self.city}\n'
                                          f'<b>Общая информация</b> - {self.about}\n'
                                          f'<b>Дата рождения</b> - {self.birthdate}\n'
                                          f'<b>Телефон</b> - {self.phone}', parse_mode='HTML')
        msg_id.append(aaa.message_id)

    async def show_user_orders(self, message: types.Message, state: FSMContext):
        self.orders = find_orders_db(self.id_user)
        print('for user - ', self.id_user, 'found orders:', self.orders)

        if not self.orders:
            await bot.send_message(message.from_user.id, text='У вас нет размещенных задач на поиск исполнителя',
                                   reply_markup=menu_main)
            aaa = await bot.send_message(message.from_user.id,
                                         text='Хотите, чтобы я самостоятельно подобрал потенциальных '
                                              'исполнителей под ваш запрос?\n'
                                              'Это бесплатно. Я задам вам несколько вопросов, '
                                              'пойму, что вам нужно и создам зявку.\n'
                                              'Далее покажу вам отклики тех испонителей, которые будут согласны ее '
                                              'выполнить.',
                                         reply_markup=yes_no)
            msg_id.append(aaa.message_id)
            await Order.Order_start.set()

        else:
            await bot.send_message(message.from_user.id, text='Вижу, у вас уже есть размещенные заявки\n',
                                   reply_markup=menu_main)
            for xxx in self.orders:
                id_user = xxx['id_user']
                id_order = xxx['id_order']
                city = xxx['city']
                spec_data = find_speciality(xxx['spec_id'])
                spec_name = spec_data[2]
                xxx['spec_name'] = spec_name
                description = xxx['description']
                aaa = await bot.send_message(message.from_user.id,
                                             text=f'Город - {city}\n'
                                                  f'Категория - {spec_name}\n'
                                                  f'Описание задачи:\n'
                                                  f'{description}',
                                             reply_markup=edit_order_btn(id_order, id_user))
                msg_id.append(aaa.message_id)

            bbb = await bot.send_message(message.from_user.id, text='Что делаем дальше?',
                                         reply_markup=finish_orders)
            msg_id.append(bbb.message_id)
            await Order.Order_change.set()


alfa_user = Client()
betta_user = Client()
