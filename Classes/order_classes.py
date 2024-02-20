from DB.add_order_db import add_order
from DB.change_order_field import change_fields_ord
from DB.delete_order_db import delete_order_db
from DB.find_spec_id_by_spec_name import find_spec_id


class Order:
    """Base class for all orders"""

    def __init__(self):
        self.id_order = None
        self.id_user = None
        self.spec_name = None
        self.spec_id = None
        self.tg_username = None
        self.description = None
        self.city = None
        self.date = None
        self.time = None

    def save_order(self):
        self.spec_id = find_spec_id(self.spec_name)
        new_order_id = add_order(self.id_user, self.spec_id, self.description, self.city)
        return new_order_id

    def change_betta_order(self, order_field, new_value):
        change_fields_ord(self.id_order, order_field, new_value)

    def delete_betta_order(self):
        delete_order_db(self.id_user, self.id_order)


alfa_order = Order()    # order making by user
betta_order = Order()   # order editing or deleting by user
