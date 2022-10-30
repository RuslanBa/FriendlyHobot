from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
import emoji

# Меню ---------------------------------------------------------------------------------

Specialties = InlineKeyboardMarkup(row_width=1)

# Кнопки ---------------------------------------------------------------------------------

VNG = InlineKeyboardButton(text='ВНЖ', callback_data='VNG')
Driver = InlineKeyboardButton(text='Водители / трансфер', callback_data='driver')
Doctor = InlineKeyboardButton(text='Врачи', callback_data='doctor')
Cleaning = InlineKeyboardButton(text='Клининг / Уборка', callback_data='cleaning')
Manicurist = InlineKeyboardButton(text='Мастера по маникюру', callback_data='manicurist')
Babysitter = InlineKeyboardButton(text='Няни', callback_data='babysitter')
Stylist = InlineKeyboardButton(text='Паракмахеры / стилисты', callback_data='stylist')
Psychologist = InlineKeyboardButton(text='Психологи', callback_data='psychologist')
Serviceman = InlineKeyboardButton(text='Мастера по ремонту', callback_data='serviceman')
Tutor = InlineKeyboardButton(text='Репетиторы / Педагоги', callback_data='tutor')
Realtors = InlineKeyboardButton(text='Риелторы', callback_data='realtors')

# Добавление кнопок ---------------------------------------------------------------------------------

Specialties.insert(VNG)
Specialties.insert(Driver)
Specialties.insert(Doctor)
Specialties.insert(Manicurist)
Specialties.insert(Babysitter)
Specialties.insert(Stylist)
Specialties.insert(Psychologist)
Specialties.insert(Serviceman)
Specialties.insert(Tutor)
Specialties.insert(Realtors)
