from aiogram.utils import executor

from handler import main, other
from import_bot import dp
from database import base

#MAIN
main.reg_handler(dp)
#OTHER
other.reg_handler(dp)

async def on_startup(_):
    try:
        base.all_user()
        print('all user -- ok')
    except:
        print('table not')

if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True, on_startup=on_startup)