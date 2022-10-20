import asyncio
import datetime
from loader import bot
import aioschedule


game_data = datetime.date.today() + datetime.timedelta(days=1)
data_new = game_data.strftime('%d.%m')


async def send_poll_func(weekday):
    await bot.send_poll(chat_id='-816657774',
                        question='🎯 Играем в спортивную мафию\n'
                                 f'📅 {weekday} {data_new}\n'
                                 '💰 Стоимость участия: 100 лир (также есть абонементы на игры)',
                        options=['Буду к 18:00', 'Буду к 19:00', 'Буду к 20:00', 'Буду позже',
                                 'Пока не знаю, решу и переголосую', 'Не в этот раз', 'Посмотреть, кто придет'],
                        is_anonymous=False)


async def scheduler():
    """ 0-monday, 1-tuesday, 2-wednesday, 3-thursday, 4-friday, 5-saturday, 6-sunday """
    if datetime.date.today().weekday() == 0:
        aioschedule.every().monday.at('12:00').do(send_poll_func, 'Вторник')
        while True:
            await aioschedule.run_pending()
            await asyncio.sleep(1)

    elif datetime.date.today().weekday() == 1:
        aioschedule.every().tuesday.at('12:00').do(send_poll_func, 'Среда')
        while True:
            await aioschedule.run_pending()
            await asyncio.sleep(1)

    elif datetime.date.today().weekday() == 2:
        aioschedule.every().wednesday.at('12:00').do(send_poll_func, 'Четверг')
        while True:
            await aioschedule.run_pending()
            await asyncio.sleep(1)

    elif datetime.date.today().weekday() == 3:
        aioschedule.every().thursday.at('12:00').do(send_poll_func, 'Пятница')
        while True:
            await aioschedule.run_pending()
            await asyncio.sleep(1)

    elif datetime.date.today().weekday() == 4:
        aioschedule.every().friday.at('12:00').do(send_poll_func, 'Суббота')
        while True:
            await aioschedule.run_pending()
            await asyncio.sleep(1)

    elif datetime.date.today().weekday() == 5:
        aioschedule.every().saturday.at('12:00').do(send_poll_func, 'Воскресенье')
        while True:
            await aioschedule.run_pending()
            await asyncio.sleep(1)

    elif datetime.date.today().weekday() == 6:
        aioschedule.every().sunday.at('12:00').do(send_poll_func, 'Понедельник')
        while True:
            await aioschedule.run_pending()
            await asyncio.sleep(1)
