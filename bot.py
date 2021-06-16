import os

from aiogram import types
import aiogram.utils.markdown as aimd
import logging

from config import dp, bot, QR, TARGET_DIR, DB_FILE
from answers import kb_start, help_mssg, info_mssg, error_mssg
from sq_statement import select_users, write_user


@dp.message_handler(commands=['start'])
async def start_command(message: types.Message):
    user_id = message.from_user.id
    result = select_users(DB_FILE)
    # Checking for the presence of the user in the database.
    for i in result:
        if user_id == i[0]:
            break
    else:
        # If the user is not in the database, write he to the database.
        first_name = message.from_user.first_name
        username = message.from_user.username
        logging.info(f"New user: {first_name}")
        write_user(DB_FILE, user_id, first_name, username)
    await message.reply(
        f"Hello, <b>{aimd.quote_html(message.from_user.first_name)}</b>! I can generate <u>QR-code</u>.\n"
        f"Just send me a text (for example, a link) and I will send you the corresponding QR-code.\n"
        f"Enter /info to see more information about me.",
        reply_markup=kb_start)


@dp.message_handler(commands=['help'])
async def help_command(message: types.Message):
    await message.reply(help_mssg)


@dp.message_handler(commands=['info'])
async def info_command(message: types.Message):
    await message.answer(info_mssg)


@dp.message_handler(content_types=types.ContentType.TEXT)
async def qr_text_creator(message: types.Message):
    data = message.text
    logging.info(data)
    QR.add_data(data)
    QR.make(fit=True)
    img = QR.make_image(fill_color="black", back_color="white").convert('RGB')
    img.save(TARGET_DIR)
    with open(TARGET_DIR, 'rb') as qrcode:
        await bot.send_photo(message.from_user.id, qrcode)
    QR.clear()
    try:
        os.remove(TARGET_DIR)
    except FileNotFoundError:
        pass


@dp.message_handler(content_types=types.ContentType.PHOTO)
async def help_command(message: types.Message):
    await message.reply(error_mssg)
