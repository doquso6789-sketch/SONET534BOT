import asyncio

from telegram.ext import (
    Application,
    CommandHandler,
    MessageHandler,
    filters,
)

from config import BOT_TOKEN

from handlers.start import start
from handlers.download import handle_message
from utils.cleanup_loop import cleanup_task


async def on_startup(app):
    asyncio.create_task(cleanup_task())
    print("CLEANUP LOOP STARTED")


app = (
    Application.builder()
    .token(BOT_TOKEN)
    .concurrent_updates(True)
    .build()
)

app.add_handler(CommandHandler("start", start))

app.add_handler(
    MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message)
)

app.post_init = on_startup

print("BOT RUNNING...")

app.run_polling(drop_pending_updates=True)
