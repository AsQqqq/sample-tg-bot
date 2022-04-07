import json, string
from aiogram import types
from import_bot import scheduler, ALLUSER
from handler.messageedit import message_delete
from datetime import timedelta, datetime

async def no_message(message:types.Message):
    await message.delete()
    if ALLUSER.total_ban(message.from_user.id):
        date_20s = datetime.now() + timedelta(seconds=20)
        if {i.lower().translate(str.maketrans('', '', string.punctuation)) for i in message.text.split(' ')} \
                .intersection(set(json.load(open('other/no_message.json')))) != set():

            for row0 in ALLUSER.exists_number_warning(0, message.from_user.id):
                mat = await message.answer('данные слова запрещены. Вырожайтесь правильно')
                scheduler.add_job(message_delete, "date", run_date=date_20s, kwargs={"message": mat})
            for row1 in ALLUSER.exists_number_warning(1, message.from_user.id):
                mat = await message.answer('Не стоит использовать такие слова...')
                scheduler.add_job(message_delete, "date", run_date=date_20s, kwargs={"message": mat})
            for row2 in ALLUSER.exists_number_warning(2, message.from_user.id):
                mat = await message.answer('Друг... я же могу забанить...')
                scheduler.add_job(message_delete, "date", run_date=date_20s, kwargs={"message": mat})
            for row3 in ALLUSER.exists_number_warning(3, message.from_user.id):
                mat = await message.answer('Еще одно такое слово и ты получишь бан!')
                scheduler.add_job(message_delete, "date", run_date=date_20s, kwargs={"message": mat})
            for row4 in ALLUSER.exists_number_warning(4, message.from_user.id):
                await ALLUSER.edit_warning(0, message.from_user.id)
                await ALLUSER.edit_ban(1, message.from_user.id)
                mat = await message.answer('Banned')
                scheduler.add_job(message_delete, "date", run_date=date_20s, kwargs={"message": mat})
            await ALLUSER.number_plus_warning(message.from_user.id)
        else:
            msg = await message.answer('Я не понимаю твои слова. Напиши /start или /help')
            scheduler.add_job(message_delete, "date", run_date=date_20s, kwargs={"message": msg})
    else:
        msg = await message.answer('Вы забанены')
        date_10s = datetime.now() + timedelta(seconds=10)
        scheduler.add_job(message_delete, "date", run_date=date_10s, kwargs={"message": msg})

def reg_handler(dp):
    dp.register_message_handler(no_message)