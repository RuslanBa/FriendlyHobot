import os
from aiogram import Dispatcher, Bot
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from dotenv import load_dotenv


load_dotenv()


bot = Bot(token=os.getenv("TOKEN"))


storage = MemoryStorage()
dp = Dispatcher(bot, storage=storage)
