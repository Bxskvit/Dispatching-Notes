from aiogram import Bot, Dispatcher
from config import TELEGRAM_TOKEN


bot = Bot(TELEGRAM_TOKEN)
dp: Dispatcher = Dispatcher()
