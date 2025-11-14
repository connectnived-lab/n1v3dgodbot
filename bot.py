import os
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, filters, ContextTypes

# --- CONFIGURATION ---

BOT_TOKEN = os.getenv("BOT_TOKEN")

# Add your friends' Telegram user IDs here (we will fill this later)
ALLOWED_USERS = []

# Define keywords and their answers (we will update this later)
KEYWORDS = {
    "zwdbm": "This is the reply for zwdbm!",
}

# --- HANDLERS ---

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if update.effective_user.id not in ALLOWED_USERS:
        await update.message.reply_text("🚫 You are not authorized to use this bot.")
        return
    await update.message.reply_text("✅ Bot is active! Send a keyword.")

async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_id = update.effective_user.id
    text = update.message.text.lower()

    if user_id not in ALLOWED_USERS:
        await update.message.reply_text("🚫 You are not authorized to use this bot.")
        return

    if text in KEYWORDS:
        await update.message.reply_text(KEYWORDS[text])
    else:
        await update.message.reply_text("❓ Unknown keyword.")

# --- MAIN FUNCTION ---

async def main():
    app = ApplicationBuilder().token(BOT_TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))

    print("🤖 Bot started...")
    await app.run_polling()

if __name__ == "__main__":
    import asyncio
    asyncio.run(main())
