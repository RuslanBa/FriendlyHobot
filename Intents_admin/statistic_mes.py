from loader import dp, admin_id, bot
from aiogram import types
from aiogram.dispatcher.storage import FSMContext
from bottons import menu_main, menu_start
from DB.statistic_db import statistic_mes
from DB.find_table_names_db import find_table_names_db


@dp.callback_query_handler(text='stats')
async def marking1(message: types.Message, state: FSMContext):
    user_id = message.from_user.id
    if user_id not in admin_id:
        await bot.send_message(message.from_user.id,
                               text='Вы заставили меня задуматься, отправляю вас в главное меню',
                               reply_markup=menu_start)
        await state.finish()
    else:
        table_names = find_table_names_db()
        stats = statistic_mes(table_names)
        num_channels = len(table_names)
        all_mes = stats[0]
        checked_admin = stats[1]
        checked_intent = stats[2]
        stat_specs = stats[3]

        await bot.send_message(message.from_user.id,
                               text='Cтатистика на текущий момент:\n\n'
                                    f'Всего каналов - {num_channels}\n'
                                    f'Всего сообщений в базе - {all_mes}\n'
                                    f'Сообщений с интентом (без нецелевых и пустых) - {checked_intent}\n'
                                    f'Сообщений проверено админом - {checked_admin}',
                               reply_markup=menu_main)

        for xxx in stat_specs:
            await bot.send_message(message.from_user.id, text=f'{xxx}')
