from loader import bot
from aiogram import types
from DB.check_user_db_tgid import check_user_tgid
from DB.find_id_by_username import find_user_id
from DB.change_user_field import change_fields
from DB.add_people_db import add_new_people
from DB.find_orders_by_user import find_orders_db
from inline_bottons import edit_order_btn, dont_change_menu
from aiogram.dispatcher.storage import FSMContext


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
                spec = xxx['spec_name']
                description = xxx['description']
                await bot.send_message(message.from_user.id,
                                       text=f'Город - {city}\n'
                                            f'Категория - {spec}\n'
                                            f'Описание задачи:\n'
                                            f'{description}',
                                       reply_markup=edit_order_btn(id_order, id_user))
            await bot.send_message(message.from_user.id, text='Проверьте все ли указано корректно?',
                                   reply_markup=dont_change_menu)


alfa_user = Client()
