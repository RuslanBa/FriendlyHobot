import asyncio
import socketserver
import http.server
from aiogram.utils import executor
from aiogram import types
from loader import bot, dp
from schedular import scheduler_monday, scheduler_thursday

from http import HTTPStatus


class Handler(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        self.send_response(HTTPStatus.OK)
        self.end_headers()
        msg = 'Hello! you requested %s' % self.path
        self.wfile.write(msg.encode())


@dp.message_handler()
async def answer(message: types.Message):
    await message.answer(text='Привет')


async def on_startup(_):
    asyncio.create_task(scheduler_monday())
    asyncio.create_task(scheduler_thursday())


if __name__ == '__main__':
    print('начинаем работу')
    port = ('0.0.0.0', 80)
    httpd = socketserver.TCPServer(('', port), Handler)
    httpd.serve_forever()
    executor.start_polling(dp, on_startup=on_startup)
