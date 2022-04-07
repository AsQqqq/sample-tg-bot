from aiogram.types import KeyboardButton, ReplyKeyboardMarkup



start_keyboard_simple = ReplyKeyboardMarkup(resize_keyboard=True)\
    .add(
    KeyboardButton(
        'Начать'
    ))