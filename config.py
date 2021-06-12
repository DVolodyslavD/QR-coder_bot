"""
    Created Volodyslav D. 06-11-2021
    Version: 2.8-a
    Last update: 06-12-2021
"""

import os
import time

import qrcode
from aiogram import Bot
from aiogram.dispatcher import Dispatcher

# QR-code template
QR = qrcode.QRCode(
    version=5,
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

bot = Bot(token=TOKEN)
dp = Dispatcher(bot)
