from dotenv import load_dotenv
import os, sys
import openai
from aiogram import Bot, executor, Dispatcher, types


class Reference:
    """A class to store previously response from the chatGPT API:
    """

    def __init__(self) -> None:
        self.response = ""


load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY") # ChatGPT OpenAI KEY

reference = Reference()

TOKEN = os.getenv("TOKEN") # Storing telegram bot token.


# model name
MODEL_NAME = "gpt-3.5-turbo"

# Initialize bot and Dispatcher:
bot = Bot(token=TOKEN)
dp = Dispatcher(bot=bot)


# Forget the past/previous search history:
def clear_past():
    """A Function to clear the previous conversations and context."""
    reference.response= ""


@dp.message_handler(commands=['start'])
async def welcome(message: types.Message):
    """
    This handler recieves messages with '/start' command.
    """
    await message.reply("Hi\n I am telebot created by Mr. Shayan.\n How can I assist you?")


@dp.message_handler(commands=['clear'])
async def clear(message: types.Message):
    """A handler to clear the previous conversation and context.
    """
    clear_past()
    await message.reply("I've cleared the past conversation and context.")

@dp.message_handler(commands=['help'])
async def helper(message: types.Message):
    """A helper to display the help menu.
    """
    help_command = """
    Hi there, I'm chatGPT based Telegram Bot created by Mr. Shayan! Please follow these commands - 
    /start - to start the conversation
    /clear - to clear the past conversation and context
    /help - to get this help menu.
    I hope this helps. :)
    """
    await message.reply(help_command)


@dp.message_handler()
async def chatgpt(message: types.Message):
    """
    A handler to process the user's input and generate a response using the chatGPT API.
    """
    print(f"USER: \n\t{message.text}")
    response = openai.Completion.create(
        model=MODEL_NAME,
        messages=[
            {"role": "assistant", "content": reference.response},  # role assistant
            {"role": "user", "content": message.text}  # out query
        ]
    )
    reference.response = response['choices'][0]['message']['content']
    print(f"chatGPT: \n\t{reference.response}")
    await bot.send_message(chat_id=message.chat.id, text=reference.response)



if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)
