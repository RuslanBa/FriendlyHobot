from aiogram.dispatcher.filters.state import State, StatesGroup


class Meeting(StatesGroup):
    Meet_name = State()     # ask name
    Meet_city = State()     # ask city


class About(StatesGroup):
    AB_go = State()  # ready for question
    AB_know = State()  # User already in base
    AB_name = State()  # ask name
    AB_spec = State()  # ask specialities
    AB_price = State()  # ask price
    AB_about = State()  # ask about_self
    AB_city = State()  # ask about_city
    AB_edit = State()  # ask edit
    AB_edit_ok = State()  # go to edit
    AB_go_change = State()  # go to change information about self


class Edit(StatesGroup):
    Edit_name = State()   # enter new name
    Edit_country = State()     # enter new country
    Edit_city = State()     # enter new city
    Edit_about = State()    # enter new about
    Edit_birthdate = State()    # enter new birthdate
    Edit_phone = State()        # enter new phone
    New_spec_name = State()    # enter new spec_name
    New_spec_about = State()   # enter new spec_about
    Edit_spec_about = State()   # edit the spec
    Edit_order = State()    # edit user order


class Delete(StatesGroup):
    Delete_self_spec = State()        # ask about delete a self service
    Delete_other_spec = State()        # ask about delete a other service
    Delete_self_order = State()         # ask about delete a self order


class Find(StatesGroup):
    Find_city = State()
    Find_spec = State()


class Other(StatesGroup):
    Other_identifiers = State()
    Other_name = State()
    Other_tg = State()
    Other_phone = State()
    Other_spec = State()
    Other_spec_about = State()
    Other_spec_city = State()
    Other_change = State()
    Other_change_name = State()
    Other_change_country = State()
    Other_change_city = State()
    Other_change_about = State()
    Other_change_birthday = State()
    Other_change_phone = State()
    Other_catalog = State()


class Feedback(StatesGroup):
    Feedback_send = State()


class Order(StatesGroup):
    Order_start = State()
    Order_spec = State()
    Order_text = State()
    Order_my = State()


class Marking(StatesGroup):
    Marking_needs = State()


all_states = [About.AB_go, About.AB_name, About.AB_spec, About.AB_price, About.AB_know, About.AB_about, About.AB_city,
              About.AB_edit, About.AB_edit_ok, About.AB_go_change,
              Find.Find_spec, Find.Find_city,
              Other.Other_tg, Other.Other_name, Other.Other_spec, Other.Other_spec_about, Other.Other_spec_city,
              Other.Other_change, Other.Other_change_name, Other.Other_change_country, Other.Other_change_city,
              Other.Other_change_about, Other.Other_change_birthday, Other.Other_change_phone, Other.Other_catalog,
              Edit.Edit_name, Edit.Edit_country, Edit.Edit_city, Edit.Edit_about, Edit.Edit_birthdate, Edit.Edit_phone,
              Edit.New_spec_name, Edit.New_spec_about, Edit.Edit_spec_about, Edit.Edit_order,
              Feedback.Feedback_send,
              Delete.Delete_other_spec, Delete.Delete_self_spec, Delete.Delete_self_order,
              Order.Order_spec, Order.Order_start, Order.Order_text, Order.Order_my]

states_edit_self = [Edit.Edit_name, Edit.Edit_country, Edit.Edit_city, Edit.Edit_about, Edit.Edit_birthdate,
                    Edit.New_spec_name, Edit.Edit_phone, Edit.New_spec_about, Edit.Edit_spec_about, Edit.Edit_order,
                    About.AB_know, About.AB_about, About.AB_city,
                    Delete.Delete_self_spec, Delete.Delete_self_order,
                    Order.Order_start, Order.Order_spec, Order.Order_text, Order.Order_my]

states_edit_self_list = ['Edit:Edit_name', 'Edit:Edit_country', 'Edit:Edit_city', 'Edit:Edit_about',
                         'Edit:Edit_birthdate', 'Edit:Edit_phone', 'Edit:New_spec_name', 'Edit:New_spec_about',
                         'Edit:Edit_spec_about', 'Edit:Edit_order',
                         'About:AB_know', 'About:AB_about', 'About:AB_city',
                         'Delete:Delete_self_spec', 'Delete:Delete_self_order',
                         'Order:Order_start', 'Order:Order_spec', 'Order:Order_text', 'Order:Order_my']

states_pers_data_edit = [Edit.Edit_name, Edit.Edit_country, Edit.Edit_city, Edit.Edit_about, Edit.Edit_birthdate,
                         Edit.Edit_phone]

states_edit_other = [Other.Other_change_name, Other.Other_change_country, Other.Other_change_city,
                     Other.Other_change_about, Other.Other_change_birthday, Other.Other_change, Other.Other_spec_about,
                     Other.Other_spec_city, Other.Other_change_phone, Other.Other_catalog, Delete.Delete_other_spec]

states_edit_other_list = ['Other:Other_change_name', 'Other:Other_change_country', 'Other:Other_change_city',
                          'Other:Other_change_about', 'Other:Other_change_birthday', 'Other:Other_change',
                          'Other:Other_spec_about', 'Other:Other_spec_city', 'Other:Other_change_phone',
                          'Other:Other_catalog', 'Delete:Delete_other_spec']
