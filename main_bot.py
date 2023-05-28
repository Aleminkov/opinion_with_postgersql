from aiogram import types, executor
from help_for_bot import dp
from handler import user 
from sql import postger_sql


async def start(_):

    await postger_sql.sql_start()
    print('Бот вышел на связь')

user.handlers_client(dp)

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True , on_startup=start)