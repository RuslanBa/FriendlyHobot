from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
import emoji

# Menu ---------------------------------------------------------------------------------

admin_buttons = InlineKeyboardMarkup(row_width=1)
Cities = InlineKeyboardMarkup(row_width=1)
dont_change_menu = InlineKeyboardMarkup(row_width=1)
intents_first = InlineKeyboardMarkup(row_width=1)
feedback = InlineKeyboardMarkup(row_width=1)
finish_orders = InlineKeyboardMarkup(row_width=1)
save_self = InlineKeyboardMarkup(row_width=2)
save_other = InlineKeyboardMarkup(row_width=2)
selfabout_fields = InlineKeyboardMarkup(row_width=1)
users_identifiers = InlineKeyboardMarkup(row_width=1)
yes_no = InlineKeyboardMarkup(row_width=1)


# Menu of specialities ---------------------------------------------------------------------------------

Specialties = InlineKeyboardMarkup(row_width=1)

Driver_menu = InlineKeyboardMarkup(row_width=1)
Food_services_menu = InlineKeyboardMarkup(row_width=1)
Beauty_menu = InlineKeyboardMarkup(row_width=1)
Events_menu = InlineKeyboardMarkup(row_width=1)
Helper_menu = InlineKeyboardMarkup(row_width=1)
Repair_menu = InlineKeyboardMarkup(row_width=1)
Equipment_repair_menu = InlineKeyboardMarkup(row_width=1)
Tutor_menu = InlineKeyboardMarkup(row_width=1)
Housekeepers_menu = InlineKeyboardMarkup(row_width=1)
Photo_video_audio_menu = InlineKeyboardMarkup(row_width=1)
Lawyer_menu = InlineKeyboardMarkup(row_width=1)

Language_menu = InlineKeyboardMarkup(row_width=1)


# Кнопки меню профессий 1 уровень ---------------------------------------------------------------------------

Realtor = InlineKeyboardButton(text='Аренда и продажа недвижимости', callback_data='Аренда и продажа недвижимости')
Driver = InlineKeyboardButton(text='Водители / перевозки / авто', callback_data='Водители / перевозки / авто')
Food_services = InlineKeyboardButton(text='Доставка и приготовление еды', callback_data='Доставка и приготовление еды')
Beauty = InlineKeyboardButton(text='Красота и здоровье', callback_data='Красота и здоровье')
Events = InlineKeyboardButton(text='Мероприятия', callback_data='Мероприятия')
Exchange = InlineKeyboardButton(text='Обмен валюты', callback_data='Обмен валюты')
Helper = InlineKeyboardButton(text='Помощь с детьми и близкими', callback_data='Помощь с детьми и близкими')
Repair = InlineKeyboardButton(text='Ремонт и строительство', callback_data='Ремонт и строительство')
Equipment_repair = InlineKeyboardButton(text='Ремонт техники', callback_data='Ремонт техники')
Tutor = InlineKeyboardButton(text='Репетиторы и обучение', callback_data='Репетиторы и обучение')
Housekeepers = InlineKeyboardButton(text='Уборка и помощь по хозяйству', callback_data='Уборка и помощь по хозяйству')
Photo_video_audio = InlineKeyboardButton(text='Фото, видео, аудио', callback_data='Фото, видео, аудио')
Lawyer = InlineKeyboardButton(text='Юриcты, переводы, бухгалтерия', callback_data='Юриcты, переводы, бухгалтерия')


# Beauty menu buttons ----------------------------------------------------------------------------------------

Beauticians = InlineKeyboardButton(text='Косметологи', callback_data='Косметологи')
Epilation = InlineKeyboardButton(text='Эпиляция', callback_data='Эпиляция')
Eyebrows_eyelashes = InlineKeyboardButton(text='Брови и ресницы', callback_data='Брови и ресницы')
Make_up = InlineKeyboardButton(text='Визажисты', callback_data='Визажисты')
Tatu = InlineKeyboardButton(text='Тату и пирсинг', callback_data='Тату и пирсинг')
Stylist = InlineKeyboardButton(text='Парикмахеры, стилисты', callback_data='Парикмахеры, стилисты')
Manicurist = InlineKeyboardButton(text='Маникюр', callback_data='Маникюр')
Massage = InlineKeyboardButton(text='Массаж', callback_data='Массаж')
Psychologist = InlineKeyboardButton(text='Психологи и психотерапевты', callback_data='Психологи и психотерапевты')
Personal_trainer = InlineKeyboardButton(text='Персональные тренеры', callback_data='Персональные тренеры')
Other_beauty = InlineKeyboardButton(text='Другие бьюти услуги', callback_data='Другие бьюти услуги')


# Repair menu buttons ----------------------------------------------------------------------------------------

Serviceman = InlineKeyboardButton(text='Мастера на час', callback_data='Мастера на час')
Furniture_assembly = InlineKeyboardButton(text='Сборка и ремонт мебели', callback_data='Сборка и ремонт мебели')
House_repair = InlineKeyboardButton(text='Ремонт квартир и домов', callback_data='Ремонт квартир и домов')
Other_repair = InlineKeyboardButton(text='Другие работы', callback_data='Другие работы')


# Tutors menu buttons ----------------------------------------------------------------------------------------

Languages = InlineKeyboardButton(text='Языки', callback_data='Языки')
Mathematics_physics = InlineKeyboardButton(text='Математика и физика', callback_data='Математика и физика')
Biology_chemistry = InlineKeyboardButton(text='Биология и химия', callback_data='Биология и химия')
History_social_science = InlineKeyboardButton(text='История и обществознание', callback_data='История и обществознание')
Geography_economics = InlineKeyboardButton(text='География и экономика', callback_data='География и экономика')
Computer_science = InlineKeyboardButton(text='Информатика и программирование',
                                        callback_data='Информатика и программирование')
Preparation_for_school = InlineKeyboardButton(text='Подготовка к школе', callback_data='Подготовка к школе')
Music_dance_art = InlineKeyboardButton(text='Музыка, танцы и арт', callback_data='Музыка, танцы и арт')
Speech_therapists = InlineKeyboardButton(text='Логопеды', callback_data='Логопеды')
Sport = InlineKeyboardButton(text='Спорт', callback_data='Спорт')
Other_tutors = InlineKeyboardButton(text='Другие преподаватели и тренера',
                                    callback_data='Другие преподаватели и тренера')


# Housekeepers menu buttons ----------------------------------------------------------------------------------------

Cleaning = InlineKeyboardButton(text='Уборка в квартире и в доме', callback_data='Уборка в квартире и в доме')
Sanitary = InlineKeyboardButton(text='Санитарные работы', callback_data='Санитарные работы')
Trash = InlineKeyboardButton(text='Вынос мусора', callback_data='Вынос мусора')
Seamstress = InlineKeyboardButton(text='Помощь швеи', callback_data='Помощь швеи')
Ironing = InlineKeyboardButton(text='Глажение белья', callback_data='Глажение белья')
Garden = InlineKeyboardButton(text='Работы в саду, на участке', callback_data='Работы в саду, на участке')
Window_cleaning = InlineKeyboardButton(text='Мытье окон', callback_data='Мытье окон')
Other_housekeepers = InlineKeyboardButton(text='Другие работы по дому', callback_data='Другие работы по дому')


# Food delivery menu buttons ----------------------------------------------------------------------------------------

Catering_ready = InlineKeyboardButton(text='Доставка готовой еды', callback_data='Доставка готовой еды')
Cooking = InlineKeyboardButton(text='Приготовление еды дома', callback_data='Приготовление еды дома')
Catering = InlineKeyboardButton(text='Кейтеринг', callback_data='Кейтеринг')
Other_food_delivery = InlineKeyboardButton(text='Другие услуги с едой', callback_data='Другие услуги с едой')


# Drivers menu buttons ----------------------------------------------------------------------------------------

Trucking = InlineKeyboardButton(text='Грузоперевозки', callback_data='Грузоперевозки')
Transfer = InlineKeyboardButton(text='Трансферы', callback_data='Трансферы')
Rent_auto = InlineKeyboardButton(text='Прокат авто', callback_data='Прокат авто')
Other_drivers = InlineKeyboardButton(text='Другие авто услуги', callback_data='Другие авто услуги')


# Lawyer menu buttons ----------------------------------------------------------------------------------------

Legalization = InlineKeyboardButton(text='Помощь в легализации', callback_data='Помощь в легализации')
Translators = InlineKeyboardButton(text='Переводчики и нотариусы', callback_data='Переводчики и нотариусы')
Bankruptcy = InlineKeyboardButton(text='Услуги по банкротству', callback_data='Услуги по банкротству')
Bank_services = InlineKeyboardButton(text='Банковские услуги', callback_data='Банковские услуги')
Other_lawyer = InlineKeyboardButton(text='Другие юр. и бух. услуги', callback_data='Другие юр. и бух. услуги')


# Events menu buttons ----------------------------------------------------------------------------------------

Animators = InlineKeyboardButton(text='Ведущие и аниматоры', callback_data='Ведущие и аниматоры')
Events_help = InlineKeyboardButton(text='Помощь на мероприятиях', callback_data='Помощь на мероприятиях')


# Equipment_repair menu buttons --------------------------------------------------------------------------------------

Phone_repair = InlineKeyboardButton(text='Планшеты и телефоны', callback_data='Планшеты и телефоны')
Computer_repair = InlineKeyboardButton(text='Компьютеры и ноутбуки', callback_data='Компьютеры и ноутбуки')
Appliances_repair = InlineKeyboardButton(text='Бытовая техника', callback_data='Бытовая техника')


# Photo_video_audio menu buttons ----------------------------------------------------------------------------------

Photography = InlineKeyboardButton(text='Фотосъемка', callback_data='Фотосъемка')
Videography = InlineKeyboardButton(text='Видеосъемка', callback_data='Видеосъемка')
Video_editing = InlineKeyboardButton(text='Монтаж видео', callback_data='Монтаж видео')
Photo_editing = InlineKeyboardButton(text='Обработка фотографий', callback_data='Обработка фотографий')
Other_foto_video = InlineKeyboardButton(text='Другие фото-видео-аудио услуги',
                                        callback_data='Другие фото-видео-аудио услуги')


# Helpers menu buttons ----------------------------------------------------------------------------------

Babysitter = InlineKeyboardButton(text='Няни', callback_data='Няни')
Nurse = InlineKeyboardButton(text='Сиделки', callback_data='Сиделки')
Dog_walking = InlineKeyboardButton(text='Выгул собак', callback_data='Выгул собак')
Animal_care = InlineKeyboardButton(text='Уход за животными', callback_data='Уход за животными')
Other_helpers = InlineKeyboardButton(text='Другая помощь с близкими', callback_data='Другая помощь с близкими')


# Languages menu buttons ----------------------------------------------------------------------------------

Russian = InlineKeyboardButton(text='Русский язык и литература', callback_data='Русский язык и литература')
English = InlineKeyboardButton(text='Английский', callback_data='Английский')
Spanish = InlineKeyboardButton(text='Испанский', callback_data='Испанский')
Turkish = InlineKeyboardButton(text='Турецкий', callback_data='Турецкий')
Other_languages = InlineKeyboardButton(text='Другие языки', callback_data='Другие языки')


# Intents_first menu buttons ----------------------------------------------------------------------------------

Need_specialist = InlineKeyboardButton(text='Ищу специалиста', callback_data='need_specialist')
Suggest_service = InlineKeyboardButton(text='Предлагаю услугу', callback_data='suggest_service')
Need_buy = InlineKeyboardButton(text='Хочет купить', callback_data='need_buy')
Need_sell = InlineKeyboardButton(text='Хочет продать', callback_data='need_sell')
None_target = InlineKeyboardButton(text='Нецелевой', callback_data='none_target')


# Other buttons ----------------------------------------------------------------------------------------

yes = InlineKeyboardButton(text='Да', callback_data='yes')
no = InlineKeyboardButton(text='Нет', callback_data='no')

edit_self = InlineKeyboardButton(text='Изменить данные', callback_data='edit_self')
edit_other = InlineKeyboardButton(text='Изменить данные', callback_data='edit_other')
dont_change = InlineKeyboardButton(text='Оставляем так', callback_data='dont_change')

name = InlineKeyboardButton(text='Имя', callback_data='name')
about = InlineKeyboardButton(text='О себе', callback_data='about')
country = InlineKeyboardButton(text='Страна', callback_data='country')
city = InlineKeyboardButton(text='Город', callback_data='city')
birthdate = InlineKeyboardButton(text='Дата рождения', callback_data='birthdate')
spec_name = InlineKeyboardButton(text='Добавить услугу', callback_data='spec_name')

Buenos_Aires = InlineKeyboardButton(text='Буэнос-Айрес', callback_data='Буэнос-Айрес')
Puerto_Iguazu = InlineKeyboardButton(text='Пуэрто-Игуасу', callback_data='Пуэрто-Игуасу')

tg = InlineKeyboardButton(text='Telegram id', callback_data='Telegram id')
phone = InlineKeyboardButton(text='Телефон', callback_data='Телефон')

feedback_button = InlineKeyboardButton(text='Написать разработчикам', callback_data='Написать разработчикам')

back_button = InlineKeyboardButton(text='⏪⏪⏪ Назад', callback_data='Назад')

message_for_marking = InlineKeyboardButton(text='Сообщения для маркировки', callback_data='message_for_marking')
orders_users = InlineKeyboardButton(text='Заявки пользователей (не работает)', callback_data='orders_users')
stats = InlineKeyboardButton(text='Статистика базы', callback_data='stats')

make_order = InlineKeyboardButton(text='Создать заявку', callback_data='make_order')

# Добавление кнопок ---------------------------------------------------------------------------------

Specialties.insert(Realtor)
Specialties.insert(Driver)
Specialties.insert(Food_services)
Specialties.insert(Beauty)
Specialties.insert(Events)
Specialties.insert(Exchange)
Specialties.insert(Helper)
Specialties.insert(Repair)
Specialties.insert(Equipment_repair)
Specialties.insert(Tutor)
Specialties.insert(Housekeepers)
Specialties.insert(Photo_video_audio)
Specialties.insert(Lawyer)
Specialties.insert(back_button)

Driver_menu.insert(Trucking)
Driver_menu.insert(Transfer)
Driver_menu.insert(Rent_auto)
Driver_menu.insert(Other_drivers)
Driver_menu.insert(back_button)

Food_services_menu.insert(Catering_ready)
Food_services_menu.insert(Cooking)
Food_services_menu.insert(Catering)
Food_services_menu.insert(Other_food_delivery)
Food_services_menu.insert(back_button)

Beauty_menu.insert(Beauticians)
Beauty_menu.insert(Epilation)
Beauty_menu.insert(Eyebrows_eyelashes)
Beauty_menu.insert(Make_up)
Beauty_menu.insert(Tatu)
Beauty_menu.insert(Stylist)
Beauty_menu.insert(Manicurist)
Beauty_menu.insert(Massage)
Beauty_menu.insert(Psychologist)
Beauty_menu.insert(Personal_trainer)
Beauty_menu.insert(Other_beauty)
Beauty_menu.insert(back_button)

Events_menu.insert(Animators)
Events_menu.insert(Events_help)
Events_menu.insert(back_button)

Helper_menu.insert(Babysitter)
Helper_menu.insert(Nurse)
Helper_menu.insert(Dog_walking)
Helper_menu.insert(Animal_care)
Helper_menu.insert(Other_helpers)
Helper_menu.insert(back_button)

Repair_menu.insert(Serviceman)
Repair_menu.insert(Furniture_assembly)
Repair_menu.insert(House_repair)
Repair_menu.insert(Other_repair)
Repair_menu.insert(back_button)

Equipment_repair_menu.insert(Phone_repair)
Equipment_repair_menu.insert(Computer_repair)
Equipment_repair_menu.insert(Appliances_repair)
Equipment_repair_menu.insert(back_button)

Tutor_menu.insert(Languages)
Tutor_menu.insert(Mathematics_physics)
Tutor_menu.insert(Biology_chemistry)
Tutor_menu.insert(History_social_science)
Tutor_menu.insert(Geography_economics)
Tutor_menu.insert(Computer_science)
Tutor_menu.insert(Preparation_for_school)
Tutor_menu.insert(Music_dance_art)
Tutor_menu.insert(Speech_therapists)
Tutor_menu.insert(Sport)
Tutor_menu.insert(Other_tutors)
Tutor_menu.insert(back_button)

Housekeepers_menu.insert(Cleaning)
Housekeepers_menu.insert(Sanitary)
Housekeepers_menu.insert(Trash)
Housekeepers_menu.insert(Seamstress)
Housekeepers_menu.insert(Ironing)
Housekeepers_menu.insert(Garden)
Housekeepers_menu.insert(Window_cleaning)
Housekeepers_menu.insert(Other_housekeepers)
Housekeepers_menu.insert(back_button)

Photo_video_audio_menu.insert(Photography)
Photo_video_audio_menu.insert(Videography)
Photo_video_audio_menu.insert(Video_editing)
Photo_video_audio_menu.insert(Photo_editing)
Photo_video_audio_menu.insert(Other_foto_video)
Photo_video_audio_menu.insert(back_button)

Lawyer_menu.insert(Translators)
Lawyer_menu.insert(Legalization)
Lawyer_menu.insert(Bank_services)
Lawyer_menu.insert(Bankruptcy)
Lawyer_menu.insert(Other_lawyer)
Lawyer_menu.insert(back_button)

Language_menu.insert(Russian)
Language_menu.insert(English)
Language_menu.insert(Spanish)
Language_menu.insert(Turkish)
Language_menu.insert(Other_languages)
Language_menu.insert(back_button)

yes_no.insert(yes)
yes_no.insert(no)

save_self.insert(edit_self)
save_self.insert(spec_name)

save_other.insert(edit_other)
save_other.insert(spec_name)

dont_change_menu.insert(dont_change)

selfabout_fields.insert(name)
selfabout_fields.insert(country)
selfabout_fields.insert(city)
selfabout_fields.insert(about)
selfabout_fields.insert(birthdate)
selfabout_fields.insert(phone)

Cities.insert(Buenos_Aires)

users_identifiers.insert(tg)
users_identifiers.insert(phone)

feedback.insert(feedback_button)

admin_buttons.insert(message_for_marking)
admin_buttons.insert(orders_users)
admin_buttons.insert(stats)

intents_first.insert(Suggest_service)
intents_first.insert(Need_specialist)
intents_first.insert(Need_buy)
intents_first.insert(Need_sell)
intents_first.insert(None_target)

finish_orders.insert(dont_change)
finish_orders.insert(make_order)


# Листы ответов ---------------------------------------------------------------------------------

list_identifiers = ['Telegram id', 'Телефон']

list_yes_no = ['yes', 'no']

list_specialities = ['Аренда и продажа недвижимости', 'Водители / перевозки / авто', 'Доставка и приготовление еды',
                     'Красота и здоровье', 'Мероприятия', 'Обмен валюты', 'Помощь с детьми и близкими',
                     'Ремонт и строительство', 'Ремонт техники', 'Репетиторы и обучение',
                     'Уборка и помощь по хозяйству', 'Фото, видео, аудио', 'Юриcты, переводы, бухгалтерия',
                     'Косметологи', 'Эпиляция', 'Брови и ресницы', 'Визажисты', 'Тату и пирсинг',
                     'Парикмахеры, стилисты', 'Маникюр', 'Массаж', 'Психологи и психотерапевты',
                     'Персональные тренеры', 'Другие бьюти услуги',
                     'Мастера на час', 'Сборка и ремонт мебели', 'Ремонт квартир и домов', 'Другие работы',
                     'Языки', 'Математика и физика', 'Биология и химия', 'История и обществознание',
                     'География и экономика', 'Информатика и программирование', 'Подготовка к школе',
                     'Музыка, танцы и арт', 'Логопеды', 'Спорт', 'Другие преподаватели и тренера',
                     'Уборка в квартире и в доме', 'Санитарные работы', 'Вынос мусора', 'Помощь швеи', 'Глажение белья',
                     'Работы в саду, на участке', 'Мытье окон', 'Другие работы по дому',
                     'Доставка готовой еды', 'Приготовление еды дома', 'Кейтеринг', 'Другие услуги с едой',
                     'Грузоперевозки', 'Трансферы', 'Прокат авто', 'Другие авто услуги',
                     'Помощь в легализации', 'Другие юр. и бух. услуги', 'Банковские услуги',
                     'Переводчики и нотариусы', 'Услуги по банкротству',
                     'Ведущие и аниматоры', 'Помощь на мероприятиях',
                     'Планшеты и телефоны', 'Компьютеры и ноутбуки', 'Бытовая техника',
                     'Фотосъемка', 'Видеосъемка', 'Монтаж видео', 'Обработка фотографий',
                     'Другие фото-видео-аудио услуги',
                     'Няни', 'Сиделки', 'Выгул собак', 'Уход за животными', 'Другая помощь с близкими',
                     'Русский язык и литература', 'Английский', 'Испанский', 'Турецкий', 'Другие языки']


list_driver_menu = ['']


list_self = ['name', 'country', 'city', 'about', 'birthdate', 'Телефон']

list_cities = ['Буэнос-Айрес', 'Пуэрто-Игуасу']

list_marking = ['suggest_service', 'need_specialist']

list_final_intents = ['need_sell', 'need_buy', 'none_target']


# Программируемые кнопки ---------------------------------------------------------------------------------

def edit_services_btn(service_id, id_user, spec_id):

    edit_spec = InlineKeyboardMarkup(row_width=2)

    btn_edit = f'btn_edit_{service_id}_{spec_id}_{id_user}'
    btn_delete = f'btn_delete_{service_id}_{spec_id}_{id_user}'
    btn_find_orders = f'btn_find_orders_{service_id}_{spec_id}_{id_user}'

    print('Выведены кнопки ', btn_edit, btn_delete, btn_find_orders)

    delete_one_spec = InlineKeyboardButton(text='Удалить услугу', callback_data=btn_delete)
    edit_one_spec = InlineKeyboardButton(text='Изменить описание', callback_data=btn_edit)
    find_orders = InlineKeyboardButton(text='⭐️ Посмотреть заявки', callback_data=btn_find_orders)

    edit_spec.insert(delete_one_spec)
    edit_spec.insert(edit_one_spec)
    edit_spec.insert(find_orders)

    return edit_spec


def edit_order_btn(order_id, id_user):

    edit_order = InlineKeyboardMarkup(row_width=2)

    btn_order_edit = f'btn_order_edit_{order_id}_{id_user}'
    btn_order_delete = f'btn_order_delete_{order_id}_{id_user}'

    print('Выведены кнопки ', btn_order_edit, btn_order_delete)

    delete_one_order = InlineKeyboardButton(text='Удалить заявку', callback_data=btn_order_delete)
    edit_one_order = InlineKeyboardButton(text='Изменить заявку', callback_data=btn_order_edit)

    edit_order.insert(delete_one_order)
    edit_order.insert(edit_one_order)

    return edit_order


def edit_intent_btn(table_name, mes_id):

    edit_intent = InlineKeyboardMarkup(row_width=1)
    btn_intent_edit = f'btn-intent-edit-{table_name}-{mes_id}'
    print('Show button ', btn_intent_edit)

    edit_one_intent = InlineKeyboardButton(text='Изменить интент', callback_data=btn_intent_edit)
    edit_intent.insert(edit_one_intent)

    return edit_intent
