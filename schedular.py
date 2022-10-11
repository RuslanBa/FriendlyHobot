import asyncio
from loader import bot
import aioschedule


async def send_poll1():
    await bot.send_poll(chat_id='-816657774',
                        question='Вы пойдете сегодня играть?',
                        options=['a)', 'b)', 'c)'],
                        is_anonymous=False)


async def scheduler():
    aioschedule.every().day.at('20:00').do(send_poll1)
    while True:
        await aioschedule.run_pending()
        await asyncio.sleep(1)
