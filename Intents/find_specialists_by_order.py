from aiogram import types
from Classes.states_classes import Order, Meeting
from Classes.client_classes import Client, alfa_user
from Classes.order_classes import alfa_order
from loader import bot, dp
# from Intents.dialog import msg_id, delete_dialog
from inline_bottons import Specialties, list_specialities, Driver_menu, Food_services_menu, \
     Beauty_menu, Events_menu, Helper_menu, Repair_menu, Equipment_repair_menu, Tutor_menu, Housekeepers_menu, \
     Photo_video_audio_menu, Language_menu, Lawyer_menu, yes_no, list_yes_no, menu_start
from aiogram.dispatcher.storage import FSMContext
from Intents.meeting_user import meetings0


@dp.callback_query_handler(text='find_offers')
async def start_order(message: types.Message, state: FSMContext):

    await alfa_user.delete_dialog(message)
    await alfa_user.add_alfa_user(message, 'оставить заявку')

    if alfa_user.users[message.from_user.id]['name'] is None or alfa_user.users[message.from_user.id]['city'] is None:
        await meetings0(message)
    else:
        await alfa_user.show_user_orders(message, state)


@dp.callback_query_handler(text=list_yes_no, state=Order.Order_start)
async def make_order(message: types.Message, state: FSMContext):
    text = str(dict(message).get('data'))

    await alfa_user.delete_dialog(message)

    if text == 'yes':
        await alfa_order.add_alfa_order(message)
        aaa = await bot.send_message(message.from_user.id, text='В какой категории вам нужна услуга?',
                                     reply_markup=Specialties)
        await alfa_user.add_msg_id(message, aaa)
        await Order.Order_spec.set()
    else:
        aaa = await bot.send_message(message.from_user.id, text='Давайте вернемся в главное меню))\n'
                                                                'Выберете, что вас интересует', reply_markup=menu_start)
        await alfa_user.add_msg_id(message, aaa)
        await state.finish()


@dp.callback_query_handler(text=list_specialities, state=Order.Order_spec)
async def order_spec(message: types.Message):
    spec_name = str(dict(message).get('data'))

    await alfa_user.delete_dialog(message)

    alfa_order.orders[message.from_user.id]['spec_name'] = spec_name

    if spec_name == 'Водители / перевозки / авто':
        aaa = await bot.send_message(message.from_user.id, 'Выберите подкатегорию', reply_markup=Driver_menu)
        await alfa_user.add_msg_id(message, aaa)

    elif spec_name == 'Доставка и приготовление еды':
        aaa = await bot.send_message(message.from_user.id, 'Выберите подкатегорию', reply_markup=Food_services_menu)
        await alfa_user.add_msg_id(message, aaa)

    elif spec_name == 'Красота и здоровье':
        aaa = await bot.send_message(message.from_user.id, 'Выберите подкатегорию', reply_markup=Beauty_menu)
        await alfa_user.add_msg_id(message, aaa)

    elif spec_name == 'Мероприятия':
        aaa = await bot.send_message(message.from_user.id, 'Выберите подкатегорию', reply_markup=Events_menu)
        await alfa_user.add_msg_id(message, aaa)

    elif spec_name == 'Помощь с детьми и близкими':
        aaa = await bot.send_message(message.from_user.id, 'Выберите подкатегорию', reply_markup=Helper_menu)
        await alfa_user.add_msg_id(message, aaa)

    elif spec_name == 'Ремонт и строительство':
        aaa = await bot.send_message(message.from_user.id, 'Выберите подкатегорию', reply_markup=Repair_menu)
        await alfa_user.add_msg_id(message, aaa)

    elif spec_name == 'Ремонт техники':
        aaa = await bot.send_message(message.from_user.id, 'Выберите подкатегорию', reply_markup=Equipment_repair_menu)
        await alfa_user.add_msg_id(message, aaa)

    elif spec_name == 'Репетиторы и обучение':
        aaa = await bot.send_message(message.from_user.id, 'Выберите подкатегорию', reply_markup=Tutor_menu)
        await alfa_user.add_msg_id(message, aaa)

    elif spec_name == 'Языки':
        aaa = await bot.send_message(message.from_user.id, 'Какой язык вас интересует?', reply_markup=Language_menu)
        await alfa_user.add_msg_id(message, aaa)

    elif spec_name == 'Уборка и помощь по хозяйству':
        aaa = await bot.send_message(message.from_user.id, 'Выберите подкатегорию', reply_markup=Housekeepers_menu)
        await alfa_user.add_msg_id(message, aaa)

    elif spec_name == 'Фото, видео, аудио':
        aaa = await bot.send_message(message.from_user.id, 'Выберите подкатегорию', reply_markup=Photo_video_audio_menu)
        await alfa_user.add_msg_id(message, aaa)

    elif spec_name == 'Юриcты, переводы, бухгалтерия':
        aaa = await bot.send_message(message.from_user.id, 'Выберите подкатегорию', reply_markup=Lawyer_menu)
        await alfa_user.add_msg_id(message, aaa)

    else:
        print('Пользователь хочет оставить заявку на  - ', spec_name)
        bbb = await bot.send_message(message.from_user.id, text='Категорию запомнил\n'
                                                          'Напишите суть задачи, что именно нужно сделать?')
        await alfa_user.add_msg_id(message, bbb)
        await Order.Order_text.set()


@dp.message_handler(state=Order.Order_text)
async def order_text(message: types.Message, state: FSMContext):
    text = message.text
    alfa_order.orders[message.from_user.id]['description'] = text
    alfa_order.save_order(message)
    aaa = await message.answer('Отлично, заявка создана.\n'
                               'Пока она активная, я буду собирать отклики исполнителей на нее и передавать вам.\n'
                               'Вы всегда можете отредактировать заявку или удалить.\n'
                               'А пока, давайте посмотрим на те заявки, которые у вас есть')
    await alfa_user.add_msg_id(message, aaa)
    await alfa_user.show_user_orders(message, state)


@dp.callback_query_handler(text='Назад', state=Order.Order_spec)
async def back_order(message: types.Message, state: FSMContext):

    if alfa_order.orders[message.from_user.id]['spec_name'] is None:
        await alfa_user.delete_dialog(message)
        await bot.send_message(message.from_user.id, text='Давайте вернемся в главное меню))\n'
                                                          'Выберете, что вас интересует', reply_markup=menu_start)
        await state.finish()

    elif alfa_order.orders[message.from_user.id]['spec_name'] in list_specialities:
        alfa_order.orders[message.from_user.id]['spec_name'] = None
        await alfa_user.delete_dialog(message)
        aaa = await bot.send_message(message.from_user.id, text='Выберите категорию:', reply_markup=Specialties)
        await alfa_user.add_msg_id(message, aaa)


@dp.callback_query_handler(text='make_order', state=Order.Order_change)
async def make_order(message: types.Message, state: FSMContext):
    await alfa_user.delete_dialog(message)
    aaa = await bot.send_message(message.from_user.id, text='В какой категории вам нужна услуга?',
                                 reply_markup=Specialties)
    await alfa_user.add_msg_id(message, aaa)

    await alfa_order.add_alfa_order(message)
    await Order.Order_spec.set()
