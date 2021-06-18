"""
    Created Volodyslav D. 06-11-2021
    Version: 3.2-b
    Last update: 17-13-2021
"""

import os
import time

import qrcode
from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher

# QR-code template
QR = qrcode.QRCode(
    version=None,
    error_correction=qrcode.constants.ERROR_CORRECT_H,
    box_size=10,
    border=4,
)

# Path to save QR-codes
TARGET_DIR = 'qrcodes' + os.sep + time.strftime('%Y%m%d%H%M%S') + '.png'

# database filename
DB_FILE = '...'

# Telegram bot
TOKEN = '...'

bot = Bot(token=TOKEN, parse_mode=types.ParseMode.HTML)
dp = Dispatcher(bot)
