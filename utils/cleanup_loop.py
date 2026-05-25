import asyncio
from utils.cleaner import clean_old_files


async def cleanup_task():
    while True:
        clean_old_files(hours=1)
        await asyncio.sleep(3600)
