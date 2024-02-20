class Message:
    """Base class for all messages"""

    def __init__(self):
        self.table_name = None
        self.mes_id = None
        self.channel_id = None
        self.date = None
        self.time = None
        self.from_tg_group_id = None
        self.from_tg_user_id = None
        self.text = None
        self.id = None
        self.intent = None
        self.spec_id = None
        self.probability = None
        self.check_admin = None


mark_message = Message()   # message for marking by admin
