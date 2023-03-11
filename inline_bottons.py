from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
import emoji

# Меню ---------------------------------------------------------------------------------

Specialties = InlineKeyboardMarkup(row_width=1)
yes_no = InlineKeyboardMarkup(row_width=1)
save_self = InlineKeyboardMarkup(row_width=1)
save_other = InlineKeyboardMarkup(row_width=1)
selfabout_fields = InlineKeyboardMarkup(row_width=1)


# Кнопки ---------------------------------------------------------------------------------

VNG = InlineKeyboardButton(text='ВНЖ', callback_data='ВНЖ')
Driver = InlineKeyboardButton(text='Водители / трансфер', callback_data='Водитель')
Doctor = InlineKeyboardButton(text='Врачи', callback_data='Врач')
Cleaning = InlineKeyboardButton(text='Клининг / Уборка', callback_data='Клининг')
Manicurist = InlineKeyboardButton(text='Мастера по маникюру', callback_data='Мастер по маникюру')
Babysitter = InlineKeyboardButton(text='Няни', callback_data='Няня')
Stylist = InlineKeyboardButton(text='Паракмахеры / стилисты', callback_data='Стилист')
Psychologist = InlineKeyboardButton(text='Психологи', callback_data='Психолог')
Serviceman = InlineKeyboardButton(text='Мастера по ремонту', callback_data='Мастер по ремонту')
Tutor = InlineKeyboardButton(text='Репетиторы / Преподаватели', callback_data='Преподаватель')
Realtor = InlineKeyboardButton(text='Риелторы', callback_data='Риелтор')

yes = InlineKeyboardButton(text='Да', callback_data='yes')
no = InlineKeyboardButton(text='Нет', callback_data='no')

edit_self = InlineKeyboardButton(text='Редактировать', callback_data='edit_self')
edit_other = InlineKeyboardButton(text='Редактировать', callback_data='edit_other')
dont_change = InlineKeyboardButton(text='Оставляем так', callback_data='dont_change')

name = InlineKeyboardButton(text='Имя', callback_data='name')
about = InlineKeyboardButton(text='О себе', callback_data='about')
city = InlineKeyboardButton(text='Город', callback_data='city')
birthdate = InlineKeyboardButton(text='Дата рождения', callback_data='birthdate')
spec_name = InlineKeyboardButton(text='Услуги и описание', callback_data='spec_name')

# Добавление кнопок ---------------------------------------------------------------------------------

Specialties.insert(VNG)
Specialties.insert(Driver)
Specialties.insert(Doctor)
Specialties.insert(Cleaning)
Specialties.insert(Manicurist)
Specialties.insert(Babysitter)
Specialties.insert(Stylist)
Specialties.insert(Psychologist)
Specialties.insert(Serviceman)
Specialties.insert(Tutor)
Specialties.insert(Realtor)

yes_no.insert(yes)
yes_no.insert(no)

save_self.insert(edit_self)
save_self.insert(dont_change)

save_other.insert(edit_other)
save_other.insert(dont_change)

selfabout_fields.insert(name)
selfabout_fields.insert(city)
selfabout_fields.insert(about)
selfabout_fields.insert(birthdate)
selfabout_fields.insert(spec_name)

# Листы ответов ---------------------------------------------------------------------------------


list_yes_no = ['yes', 'no']

list_specialities = ['ВНЖ', 'Водитель', 'Врач', 'Клининг', 'Мастер по маникюру', 'Няня', 'Стилист', 'Психолог',
                     'Мастер по ремонту', 'Преподаватель', 'Риелтор']

list_fields = ['name', 'city', 'about', 'birthdate', 'spec_name']
