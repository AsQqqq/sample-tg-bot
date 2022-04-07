from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup


start_keyboard_inline = InlineKeyboardMarkup()\
    .add(InlineKeyboardButton('Начать', callback_data='start_inline'))