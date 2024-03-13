from aiogram import types
from Classes.client_classes import alfa_user
from DB.add_order_db import add_order
from DB.change_order_field import change_fields_ord
from DB.delete_order_db import delete_order_db
from DB.find_spec_id_by_spec_name import find_spec_id


class Order:
    """Base class for all orders"""

    def __init__(self):

        self.orders = {}

    async def add_alfa_order(self, message: types.Message):

        self.orders[message.from_user.id] = {'id_order': None,
                                             'id_user': alfa_user.users[message.from_user.id]['id_user'],
                                             'spec_name': None,
                                             'spec_id': None,
                                             'tg_username': message.from_user.username,
                                             'description': None,
                                             'city': alfa_user.users[message.from_user.id]['city'],
                                             'date': None,
                                             'time': None}

    def save_order(self, message: types.Message):

        spec_name = self.orders[message.from_user.id]['spec_name']
        id_user = self.orders[message.from_user.id]['id_user']
        description = self.orders[message.from_user.id]['description']
        city = self.orders[message.from_user.id]['city']

        self.orders[message.from_user.id]['spec_id'] = find_spec_id(spec_name)
        new_order_id = add_order(id_user, self.orders[message.from_user.id]['spec_id'], description, city)
        del self.orders[message.from_user.id]
        return new_order_id

    def change_betta_order(self, order_field, new_value, message: types.Message):
        change_fields_ord(self.orders[message.from_user.id]['id_order'], order_field, new_value)

    def delete_betta_order(self, message: types.Message):
        delete_order_db(self.orders[message.from_user.id]['id_user'],
                        self.orders[message.from_user.id]['id_order'])


alfa_order = Order()    # order making by user
betta_order = Order()   # order editing or deleting by user
