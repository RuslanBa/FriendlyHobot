from aiogram import types
from loader import dp, bot, msg_id
from Classes.states_classes import Meeting, Order
from Classes.client_classes import Client, alfa_user
from aiogram.dispatcher.storage import FSMContext
from inline_bottons import yes_no


async def meetings0(message: types.Message):

    if alfa_user.name is None:
        print('нужно спросить имя у пользователя')
        await message.answer('Вижу, мы еще не знакомы. Давайте исправим это. Как вас зовут?')
        await Meeting.Meet_name.set()

    elif alfa_user.city is None:
        print('имя у пользователя знаем, нужно спросить город')
        await message.answer(f'Я уже знаю, что вас зовут - {alfa_user.name}, однако не знают из какого вы города. '
                             'Напишите, ваш город.\n'
                             'Это поможет в будущем показывать вам полезную информацию именно в нем. '
                             'Вы всегда сможете изменить город, просто попросив меня об этом ))')
        await Meeting.Meet_city.set()


@dp.message_handler(state=Meeting.Meet_name)
async def meetings1(message: types.Message, state: FSMContext):
    alfa_user.name = message.text
    alfa_user.change_user_data('user_name', alfa_user.name)

    if alfa_user.city is None:
        await message.answer(f'Хорошо, запомнил ваше имя {alfa_user.name}.\n'
                             f'Напишите, ваш город.\n '
                             'Это поможет в будущем показывать вам полезную информацию именно в нем. В случае, '
                             'если вы переедете или вам понадобится узнать что-то в другом населенном пункте, '
                             'то сможете изменить город, просто попросив меня об этом ))')
        await Meeting.Meet_city.set()

    else:
        await message.answer(f'Отлично, запомнил ваше имя {alfa_user.name}')

        if alfa_user.intent == 'оставить заявку':
            aaa = await message.answer('Теперь давайте перейдем к заявке.\n'
                                       'Я задам вам несколько вопросов, готовы?', reply_markup=yes_no)
            msg_id.append(aaa.message_id)
            await Order.Order_start.set()

        elif alfa_user.intent == 'мои заказы':
            await message.answer('Теперь давайте вернемся к вашим заказам и посмотрим на них:')
            await alfa_user.show_user_orders(message, state)

        else:
            await message.answer('Напишите или выберите вопрос, который вас интересует')
            await state.finish()


@dp.message_handler(state=Meeting.Meet_city)
async def meetings2(message: types.Message, state: FSMContext):
    alfa_user.city = message.text
    alfa_user.change_user_data('city', alfa_user.city)

    await message.answer(f'Отлично, запомнил ваш город {alfa_user.city}')

    if alfa_user.intent == 'оставить заявку':
        aaa = await message.answer('Теперь давайте перейдем к заявке.\n'
                                   'Я задам вам несколько вопросов, готовы?', reply_markup=yes_no)
        msg_id.append(aaa.message_id)
        await Order.Order_start.set()

    elif alfa_user.intent == 'мои заказы':
        await message.answer('Теперь давайте вернемся к вашим заказам и посмотрим на них:')
        await alfa_user.show_user_orders(message, state)

    else:
        await message.answer('Напишите или выберите вопрос, который вас интересует')
        await state.finish()
