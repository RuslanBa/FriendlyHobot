from aiogram.dispatcher.filters.state import State, StatesGroup


class About(StatesGroup):
    AB_go = State()  # ready for question
    AB_know = State()  # User already in base
    AB_name = State()  # ask name
    AB_spec = State()  # ask specialities
    AB_price = State()  # ask price
    AB_about = State()  # ask about_self
    AB_edit = State()  # ask edit
    AB_edit_ok = State()  # go to edit
    AB_go_change = State()  # go to change information about self


class Edit(StatesGroup):
    Edit_name = State()   # enter new name
    Edit_country = State()     # enter new country
    Edit_city = State()     # enter new city
    Edit_about = State()    # enter new about
    Edit_birthdate = State()    # enter new birthdate
    Edit_spec_name = State()    # enter new spec_name
    Edit_spec_about = State()   # enter new spec_about


class Find(StatesGroup):
    Find_city = State()
    Find_spec = State()


class Other(StatesGroup):
    Other_name = State()
    Other_tg = State()
    Other_spec = State()
    Other_spec_about = State()
    Other_spec_city = State()
    Other_change = State()
    Other_change_name = State()
    Other_change_country = State()
    Other_change_city = State()
    Other_change_about = State()
    Other_change_birthday = State()


all_states = [About.AB_go, About.AB_name, About.AB_spec, About.AB_price, About.AB_know, About.AB_about, About.AB_edit,
              About.AB_edit_ok, About.AB_go_change,
              Find.Find_spec, Find.Find_city,
              Other.Other_tg, Other.Other_name, Other.Other_spec, Other.Other_spec_about, Other.Other_spec_city,
              Other.Other_change, Other.Other_change_name, Other.Other_change_country, Other.Other_change_city,
              Other.Other_change_about, Other.Other_change_birthday,
              Edit.Edit_name, Edit.Edit_country, Edit.Edit_city, Edit.Edit_about, Edit.Edit_birthdate,
              Edit.Edit_spec_name, Edit.Edit_spec_about]

states_edit_self = [Edit.Edit_name, Edit.Edit_country, Edit.Edit_city, Edit.Edit_about, Edit.Edit_birthdate, Edit.Edit_spec_name,
                    Edit.Edit_spec_about, About.AB_know, About.AB_about]

states_edit_self_list = ['Edit:Edit_name', 'Edit:Edit_country', 'Edit:Edit_city', 'Edit:Edit_about',
                         'Edit:Edit_birthdate', 'Edit:Edit_spec_name', 'Edit:Edit_spec_about', 'About:AB_know',
                         'About:AB_about']

states_edit_other = [Other.Other_change_name, Other.Other_change_country, Other.Other_change_city,
                     Other.Other_change_about, Other.Other_change_birthday, Other.Other_change, Other.Other_spec_about,
                     Other.Other_spec_city]

states_edit_other_list = ['Other:Other_change_name', 'Other:Other_change_country', 'Other:Other_change_city',
                          'Other:Other_change_about', 'Other:Other_change_birthday', 'Other:Other_change',
                          'Other:Other_spec_about', 'Other.Other_spec_city']
