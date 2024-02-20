from aiogram import types
from Classes.states_classes import Order, Meeting
from Classes.client_classes import alfa_user
from Classes.order_classes import alfa_order
from bottons import menu_start, menu_main
from loader import bot, dp, msg_id
from inline_bottons import Specialties, list_specialities, Driver_menu, Food_services_menu, \
     Beauty_menu, Events_menu, Helper_menu, Repair_menu, Equipment_repair_menu, Tutor_menu, Housekeepers_menu, \
     Photo_video_audio_menu, Language_menu, Lawyer_menu, yes_no, list_yes_no
from aiogram.dispatcher.storage import FSMContext
from Intents.meeting_user import meetings0


@dp.message_handler(text='Найти исполнителя')
async def start_order(message: types.Message):

    alfa_user.intent = 'оставить заявку'
    alfa_user.update_alfa_user(message, alfa_user.intent)

    await message.answer('Вы можете оставить заявку с указанием того, кто вам нужен и на каких условиях.\n'
                         'Я самостоятельно подберу потенциальных исполнителей и отправлю им ваш запрос\n\n',
                         reply_markup=menu_main)

    if alfa_user.name is None or alfa_user.city is None:
        await meetings0(message)

    else:
        aaa = await message.answer('Я задам вам несколько вопросов, готовы?', reply_markup=yes_no)
        msg_id.append(aaa.message_id)
        await Order.Order_start.set()


@dp.callback_query_handler(text=list_yes_no, state=Order.Order_start)
async def make_order(message: types.Message, state: FSMContext):
    text = str(dict(message).get('data'))

    await bot.delete_message(message.from_user.id, message_id=int(msg_id[0]))
    msg_id.clear()

    if text == 'yes':
        aaa = await bot.send_message(message.from_user.id, text='В какой категории вам нужна услуга?',
                                     reply_markup=Specialties)
        msg_id.append(aaa.message_id)

        alfa_order.tg_username = message.from_user.username
        alfa_order.city = alfa_user.city
        alfa_order.id_user = alfa_user.id_user

        await Order.Order_spec.set()
    else:
        await bot.send_message(message.from_user.id, text='Давайте вернемся в главное меню))\n'
                                                          'Выберете, что вас интересует', reply_markup=menu_start)
        await state.finish()


@dp.callback_query_handler(text=list_specialities, state=Order.Order_spec)
async def order_spec(message: types.Message):
    spec_name = str(dict(message).get('data'))

    if msg_id:
        await bot.delete_message(message.from_user.id, message_id=int(msg_id[0]))
        msg_id.clear()

    alfa_order.spec_name = spec_name

    if spec_name == 'Водители / перевозки / авто':
        aaa = await bot.send_message(message.from_user.id, 'Выберите подкатегорию', reply_markup=Driver_menu)
        msg_id.append(aaa.message_id)

    elif spec_name == 'Доставка и приготовление еды':
        aaa = await bot.send_message(message.from_user.id, 'Выберите подкатегорию', reply_markup=Food_services_menu)
        msg_id.append(aaa.message_id)

    elif spec_name == 'Красота и здоровье':
        aaa = await bot.send_message(message.from_user.id, 'Выберите подкатегорию', reply_markup=Beauty_menu)
        msg_id.append(aaa.message_id)

    elif spec_name == 'Мероприятия':
        aaa = await bot.send_message(message.from_user.id, 'Выберите подкатегорию', reply_markup=Events_menu)
        msg_id.append(aaa.message_id)

    elif spec_name == 'Помощь с детьми и близкими':
        aaa = await bot.send_message(message.from_user.id, 'Выберите подкатегорию', reply_markup=Helper_menu)
        msg_id.append(aaa.message_id)

    elif spec_name == 'Ремонт и строительство':
        aaa = await bot.send_message(message.from_user.id, 'Выберите подкатегорию', reply_markup=Repair_menu)
        msg_id.append(aaa.message_id)

    elif spec_name == 'Ремонт техники':
        aaa = await bot.send_message(message.from_user.id, 'Выберите подкатегорию', reply_markup=Equipment_repair_menu)
        msg_id.append(aaa.message_id)

    elif spec_name == 'Репетиторы и обучение':
        aaa = await bot.send_message(message.from_user.id, 'Выберите подкатегорию', reply_markup=Tutor_menu)
        msg_id.append(aaa.message_id)

    elif spec_name == 'Языки':
        aaa = await bot.send_message(message.from_user.id, 'Какой язык вас интересует?', reply_markup=Language_menu)
        msg_id.append(aaa.message_id)

    elif spec_name == 'Уборка и помощь по хозяйству':
        aaa = await bot.send_message(message.from_user.id, 'Выберите подкатегорию', reply_markup=Housekeepers_menu)
        msg_id.append(aaa.message_id)

    elif spec_name == 'Фото, видео, аудио':
        aaa = await bot.send_message(message.from_user.id, 'Выберите подкатегорию', reply_markup=Photo_video_audio_menu)
        msg_id.append(aaa.message_id)

    elif spec_name == 'Юриcты, переводы, бухгалтерия':
        aaa = await bot.send_message(message.from_user.id, 'Выберите подкатегорию', reply_markup=Lawyer_menu)
        msg_id.append(aaa.message_id)

    else:
        print('Пользователь хочет оставить заявку на  - ', spec_name)
        await bot.send_message(message.from_user.id, text='Категорию запомнил\n'
                                                          'Напишите суть задачи, что именно нужно сделать?')
        await Order.Order_text.set()


@dp.message_handler(state=Order.Order_text)
async def order_text(message: types.Message, state: FSMContext):
    text = message.text
    alfa_order.description = text
    alfa_order.save_order()
    await message.answer('Отлично, заявка создана.\n'
                         'Пока она активная, я буду собирать отклики исполнителей на нее и передавать вам.\n'
                         'Вы всегда можете отредактировать заявку или удалить.\n'
                         'А пока, давайте посмотрим на те заявки, которые у вас есть')
    await alfa_user.show_user_orders(message, state)


@dp.callback_query_handler(text='Назад', state=Order.Order_spec)
async def back_order(message: types.Message, state: FSMContext):

    if alfa_order.spec_name is None:
        await bot.delete_message(message.from_user.id, message_id=int(msg_id[0]))
        msg_id.clear()
        await bot.send_message(message.from_user.id, text='Давайте вернемся в главное меню))\n'
                                                          'Выберете, что вас интересует', reply_markup=menu_start)
        await state.finish()

    elif alfa_order.spec_name in list_specialities:
        alfa_order.spec_name = None
        await bot.delete_message(message.from_user.id, message_id=int(msg_id[0]))
        aaa = await bot.send_message(message.from_user.id, text='Выберите категорию:', reply_markup=Specialties)
        msg_id.clear()
        msg_id.append(aaa.message_id)
