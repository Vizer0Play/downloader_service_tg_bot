from pyrogram import Client, idle
from handlers import register_handlers
from dotenv import load_dotenv
import asyncio
import nest_asyncio
import os

nest_asyncio.apply()
load_dotenv()

API_ID = os.getenv("API_ID")
API_HASH = os.getenv("API_HASH")
BOT_TOKEN = os.getenv("BOT_TOKEN")

client = Client(name="client", api_id=API_ID, api_hash=API_HASH)
bot = Client(name="bot", bot_token=BOT_TOKEN, api_id=API_ID, api_hash=API_HASH)

async def main():
    await client.start()
    await bot.start()
    await register_handlers(bot)
    await idle()
    await client.stop()
    await bot.stop()


if __name__ == "__main__":
    asyncio.run(main())