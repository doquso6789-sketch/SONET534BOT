import os
import re
import asyncio

from telegram import Update
from telegram.ext import ContextTypes

from utils.downloader import download_video
from utils.database import save_user
from utils.security import is_allowed
from utils.logger import log

URL_REGEX = re.compile(r"https?://[^\s]+")


async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):

    user_id = update.effective_user.id

    save_user(user_id)

    if not is_allowed(user_id):
        await update.message.reply_text(
            "⏳ Please wait before next download"
        )
        return

    text = update.message.text

    urls = URL_REGEX.findall(text)

    if not urls:
        await update.message.reply_text("❌ Invalid URL")
        return

    url = urls[0]

    msg = await update.message.reply_text(
        "⏳ Downloading..."
    )

    try:

        loop = asyncio.get_event_loop()

        file_path = await loop.run_in_executor(
            None,
            download_video,
            url
        )

        if not file_path:
            await msg.edit_text(
                "❌ Download failed"
            )
            return

        ext = os.path.splitext(file_path)[1].lower()

        await msg.edit_text(
            "📤 Uploading..."
        )

        if ext in [".mp3", ".m4a"]:

            with open(file_path, "rb") as audio:

                await update.message.reply_audio(
                    audio=audio,
                    caption="✅ Download Complete"
                )

        else:

            with open(file_path, "rb") as video:

                await update.message.reply_video(
                    video=video,
                    caption="✅ Download Complete",
                    supports_streaming=True
                )

        os.remove(file_path)

        await msg.delete()

        log(f"Downloaded: {url}")

    except Exception as e:

        await msg.edit_text(
            f"❌ Error:\n{str(e)}"
        )
