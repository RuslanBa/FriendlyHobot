from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
import emoji

# Меню ---------------------------------------------------------------------------------

Cities = InlineKeyboardMarkup(row_width=1)
Specialties = InlineKeyboardMarkup(row_width=1)
yes_no = InlineKeyboardMarkup(row_width=1)
save_self = InlineKeyboardMarkup(row_width=1)
save_other = InlineKeyboardMarkup(row_width=1)
selfabout_fields = InlineKeyboardMarkup(row_width=1)


# Кнопки ---------------------------------------------------------------------------------

VNG = InlineKeyboardButton(text='ВНЖ', callback_data='ВНЖ')
Driver = InlineKeyboardButton(text='Водители / трансфер', callback_data='Водитель')
Doctor = InlineKeyboardButton(text='Врачи', callback_data='Врач')
Catering = InlineKeyboardButton(text='Доставка еды', callback_data='Доставка еды')
Cleaning = InlineKeyboardButton(text='Клининг / Уборка', callback_data='Клининг')
Manicurist = InlineKeyboardButton(text='Мастера по маникюру', callback_data='Мастер по маникюру')
Serviceman = InlineKeyboardButton(text='Мастера по ремонту', callback_data='Мастер по ремонту')
Babysitter = InlineKeyboardButton(text='Няни', callback_data='Няня')
Exchange = InlineKeyboardButton(text='Обмен валюты', callback_data='Обмен валюты')
Stylist = InlineKeyboardButton(text='Паракмахеры / стилисты', callback_data='Стилист')
Psychologist = InlineKeyboardButton(text='Психологи', callback_data='Психолог')
Tutor = InlineKeyboardButton(text='Репетиторы / Преподаватели', callback_data='Преподаватель')
Realtor = InlineKeyboardButton(text='Риелторы', callback_data='Риелтор')
Photographer = InlineKeyboardButton(text='Фотографы/Операторы', callback_data='Фотографы/Операторы')
Lawyer = InlineKeyboardButton(text='Юристы', callback_data='Юристы')

yes = InlineKeyboardButton(text='Да', callback_data='yes')
no = InlineKeyboardButton(text='Нет', callback_data='no')

edit_self = InlineKeyboardButton(text='Редактировать', callback_data='edit_self')
edit_other = InlineKeyboardButton(text='Редактировать', callback_data='edit_other')
dont_change = InlineKeyboardButton(text='Оставляем так', callback_data='dont_change')

name = InlineKeyboardButton(text='Имя', callback_data='name')
about = InlineKeyboardButton(text='О себе', callback_data='about')
country = InlineKeyboardButton(text='Страна', callback_data='country')
city = InlineKeyboardButton(text='Город', callback_data='city')
birthdate = InlineKeyboardButton(text='Дата рождения', callback_data='birthdate')
spec_name = InlineKeyboardButton(text='Услуги и описание', callback_data='spec_name')

Buenos_Aires = InlineKeyboardButton(text='Буэнос-Айрес', callback_data='Буэнос-Айрес')


# Добавление кнопок ---------------------------------------------------------------------------------

Specialties.insert(VNG)
Specialties.insert(Driver)
Specialties.insert(Doctor)
Specialties.insert(Catering)
Specialties.insert(Cleaning)
Specialties.insert(Manicurist)
Specialties.insert(Serviceman)
Specialties.insert(Babysitter)
Specialties.insert(Exchange)
Specialties.insert(Stylist)
Specialties.insert(Psychologist)
Specialties.insert(Tutor)
Specialties.insert(Realtor)
Specialties.insert(Photographer)
Specialties.insert(Lawyer)

yes_no.insert(yes)
yes_no.insert(no)

save_self.insert(edit_self)
save_self.insert(dont_change)

save_other.insert(edit_other)
save_other.insert(dont_change)

selfabout_fields.insert(name)
selfabout_fields.insert(country)
selfabout_fields.insert(city)
selfabout_fields.insert(about)
selfabout_fields.insert(birthdate)
selfabout_fields.insert(spec_name)

Cities.insert(Buenos_Aires)

# Листы ответов ---------------------------------------------------------------------------------


list_yes_no = ['yes', 'no']

list_specialities = ['ВНЖ', 'Водитель', 'Врач', 'Доставка еды', 'Клининг', 'Мастер по маникюру', 'Няня',
                     'Обмен валюты', 'Стилист', 'Психолог', 'Мастер по ремонту', 'Преподаватель', 'Риелтор',
                     'Фотографы/Операторы', 'Юристы']

list_fields = ['name', 'country', 'city', 'about', 'birthdate', 'spec_name']

list_cities = ['Буэнос-Айрес']
