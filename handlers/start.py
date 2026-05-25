from telegram import Update
from telegram.ext import ContextTypes


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):

    text = (
        "🔥 SOCIAL DOWNLOADER BOT\n\n"
        "✅ TikTok No Watermark\n"
        "✅ Facebook\n"
        "✅ Instagram\n"
        "✅ YouTube\n"
        "✅ SoundCloud\n\n"
        "📥 Send Link"
    )

    await update.message.reply_text(text)
