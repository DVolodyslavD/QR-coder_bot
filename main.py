import logging

from aiogram.utils import executor

from config import dp
import bot

if __name__ == '__main__':
    logging.basicConfig(
        level=logging.INFO,
        format="[%(asctime)s](%(levelname)s): \"%(filename)s\", line:%(lineno)d %(funcName)s - %(message)s",
        filename='botLogs.log')

    executor.start_polling(dp)
