import logging
from aiogram import Bot, Dispatcher, executor, types
from dotenv import load_dotenv
import os, sys

load_dotenv()
API_TOKEN = os.getenv("TOKEN")
# print(API_TOKEN)

# Configure logging:
logging.basicConfig(level=logging.INFO)

# Initialize the bot and dispatcher:
bot = Bot(token=API_TOKEN)  # create an object
dp = Dispatcher(bot=bot) # Help to make the connection with telegram bot


@dp.message_handler(commands=['start', 'help'])
async def command_start_handler(message: types.Message):
    """
    This handler receives messages with '/start' or '/help' command
    """
    await message.reply("Hi \n I am Echo Bot Created By Mr. Shayan! \n Powered by aiogram.")


@dp.message_handler()
async def echo(message: types.Message):
    """This will return echo
    """
    await message.answer(message.text)
    




if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)