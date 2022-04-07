from aiogram import types
from handler.messageedit import message_delete
from import_bot import ID, ALLUSER, dp, scheduler, bot
from datetime import timedelta, datetime
from keyboard import start_keyboard_inline, start_keyboard_simple


async def start_command(message: types.Message):
    await message.delete()
    if not ALLUSER.user_exists(message.from_user.id):
        await ALLUSER.add_user(message.from_user.id)
    else:
        await ALLUSER.edit_status(1, message.from_user.id)
    if ALLUSER.total_ban(message.from_user.id):
        date_20s = datetime.now() + timedelta(seconds=20)
        if ALLUSER.total_status(message.from_user.id):
            await ALLUSER.edit_status(True, message.from_user.id)
        if message.from_user.id == ID:
            msg = await message.answer('HELLO ADMIN', reply_markup=start_keyboard_inline)
        else:
            msg = await message.answer('HELLO USER', reply_markup=start_keyboard_inline)
        scheduler.add_job(message_delete, "date", run_date=date_20s, kwargs={"message": msg})
    else:
        msg = await message.answer('Вы забанены')
        date_10s = datetime.now() + timedelta(seconds=10)
        scheduler.add_job(message_delete, "date", run_date=date_10s, kwargs={"message": msg})

@dp.callback_query_handler(text='start_inline')
async def start_inline(call: types.CallbackQuery):
    date_30s = datetime.now() + timedelta(seconds=20)
    await bot.delete_message(chat_id=call.message.chat.id, message_id=call.message.message_id)
    msg = await call.message.answer('Вызвана новая клавиатура',
                        reply_markup=start_keyboard_simple)
    scheduler.add_job(message_delete, "date", run_date=date_30s, kwargs={"message": msg})

def reg_handler(dp):
    dp.register_message_handler(start_command, commands='start')