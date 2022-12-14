import os
import asyncio
import datetime
from loader import bot
import aioschedule
from aiogram.utils.markdown import hlink
from dotenv import load_dotenv

load_dotenv()


game_data = datetime.date.today() + datetime.timedelta(days=1)
data_new = game_data.strftime('%d.%m')


address_link = hlink('адрес на карте', 'https://maps.app.goo.gl/Mya9x76EKrbX3R9g8')


async def send_poll_func(weekday):
    await bot.send_poll(chat_id=os.getenv('CHAT_ID_MAFIA'),
                        question='🎯 Играем в спортивную мафию\n'
                                 f'📅 {weekday} {data_new}\n'
                                 '💰 Стоимость участия: 100 лир (также есть абонементы на игры)',
                        options=['Буду к 18:00', 'Буду к 19:00', 'Буду к 20:00', 'Буду позже',
                                 'Пока не знаю, решу и переголосую', 'Не в этот раз', 'Посмотреть, кто придет'],
                        is_anonymous=False)
    await bot.send_message(chat_id=os.getenv('CHAT_ID_MAFIA'),
                           text='<a href="https://maps.app.goo.gl/Mya9x76EKrbX3R9g8">'
                                '📍Локация: MEZZA GURME (ссылка на карту)</a>', parse_mode="HTML")


async def scheduler():
    """ 0-monday, 1-tuesday, 2-wednesday, 3-thursday, 4-friday, 5-saturday, 6-sunday """
    aioschedule.every().monday.at('12:00').do(send_poll_func, 'Вторник')
    aioschedule.every().thursday.at('12:00').do(send_poll_func, 'Пятница')
    print('Функция sсhedule запущена')
    while True:
        await aioschedule.run_pending()
        await asyncio.sleep(1)


#  if datetime.date.today().weekday() == 3:
