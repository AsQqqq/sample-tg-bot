import config
from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from database.base import all_user_class
from apscheduler.schedulers.asyncio import AsyncIOScheduler


ALLUSER = all_user_class('database.db')

storage = MemoryStorage()
ID = config.ADMINS

scheduler = AsyncIOScheduler()
scheduler.start()



bot = Bot(token=config.TOKEN, parse_mode=types.ParseMode.HTML)
dp = Dispatcher(bot, storage=storage)