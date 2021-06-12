"""
    Created Volodyslav D. 06-11-2021
    Version: 2.4-a
    Last update: 06-11-2021
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
DB_FILE = 'db_users.db'

# Telegram bot
TOKEN = '1881100312:AAES_c6tOBAm_69Qw4W3_2e71yEcRyo07Ys'

bot = Bot(token=TOKEN)
dp = Dispatcher(bot)
