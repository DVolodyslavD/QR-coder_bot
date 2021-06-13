from aiogram.types import KeyboardButton, ReplyKeyboardMarkup

help_mssg = "Hey! Just send me a text, and I will send you the corresponding QR-code! I'll wait ;)"
info_mssg = """
Creator: dvd.workacc20@gmail.com\n\n
Thanks for using the bot
"""
error_mssg = "I don't know how to work with this yet..."

button_help = KeyboardButton('/help')
button_info = KeyboardButton('/info')

kb_start = ReplyKeyboardMarkup(
    resize_keyboard=True, one_time_keyboard=True
).add(button_help, button_info)
