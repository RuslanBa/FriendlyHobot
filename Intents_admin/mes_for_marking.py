from loader import dp, admin_id, bot
# from Intents.dialog import msg_id
from aiogram import types
from aiogram.dispatcher.storage import FSMContext
from inline_bottons import edit_intent_btn, intents_first, list_marking, Specialties, list_specialities, Driver_menu, \
    Food_services_menu, Beauty_menu, Events_menu, Helper_menu, Repair_menu, Equipment_repair_menu, Tutor_menu, \
    Housekeepers_menu, Photo_video_audio_menu, Language_menu, Lawyer_menu, admin_buttons, list_final_intents, menu_start
from DB.find_table_names_db import find_table_names_db
from DB.find_mes_for_marking_db import find_mes_for_marking_db
from DB.save_intent_db import save_intent_db
from DB.find_spec_id_by_spec_name import find_spec_id
from Classes.message_classes import Message, mark_message
from Classes.states_classes import Marking
from Classes.client_classes import alfa_user


@dp.callback_query_handler(text='message_for_marking')
async def marking1(message: types.Message, state: FSMContext):
    user_id = message.from_user.id
    if user_id not in admin_id:
        await bot.send_message(message.from_user.id,
                               text='Вы заставили меня задуматься, отправляю вас в главное меню',
                               reply_markup=menu_start)
        await state.finish()
    else:
        table_names = find_table_names_db()
        mes_for_marking = find_mes_for_marking_db(table_names)

        await bot.send_message(message.from_user.id,
                               text='Это случайное сообщение, для которого не проставлен или не проверен интент.\n')

        for messages in mes_for_marking:
            mes_id = messages[0]
            mes_text = messages[6]
            table_name = str(messages[11])+'_'+str(messages[1])
            intent = messages[8]

            await bot.send_message(message.from_user.id,
                                   text=f'>>>> Текст:\n\n'
                                        f'{mes_text}\n\n'
                                        f'>>>> Интент: {intent}',
                                   reply_markup=edit_intent_btn(table_name, mes_id))


@dp.callback_query_handler(text_startswith='btn-intent')
async def marking2(message: types.Message, state: FSMContext):
    text = str(dict(message).get('data'))
    data = text.split('-')
    print('data = ', data)

    await mark_message.add_message(message)
    mark_message.messages[message.from_user.id]['table_name'] = str(data[3])
    mark_message.messages[message.from_user.id]['mes_id'] = data[4]
    aaa = await bot.send_message(message.from_user.id, text='Выбери интент для этого сообщения',
                                 reply_markup=intents_first)
    await alfa_user.delete_dialog(message)
    await alfa_user.add_msg_id(message, aaa)
    await Marking.Marking_needs.set()


@dp.callback_query_handler(text=list_final_intents, state=Marking.Marking_needs)
async def marking3(message: types.Message, state: FSMContext):
    mark_message.messages[message.from_user.id]['intent'] = str(dict(message).get('data'))
    save_intent_db(mark_message.messages[message.from_user.id]['table_name'],
                   mark_message.messages[message.from_user.id]['mes_id'],
                   mark_message.messages[message.from_user.id]['intent'],
                   mark_message.messages[message.from_user.id]['spec_id'])

    await alfa_user.delete_dialog(message)

    await bot.send_message(message.from_user.id, text='Готово, запомнил интент. Выбери следующее действие',
                           reply_markup=admin_buttons)
    await state.finish()


@dp.callback_query_handler(text=list_marking, state=Marking.Marking_needs)
async def marking4(message: types.Message, state: FSMContext):
    mark_message.messages[message.from_user.id]['intent'] = str(dict(message).get('data'))

    await alfa_user.delete_dialog(message)

    aaa = await bot.send_message(message.from_user.id, text='Выберите категорию', reply_markup=Specialties)
    await alfa_user.add_msg_id(message, aaa)


@dp.callback_query_handler(text=list_specialities, state=Marking.Marking_needs)
async def marking5(message: types.Message, state: FSMContext):
    spec_name = str(dict(message).get('data'))

    await alfa_user.delete_dialog(message)

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
        mark_message.messages[message.from_user.id]['spec_id'] = find_spec_id(spec_name)
        save_intent_db(mark_message.messages[message.from_user.id]['table_name'],
                       mark_message.messages[message.from_user.id]['mes_id'],
                       mark_message.messages[message.from_user.id]['intent'],
                       mark_message.messages[message.from_user.id]['spec_id'])

        await bot.send_message(message.from_user.id, text='Готово, запомнил интент. Выбери следующее действие',
                               reply_markup=admin_buttons)
        await state.finish()


@dp.callback_query_handler(text='Назад', state=Marking.Marking_needs)
async def back_func(message: types.Message, state: FSMContext):

    await alfa_user.delete_dialog(message)

    aaa = await bot.send_message(message.from_user.id, text='Выбери интент для этого сообщения',
                                 reply_markup=intents_first)
    await alfa_user.add_msg_id(message, aaa)
