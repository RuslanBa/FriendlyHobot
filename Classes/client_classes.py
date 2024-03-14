from loader import bot
from aiogram import types
# from Intents.dialog import msg_id
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

        self.users = {}

    async def add_alfa_user(self, message: types.Message, intent):

        if message.from_user.id in self.users:
            print('[add_alfa_user] user exist in alfa_user')
        else:
            self.users[message.from_user.id] = {'tg_id': message.from_user.id,
                                                'tg_name': message.from_user.first_name,
                                                'tg_surname': message.from_user.last_name,
                                                'tg_username': message.from_user.username,
                                                'intent': intent,
                                                'name': None,
                                                'about': None,
                                                'archetype': None,
                                                'city': None,
                                                'birthdate': None,
                                                'speciality_need': None,
                                                'id_user': None,
                                                'country': None,
                                                'phone': None,
                                                'services': None,
                                                'new_spec_name': None,
                                                'new_spec_id': None,
                                                'new_spec_about': None,
                                                'new_spec_city': None,
                                                'orders': None,
                                                'msg_id': []}

            alfa = check_user_tgid(message.from_user.id)
            print('Найден пользователь с данными:', {alfa})

            if alfa is None:
                user_by_username = find_user_id(message.from_user.username)

                if user_by_username is None:
                    print(f'Пользователь не найден ни по tg_id {message.from_user.id}, '
                          f'ни по tg_username {message.from_user.username}')
                    add_new_people(None,
                                   message.from_user.id,
                                   message.from_user.first_name,
                                   message.from_user.last_name,
                                   message.from_user.username,
                                   None, None)

                else:
                    change_fields(user_by_username, 'tg_id', message.from_user.id)
                    print(f'для пользователя с tg_username {message.from_user.username} '
                          f'добавлен tg_id {message.from_user.id}')

                alfa = check_user_tgid(message.from_user.id)

            self.users[message.from_user.id]['name'] = alfa[0]
            self.users[message.from_user.id]['about'] = alfa[5]
            self.users[message.from_user.id]['archetype'] = alfa[6]
            self.users[message.from_user.id]['city'] = alfa[7]
            self.users[message.from_user.id]['birthdate'] = alfa[8]
            self.users[message.from_user.id]['speciality_need'] = alfa[9]
            self.users[message.from_user.id]['id_user'] = alfa[10]
            self.users[message.from_user.id]['country'] = alfa[11]
            self.users[message.from_user.id]['phone'] = alfa[12]

    async def add_msg_id(self, message, aaa):
        self.users[message.from_user.id]['msg_id'].append(aaa)

    async def delete_dialog(self, message: types.Message):

        msg_id = self.users[message.from_user.id]['msg_id']

        if msg_id:
            print('need to delete - ', msg_id)
            for id_messages in msg_id:
                try:
                    await bot.delete_message(message.from_user.id, message_id=int(id_messages))
                except Exception as _ex:
                    print('[client_classes] Error in delete_dialog - ', _ex)
            msg_id.clear()
            print('self.msg_id cleaned and now is - ', msg_id)
        else:
            print("can't clean self.msg_id - it is clean")

    def add_to_db(self, message: types.Message):
        self.users[message.from_user.id]['id_user'] = add_new_people(self.users[message.from_user.id]['name'],
                                                                self.users[message.from_user.id]['tg_id'],
                                                                self.users[message.from_user.id]['tg_name'],
                                                                self.users[message.from_user.id]['tg_surname'],
                                                                self.users[message.from_user.id]['tg_username'],
                                                                self.users[message.from_user.id]['city'],
                                                                self.users[message.from_user.id]['phone'])

        print('[add_to_db] After saving user in DB his self.id_user =',
              self.active_users[message.from_user.id]['id_user'])

    def add_user_spec(self, message: types.Message, spec_id, spec_about, spec_city):
        add_spec(self.users[message.from_user.id]['id_user'],
                 spec_id,
                 spec_about,
                 spec_city,
                 self.users[message.from_user.id]['tg_username'])

        print('[add_user_spec] Trying to save user_spec in DB with self.id_user =',
              self.users[message.from_user.id]['id_user'])

    def change_user_data(self, message: types.Message, user_field, new_value):
        change_fields(self.users[message.from_user.id]['id_user'], user_field, new_value)

    async def show_user_data(self, message: types.Message, state: FSMContext):

        id_user = self.users[message.from_user.id]['id_user']
        tg_username = self.users[message.from_user.id]['tg_username']

        if id_user is None and tg_username:
            self.users[message.from_user.id]['id_user'] = find_user_id(tg_username)
        elif id_user is None and tg_username is None:
            print('[show_user_data] no id and username for searching user')

        xxx = user_data_by_id(id_user)
        self.users[message.from_user.id]['name'] = xxx[0]
        self.users[message.from_user.id]['tg_id'] = xxx[1]
        self.users[message.from_user.id]['tg_name'] = xxx[2]
        self.users[message.from_user.id]['tg_surname'] = xxx[3]
        self.users[message.from_user.id]['tg_username'] = xxx[4]
        self.users[message.from_user.id]['about'] = xxx[5]
        self.users[message.from_user.id]['archetype'] = xxx[6]
        self.users[message.from_user.id]['city'] = xxx[7]
        self.users[message.from_user.id]['birthdate'] = xxx[8]
        self.users[message.from_user.id]['speciality_need'] = xxx[9]
        self.users[message.from_user.id]['country'] = xxx[10]
        self.users[message.from_user.id]['phone'] = xxx[11]

        self.users[message.from_user.id]['services'] = user_spec(tg_username)
        print('us_spec =', self.users[message.from_user.id]['services'])

        current_state = await state.get_state()
        ttt = None
        if current_state in states_edit_self_list:
            ttt = save_self
        elif current_state in states_edit_other_list:
            ttt = save_other

        aaa = await bot.send_message(message.from_user.id,
                                     text=f'<b>Имя</b> - {self.users[message.from_user.id]["name"]}\n'
                                          f'<b>Cтрана</b> - {self.users[message.from_user.id]["country"]}\n'
                                          f'<b>Город исполнителя</b> - {self.users[message.from_user.id]["city"]}\n'
                                          f'<b>Общая информация</b> - {self.users[message.from_user.id]["about"]}\n'
                                          f'<b>Дата рождения</b> - {self.users[message.from_user.id]["birthdate"]}\n'
                                          f'<b>Телефон</b> - {self.users[message.from_user.id]["phone"]}',
                                     parse_mode='HTML',
                                     reply_markup=ttt)
        self.users[message.from_user.id]["msg_id"].append(aaa.message_id)

        if alfa_user.users[message.from_user.id]['services']:
            bbb = await bot.send_message(message.from_user.id, text='<b>Услуги</b>\n', parse_mode='HTML',
                                         reply_markup=menu_main)
            self.users[message.from_user.id]["msg_id"].append(bbb.message_id)

            for item in alfa_user.users[message.from_user.id]['services']:
                spec_name = item['spec_name']
                about_spec = item['about']
                service_id = item['service_id']
                spec_id = item['spec_id']
                text_spec = 'Cпециальность:\n' + spec_name + '\nОписание услуги:\n' + about_spec
                ccc = await bot.send_message(message.from_user.id,
                                             text=text_spec,
                                             parse_mode='HTML',
                                             reply_markup=edit_services_btn(service_id,
                                                                            self.users[message.from_user.id]['id_user'],
                                                                            spec_id))
                self.users[message.from_user.id]["msg_id"].append(ccc.message_id)

            ddd = await bot.send_message(message.from_user.id,
                                         text='Проверьте все ли указано корректно у этого пользователя?',
                                         reply_markup=dont_change_menu)
            self.users[message.from_user.id]["msg_id"].append(ddd.message_id)
            print('msg_id now is - ', self.users[message.from_user.id]["msg_id"])

        else:
            await bot.send_message(message.from_user.id, text='Добавленных услуг у вас пока еще нет',
                                   reply_markup=menu_main)

    async def show_pers_data(self, message: types.Message):

        id_user = self.users[message.from_user.id]['id_user']
        tg_username = self.users[message.from_user.id]['tg_username']

        if id_user is None and tg_username:
            self.users[message.from_user.id]['id_user'] = find_user_id(tg_username)
        elif id_user is None and tg_username is None:
            print('[show_user_data] no id and username for searching user')

        xxx = user_data_by_id(id_user)
        self.users[message.from_user.id]['name'] = xxx[0]
        self.users[message.from_user.id]['tg_id'] = xxx[1]
        self.users[message.from_user.id]['tg_name'] = xxx[2]
        self.users[message.from_user.id]['tg_surname'] = xxx[3]
        self.users[message.from_user.id]['tg_username'] = xxx[4]
        self.users[message.from_user.id]['about'] = xxx[5]
        self.users[message.from_user.id]['archetype'] = xxx[6]
        self.users[message.from_user.id]['city'] = xxx[7]
        self.users[message.from_user.id]['birthdate'] = xxx[8]
        self.users[message.from_user.id]['speciality_need'] = xxx[9]
        self.users[message.from_user.id]['country'] = xxx[10]
        self.users[message.from_user.id]['phone'] = xxx[11]

        aaa = await bot.send_message(message.from_user.id,
                                     text=f'<b>Имя</b> - {self.users[message.from_user.id]["name"]}\n'
                                          f'<b>Cтрана</b> - {self.users[message.from_user.id]["country"]}\n'
                                          f'<b>Город исполнителя</b> - {self.users[message.from_user.id]["city"]}\n'
                                          f'<b>Общая информация</b> - {self.users[message.from_user.id]["about"]}\n'
                                          f'<b>Дата рождения</b> - {self.users[message.from_user.id]["birthdate"]}\n'
                                          f'<b>Телефон</b> - {self.users[message.from_user.id]["phone"]}',
                                     parse_mode='HTML')

        self.users[message.from_user.id]["msg_id"].append(aaa.message_id)

    async def show_user_orders(self, message: types.Message, state: FSMContext):
        print(self.users[message.from_user.id]['id_user'])
        self.users[message.from_user.id]['orders'] = find_orders_db(self.users[message.from_user.id]['id_user'])
        print('for user - ', self.users[message.from_user.id]['id_user'],
              'found orders:', self.users[message.from_user.id]['orders'])

        if not self.users[message.from_user.id]['orders']:
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
            self.users[message.from_user.id]["msg_id"].append(aaa.message_id)
            print('For user ', self.users[message.from_user.id]['id_user'], 'add mes_id - ', aaa.message_id)
            await Order.Order_start.set()

        else:
            await bot.send_message(message.from_user.id, text='Вижу, у вас уже есть размещенные заявки\n',
                                   reply_markup=menu_main)
            for xxx in self.users[message.from_user.id]['orders']:
                id_user = xxx['id_user']
                id_order = xxx['id_order']
                city = xxx['city']
                spec_id = xxx['spec_id']
                spec_data = find_speciality(spec_id)
                spec_name = spec_data[2]
                xxx['spec_name'] = spec_name
                description = xxx['description']
                aaa = await bot.send_message(message.from_user.id,
                                             text=f'Город - {city}\n'
                                                  f'Категория - {spec_name}\n'
                                                  f'Описание задачи:\n'
                                                  f'{description}',
                                             reply_markup=edit_order_btn(id_order, id_user, spec_id))
                self.users[message.from_user.id]["msg_id"].append(aaa.message_id)

            bbb = await bot.send_message(message.from_user.id, text='Что делаем дальше?',
                                         reply_markup=finish_orders)
            self.users[message.from_user.id]["msg_id"].append(bbb.message_id)
            await Order.Order_change.set()

    # def update_alfa_user(self, message: types.Message, intent):
    #     self.intent = intent
    #     self.tg_id = message.from_user.id
    #     self.tg_username = message.from_user.username
    #     self.tg_name = message.from_user.first_name
    #     self.tg_surname = message.from_user.last_name
    #
    #     alfa = check_user_tgid(self.tg_id)
    #     print('Найден пользователь с данными:', {alfa})
    #
    #     if alfa is None:
    #         user_by_username = find_user_id(self.tg_username)
    #
    #         if user_by_username is None:
    #             print(f'Пользователь не найден ни по tg_id {self.tg_id}, ни по tg_username {self.tg_username}')
    #             add_new_people(None, self.tg_id, self.tg_name, self.tg_surname, self.tg_username, None, None)
    #
    #         else:
    #             change_fields(user_by_username, 'tg_id', self.tg_id)
    #             print(f'для пользователя с tg_username {self.tg_username} добавлен tg_id {self.tg_id}')
    #
    #         alfa = check_user_tgid(self.tg_id)
    #
    #     self.name = alfa[0]
    #     self.about = alfa[5]
    #     self.archetype = alfa[6]
    #     self.city = alfa[7]
    #     self.birthdate = alfa[8]
    #     self.speciality_need = alfa[9]
    #     self.id_user = alfa[10]
    #     self.country = alfa[11]
    #     self.phone = alfa[12]


alfa_user = Client()
betta_user = Client()
