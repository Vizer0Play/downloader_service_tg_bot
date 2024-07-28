from download_socials_bot.downloader import download_from_tiktok
from download_socials_bot.errors import UnknownService

async def check_service(url: str):
    if "tiktok.com" in url:
        await download_from_tiktok(url)
    else:
        raise UnknownService