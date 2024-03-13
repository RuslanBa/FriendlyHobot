from aiogram import types


class Message:
    """Base class for all messages"""

    def __init__(self):

        self.messages = {}

    async def add_message(self, message: types.Message):

        self.messages[message.from_user.id] = {
            'table_name': None,
            'mes_id': None,
            'channel_id': None,
            'date': None,
            'time': None,
            'from_tg_group_id': None,
            'from_tg_user_id': None,
            'text': None,
            'id': None,
            'intent': None,
            'spec_id': None,
            'probability': None,
            'check_admin': None
        }


mark_message = Message()   # message for marking by admin
