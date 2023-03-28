import asyncio
import io
from telebot.async_telebot import AsyncTeleBot
import token

tbtoken = token.TOKEN
tb = AsyncTeleBot(tbtoken)


@tb.message_handler(commands=["start"])
async def start(message):
    await tb.send_message(message.chat.id, "zdarova!")


asyncio.run(tb.infinity_polling(timeout=None))
