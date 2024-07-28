from pyrogram import Client, filters
from pyrogram.types import Message
from download_socials_bot.check import check_service
from download_socials_bot.errors import UnknownService

async def register_handlers(bot: Client):

    @bot.on_message(filters.command("start"))
    async def command_start(client: Client, message: Message):
        await message.reply("Привет, я - бот, который поможет тебе скачать видео из популярных сервисов, таких как Youtube, TikTok, Reels и т.д. Отправь ниже ссылку на видео")


    @bot.on_message(filters.command("help"))
    async def command_help(client: Client, message: Message):
        await message.reply("Просто скинь сюда ссылку на видео, будь то Youtube, Tiktok, Reels и я отправлю это видео тебе без водяных знаков. Я всё ещё в разработке, поэтому, если заметили баг, настоятельно рекомендую сообщить о нём @vizer0n\nP.S: Пока что бот ничего не умеет")


    @bot.on_message(filters.regex("http"))
    async def download_from_url(client: Client, message: Message):
        try:
            await check_service(message.text)
        except UnknownService as e:
            await message.reply(e)