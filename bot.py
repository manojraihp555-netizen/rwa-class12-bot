import os
from telegram import Update
from telegram.ext import (
    Application,
    CommandHandler,
    MessageHandler,
    ContextTypes,
    filters,
)

TOKEN = os.getenv("BOT_TOKEN")

RULES = """
📚 RWA DOUBT GROUP RULES

🤝 Respect Everyone.
📖 Study Related Messages Only.
🚫 No Spam or Promotions.
📩 Don't DM Members Without Reason.
💬 Fun Chat: 8:30 PM - 10:00 PM.

👑 Owner : Nitin Kumar Gupta
🛡️ Admin : Vishesh
"""

SUPPORT = """
📞 Need Help?

अगर आपको किसी भी प्रकार की Study Related Problem हो तो Admin से संपर्क करें.

👑 Owner : Nitin Kumar Gupta
🛡️ Admin : Vishesh

📩 Telegram :
@Thakur_h4
"""

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "👋 Welcome!\n\n❤🌷 आपका RWA DOUBT GROUP में हार्दिक स्वागत है।"
    )

async def help_cmd(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "/rules - Group Rules\n"
        "/support - Contact Admin\n"
        "/help - Help Menu"
    )

async def rules(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(RULES)

async def support(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(SUPPORT)

async def welcome(update: Update, context: ContextTypes.DEFAULT_TYPE):
    for member in update.message.new_chat_members:
        await update.message.reply_text(
            f"👋 Welcome {member.first_name}! ❤🌷\n\n"
            "आपका RWA DOUBT GROUP में हार्दिक स्वागत है।\n\n"
            "📜 Rules देखने के लिए /rules लिखें।"
        async def goodbye(update: Update, context: ContextTypes.DEFAULT_TYPE):
    member = update.message.left_chat_member
    if member:
        await update.message.reply_text(
            f"😔 {member.first_name} ने Group छोड़ दिया।\n"
            "जहाँ भी रहें, खुश रहें। 🌸"
        )

def main():
    app = Application.builder().token(TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("help", help_cmd))
    app.add_handler(CommandHandler("rules", rules))
    app.add_handler(CommandHandler("support", support))

    app.add_handler(
        MessageHandler(filters.StatusUpdate.NEW_CHAT_MEMBERS, welcome)
    )
    app.add_handler(
        MessageHandler(filters.StatusUpdate.LEFT_CHAT_MEMBER, goodbye)
    )

    print("✅ Bot Started...")
    app.run_polling(allowed_updates=Update.ALL_TYPES)

if __name__ == "__main__":
    main()
