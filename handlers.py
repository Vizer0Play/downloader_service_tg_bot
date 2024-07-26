from pyrogram import Client, filters
from pyrogram.types import Message
from pyrogram.enums import ParseMode

async def register_handlers(bot: Client):
    @bot.on_message(filters.command("start"))
    async def command_start(client: Client, message: Message):
        await message.reply("Привет, я - бот, который поможет тебе скачать видео из популярных сервисов, таких как Youtube, TikTok, Reels и т.д. Я всё ещё в разработке, поэтому, если заметили баг, настоятельно рекомендую сообщить о нём @vizer0n", parse_mode=ParseMode.MARKDOWN)
