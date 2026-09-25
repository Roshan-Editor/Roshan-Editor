import logging
from telegram import Update, ReplyKeyboardMarkup
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, filters, ContextTypes
from telegram.request import HTTPXRequest

# Logging Setup
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)

# 🔑 Apka Bot Token
BOT_TOKEN = "8577045271:AAHz_LC9XiZ41E3Yt5YdFwlttOiLm0ltpV0"

# 🌐 Social Links Setup
TELEGRAM_LINK_1 = "https://t.me/RoshanGaming_bot"
TELEGRAM_LINK_2 = "https://t.me/roshangaming0"
WHATSAPP_LINK = "https://wa.me/910000000000"
YOUTUBE_LINK = "https://youtube.com/@roshangaming"
FACEBOOK_LINK = "https://facebook.com/roshangaming"
INSTA_LINK = "https://instagram.com/roshangaming"

# 👑 3D ANSI Banner
ROSHAN_BIG_TEXT = (
    "<pre>"
    "██████╗  ██████╗ ███████╗██╗  ██╗  █████╗ ██╗  ██╗\n"
    "██╔══██╗██╔═══██╗██╔════╝██║  ██║██╔══██╗████╗ ██║\n"
    "██████╔╝██║   ██║███████╗███████║███████║██╔██╗██║\n"
    "██╔══██╗██║   ██║╚════██║██╔══██║██╔══██║██║╚████║\n"
    "██║  ██║╚██████╔╝███████║██║  ██║██║  ██║██║ ╚███║\n"
    "╚═╝  ╚═╝ ╚═════╝ ╚══════╝╚═╝  ╚═╝╚═╝  ╚═╝╚═╝  ╚══╝"
    "</pre>"
)

# 🔑 Updated Passwords Dictionary (V1 to V24)
PROJECT_PASSWORDS = {
    "VIP INJECTOR PASS V1": "8865",
    "VIP INJECTOR PASS V2": "98789",
    "VIP INJECTOR PASS V3": "84839393",
    "VIP INJECTOR PASS V4": "8923",
    "VIP INJECTOR PASS V5": "82190",
    "VIP INJECTOR PASS V6": "11029",
    "VIP INJECTOR PASS V7": "38383421",
    "VIP INJECTOR PASS V8": "7310",
    "VIP INJECTOR PASS V9": "292910",
    "VIP INJECTOR PASS V10": "3829",
    "VIP INJECTOR PASS V11": "39292",
    "VIP INJECTOR PASS V12": "3201",
    "VIP INJECTOR PASS V13": "39292",
    "VIP INJECTOR PASS V14": "Roshan",
    "VIP INJECTOR PASS V15": "292p",
    "VIP INJECTOR PASS V16": "2939ei",
    "VIP INJECTOR PASS V17": "wiw922",
    "VIP INJECTOR PASS V18": "192iw9",
    "VIP INJECTOR PASS V19": "292js92iq19",
    "VIP INJECTOR PASS V20": "w92929",
    "VIP INJECTOR PASS V21": "w02929",
    "VIP INJECTOR PASS V22": "wi93",
    "VIP INJECTOR PASS V23": "w0300s",
    "VIP INJECTOR PASS V24": "wowo",
}

# 🌟 Main Header Text
HEADER_TEXT = (
    f"{ROSHAN_BIG_TEXT}\n"
    "<b><i>👑 CREATED BY ROSHAN GUPTA 👑</i></b>\n"
    "<b><i>⚙️ VERSION 46.56.90.89 ⚙️</i></b>\n\n"
    "<b>🌐 <i>OUR OFFICIAL SOCIAL LINKS:</i></b>\n"
    f"<b>▶️ <i>YOUTUBE:</i></b> <a href='{YOUTUBE_LINK}'><b><i>CLICK HERE</i></b></a>\n"
    f"<b>📢 <i>TELEGRAM 1:</i></b> <a href='{TELEGRAM_LINK_1}'><b><i>CLICK HERE</i></b></a>\n"
    f"<b>📢 <i>TELEGRAM 2:</i></b> <a href='{TELEGRAM_LINK_2}'><b><i>CLICK HERE</i></b></a>\n"
    f"<b>💬 <i>WHATSAPP:</i></b> <a href='{WHATSAPP_LINK}'><b><i>CLICK HERE</i></b></a>\n"
    f"<b>📸 <i>INSTAGRAM:</i></b> <a href='{INSTA_LINK}'><b><i>CLICK HERE</i></b></a>\n"
    f"<b>📘 <i>FACEBOOK:</i></b> <a href='{FACEBOOK_LINK}'><b><i>CLICK HERE</i></b></a>\n\n"
    "<b>━━━━━━━━━━━━━━━━━━━━━━━━━━━</b>\n"
    "<b>👇 <i>SELECT A VIP INJECTOR PASS</i> 👇</b>"
)

# /start Command Handler
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_name = update.effective_user.first_name

    keyboard = [
        ["VIP INJECTOR PASS V1", "VIP INJECTOR PASS V2"],
        ["VIP INJECTOR PASS V3", "VIP INJECTOR PASS V4"],
        ["VIP INJECTOR PASS V5", "VIP INJECTOR PASS V6"],
        ["VIP INJECTOR PASS V7", "VIP INJECTOR PASS V8"],
        ["VIP INJECTOR PASS V9", "VIP INJECTOR PASS V10"],
        ["VIP INJECTOR PASS V11", "VIP INJECTOR PASS V12"],
        ["VIP INJECTOR PASS V13", "VIP INJECTOR PASS V14"],
        ["VIP INJECTOR PASS V15", "VIP INJECTOR PASS V16"],
        ["VIP INJECTOR PASS V17", "VIP INJECTOR PASS V18"],
        ["VIP INJECTOR PASS V19", "VIP INJECTOR PASS V20"],
        ["VIP INJECTOR PASS V21", "VIP INJECTOR PASS V22"],
        ["VIP INJECTOR PASS V23", "VIP INJECTOR PASS V24"]
    ]
    reply_markup = ReplyKeyboardMarkup(keyboard, resize_keyboard=True)

    welcome_message = f"<b>👋 <i>HELLO, {user_name.upper()}!</i></b>\n\n" + HEADER_TEXT

    await update.message.reply_text(
        text=welcome_message,
        reply_markup=reply_markup,
        parse_mode="HTML",
        disable_web_page_preview=True
    )

# Injector Button Handler
async def handle_buttons(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = update.message.text.strip()

    if text in PROJECT_PASSWORDS:
        password = PROJECT_PASSWORDS[text]

        response_text = (
            f"{ROSHAN_BIG_TEXT}\n"
            "<b><i>👑 CREATED BY ROSHAN GUPTA 👑</i></b>\n"
            "<b><i>⚙️ VERSION 46.56.90.89 ⚙️</i></b>\n\n"
            "<b>━━━━━━━━━━━━━━━━━━━━━━━━━━━</b>\n\n"
            "🌸🌺🌹🌻✨💖⭐🔥💖✨🌻🌹🌺🌸\n"
            f"<b>🔥 <u>{text}</u> 🔥</b>\n"
            "🌸🌺🌹🌻✨💖⭐🔥💖✨🌻🌹🌺🌸\n\n"
            "🌸✨🌹💖⭐🌻🌺✨💖⭐🌹🌻🌸\n"
            "<b>🔑 <i>VIP INJECTOR PASSWORD</i> 🔑</b>\n"
            "🌸✨🌹💖⭐🌻🌺✨💖⭐🌹🌻🌸\n\n"
            "╔═════════════════════════════════╗\n"
            f"  🌸 🌺 <b><code>{password}</code></b> 🌹 🌻\n"
            "╚═════════════════════════════════╝\n\n"
            "<b>━━━━━━━━━━━━━━━━━━━━━━━━━━━</b>\n"
            "<b>[ <i>DIRECT LINK PAY 30 RUPEES</i> ]</b>\n\n"
            "<b><i>DM</i> = @RoshanGaming ❗</b>"
        )

        await update.message.reply_text(
            text=response_text,
            parse_mode="HTML",
            disable_web_page_preview=True
        )
    else:
        await update.message.reply_text(
            "<b>⚠️ <i>Kripya niche दिए गए menu se sahi option select karein!</i></b>",
            parse_mode="HTML"
        )

if __name__ == '__main__':
    request = HTTPXRequest(connect_timeout=20.0, read_timeout=20.0)
    app = ApplicationBuilder().token(BOT_TOKEN).request(request).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_buttons))

    print("🔥 Roshan Gupta Bot V5.0 Fully Updated & Online! 🔥")
    app.run_polling()
