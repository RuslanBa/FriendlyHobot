from aiogram import types
from loader import dp, bot
# from Intents.dialog import msg_id, delete_dialog
from Classes.states_classes import Meeting, Order, About
from Classes.client_classes import Client, alfa_user
from aiogram.dispatcher.storage import FSMContext
from inline_bottons import yes_no, Specialties
from bottons import menu_main


async def meetings0(message: types.Message):

    if alfa_user.users[message.from_user.id]['name'] is None:
        print('нужно спросить имя у пользователя')
        await message.answer('Вижу, мы еще не знакомы. Давайте исправим это. Как вас зовут?')
        await Meeting.Meet_name.set()

    elif alfa_user.users[message.from_user.id]['city'] is None:
        print('имя у пользователя знаем, нужно спросить город')
        await message.answer(f'Я уже знаю, что вас зовут - {alfa_user.name}, однако не знают из какого вы города. '
                             'Напишите, ваш город.\n'
                             'Это поможет в будущем показывать вам полезную информацию именно в нем. '
                             'Вы всегда сможете изменить город, просто попросив меня об этом ))')
        await Meeting.Meet_city.set()


@dp.message_handler(state=Meeting.Meet_name)
async def meetings1(message: types.Message, state: FSMContext):
    alfa_user.users[message.from_user.id]['name'] = message.text
    alfa_user.change_user_data(message, 'user_name', alfa_user.users[message.from_user.id]['name'])

    if alfa_user.users[message.from_user.id]['city'] is None:
        await message.answer(f'Хорошо, запомнил ваше имя {alfa_user.users[message.from_user.id]["name"]}.\n'
                             f'Напишите, ваш город.\n '
                             'Это поможет в будущем показывать вам полезную информацию именно в нем. В случае, '
                             'если вы переедете или вам понадобится узнать что-то в другом населенном пункте, '
                             'то сможете изменить город, просто попросив меня об этом ))')
        await Meeting.Meet_city.set()

    else:
        await message.answer(f'Отлично, запомнил ваше имя {alfa_user.name}')

        if alfa_user.users[message.from_user.id]['intent'] == 'оставить заявку':
            aaa = await message.answer('Теперь давайте перейдем к заявке.\n'
                                       'Я задам вам несколько вопросов, готовы?', reply_markup=yes_no)
            alfa_user.add_msg_id(message, aaa)
            await Order.Order_start.set()

        elif alfa_user.users[message.from_user.id]['intent'] == 'мои заказы':
            await message.answer('Теперь давайте вернемся к вашим заказам и посмотрим на них:')
            await alfa_user.show_user_orders(message, state)

        elif alfa_user.users[message.from_user.id]['intent'] == 'найти заказы':
            await message.answer(text='Теперь давайте вернемся к поиску заказов', reply_markup=menu_main)
            await message.answer(text='В какой категории услуг вы можете быть полезным другим людям?',
                                 reply_markup=Specialties)
            await About.AB_spec.set()

        else:
            await message.answer('Напишите или выберите вопрос, который вас интересует')
            await state.finish()


@dp.message_handler(state=Meeting.Meet_city)
async def meetings2(message: types.Message, state: FSMContext):
    alfa_user.users[message.from_user.id]['city'] = message.text
    alfa_user.change_user_data(message, 'city', alfa_user.users[message.from_user.id]['city'])

    await message.answer(f'Отлично, запомнил ваш город {alfa_user.users[message.from_user.id]["city"]}')

    if alfa_user.users[message.from_user.id]['intent'] == 'оставить заявку':
        aaa = await message.answer('Теперь давайте перейдем к заявке.\n'
                                   'Я задам вам несколько вопросов, готовы?', reply_markup=yes_no)
        alfa_user.add_msg_id(message, aaa)
        await Order.Order_start.set()

    elif alfa_user.users[message.from_user.id]['intent'] == 'мои заказы':
        await message.answer('Теперь давайте вернемся к вашим заказам и посмотрим на них:')
        await alfa_user.show_user_orders(message, state)

    elif alfa_user.users[message.from_user.id]['intent'] == 'найти заказы':
        await message.answer(text='Теперь давайте вернемся к поиску заказов', reply_markup=menu_main)
        await message.answer(text='В какой категории услуг вы можете быть полезным другим людям?',
                             reply_markup=Specialties)
        await About.AB_spec.set()

    else:
        await message.answer('Напишите или выберите вопрос, который вас интересует')
        await state.finish()
