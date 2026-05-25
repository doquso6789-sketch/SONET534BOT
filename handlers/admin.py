from telegram import Update
from telegram.ext import ContextTypes

ADMIN_ID = 123456789


async def broadcast(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if update.effective_user.id != ADMIN_ID:
        return

    text = " ".join(context.args)

    with open("data/users.json", "r") as f:
        users = json.load(f)

    for uid in users:
        try:
            await context.bot.send_message(uid, text)
        except:
            pass
