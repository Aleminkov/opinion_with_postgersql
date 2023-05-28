from TOKEN import TOKEN
from aiogram import Bot , Dispatcher
import logging


logging.basicConfig()

bot = Bot(TOKEN)
dp = Dispatcher(bot=bot)
