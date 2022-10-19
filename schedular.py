import asyncio
import datetime
from loader import bot
import aioschedule


game_data = datetime.date.today() + datetime.timedelta(days=1)
data_new = game_data.strftime('%d.%m')


async def send_poll_monday():
    await bot.send_poll(chat_id='-816657774',
                        question='🎯 Играем в спортивную мафию\n'
                                 f'📅 Вторник {data_new}\n'
                                 '💰 Стоимость участия: 100 лир (также есть абонементы на игры)',
                        options=['Буду к 18:00', 'Буду к 19:00', 'Буду к 20:00', 'Буду позже',
                                 'Пока не знаю, решу и переголосую', 'Не в этот раз', 'Посмотреть, кто придет'],
                        is_anonymous=False)


async def send_poll_thursday():
    await bot.send_poll(chat_id='-816657774',
                        question='🎯 Играем в спортивную мафию\n'
                                 f'📅 Пятница {data_new}\n'
                                 '💰 Стоимость участия: 100 лир (также есть абонементы на игры)',
                        options=['Буду к 18:00', 'Буду к 19:00', 'Буду к 20:00', 'Буду позже',
                                 'Пока не знаю, решу и переголосую', 'Не в этот раз', 'Посмотреть, кто придет'],
                        is_anonymous=False)


async def scheduler_monday():
    aioschedule.every().monday.at('12:00').do(send_poll_monday)
    while True:
        await aioschedule.run_pending()
        await asyncio.sleep(1)


async def scheduler_wednesday():
    aioschedule.every().wednesday.at('19:37').do(send_poll_thursday)
    while True:
        await aioschedule.run_pending()
        await asyncio.sleep(1)
