from aiogram.dispatcher.filters.state import State, StatesGroup


class About_me(StatesGroup):
    AB_go = State()  # ready for question
    AB_name = State()  # ask name
    AB_spec = State()  # ask specialities
    AB_price = State()  # ask price
    AB_about = State()  # ask about_self
    AB_edit = State()  # ask edit
