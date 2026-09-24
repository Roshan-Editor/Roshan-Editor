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
BOT_TOKEN = "8867333421:AAEzbeZAHLjnqO5iEDNi8v6Il43_oh_4K8Y"

# 🌐 Social Links Setup
TELEGRAM_LINK_1 = "https://t.me/RoshanGaming_bot"
TELEGRAM_LINK_2 = "https://t.me/roshangaming0"
WHATSAPP_LINK = "https://wa.me/910000000000"
YOUTUBE_LINK = "https://youtube.com/@roshangaming"
FACEBOOK_LINK = "https://facebook.com/roshangaming"
INSTA_LINK = "https://instagram.com/roshangaming"

# Projects List
PROJECT_LIST = [
    "🔥 VIP INJECTOR PROJECT V34",
    "⚡ VIP INJECTOR PROJECT V33",
    "💎 VIP INJECTOR PROJECT V32",
    "🚀 VIP INJECTOR PROJECT V31",
    "🎯 VIP INJECTOR PROJECT V30",
    "🌟 VIP INJECTOR PROJECT V29"
]

# 👑 100% Straight & Unbroken 3D ANSI Shadow ROSHAN Banner (Fixed Inside <pre>)
ROSHAN_BIG_TEXT = (
    "<pre>"
    "██████╗  ██████╗ ███████╗██╗  ██╗  █████╗ ██╗    ██╗\n"
    "██╔══██╗██╔═══██╗██╔════╝██║  ██║██╔══██╗████╗ ██║\n"
    "██████╔╝██║   ██║███████╗███████║███████║██╔██╗██║\n"
    "██╔══██╗██║   ██║╚════██║██╔══██║██╔══██║██║╚████║\n"
    "██║  ██║╚██████╔╝███████║██║  ██║██║  ██║██║ ╚███║\n"
    "╚═╝  ╚═╝ ╚═════╝ ╚══════╝╚═╝  ╚═╝╚═╝  ╚═╝╚═╝  ╚══╝"
    "</pre>"
)

# 📥 Download Links Dictionary
PROJECT_DATA = {
    "🔥 VIP INJECTOR PROJECT V34": {
        "vip_link1": "https://example.link/v34_1",
        "vip_link2": "https://example.link/v34_2",
        "macro_link1": "https://example.link/macro_v34_1",
        "macro_link2": "https://example.link/macro_v34_2",
        "holo_link1": "https://example.link/holo_v34_1",
        "holo_link2": "https://example.link/holo_v34_2",
        "sketch_link1": "https://example.link/sketch_v34_1",
        "sketch_link2": "https://example.link/sketch_v34_2",
        "mt_link1": "https://example.link/mt_v34_1",
        "mt_link2": "https://example.link/mt_v34_2",
    },
    "⚡ VIP INJECTOR PROJECT V33": {
        "vip_link1": "https://example.link/v33_1",
        "vip_link2": "https://example.link/v33_2",
        "macro_link1": "https://example.link/macro_v33_1",
        "macro_link2": "https://example.link/macro_v33_2",
        "holo_link1": "https://example.link/holo_v33_1",
        "holo_link2": "https://example.link/holo_v33_2",
        "sketch_link1": "https://example.link/sketch_v33_1",
        "sketch_link2": "https://example.link/sketch_v33_2",
        "mt_link1": "https://example.link/mt_v33_1",
        "mt_link2": "https://example.link/mt_v33_2",
    },
    "💎 VIP INJECTOR PROJECT V32": {
        "vip_link1": "https://example.link/v32_1",
        "vip_link2": "https://example.link/v32_2",
        "macro_link1": "https://example.link/macro_v32_1",
        "macro_link2": "https://example.link/macro_v32_2",
        "holo_link1": "https://example.link/holo_v32_1",
        "holo_link2": "https://example.link/holo_v32_2",
        "sketch_link1": "https://example.link/sketch_v32_1",
        "sketch_link2": "https://example.link/sketch_v32_2",
        "mt_link1": "https://example.link/mt_v32_1",
        "mt_link2": "https://example.link/mt_v32_2",
    },
    "🚀 VIP INJECTOR PROJECT V31": {
        "vip_link1": "https://example.link/v31_1",
        "vip_link2": "https://example.link/v31_2",
        "macro_link1": "https://example.link/macro_v31_1",
        "macro_link2": "https://example.link/macro_v31_2",
        "holo_link1": "https://example.link/holo_v31_1",
        "holo_link2": "https://example.link/holo_v31_2",
        "sketch_link1": "https://example.link/sketch_v31_1",
        "sketch_link2": "https://example.link/sketch_v31_2",
        "mt_link1": "https://example.link/mt_v31_1",
        "mt_link2": "https://example.link/mt_v31_2",
    },
    "🎯 VIP INJECTOR PROJECT V30": {
        "vip_link1": "https://example.link/v30_1",
        "vip_link2": "https://example.link/v30_2",
        "macro_link1": "https://example.link/macro_v30_1",
        "macro_link2": "https://example.link/macro_v30_2",
        "holo_link1": "https://example.link/holo_v30_1",
        "holo_link2": "https://example.link/holo_v30_2",
        "sketch_link1": "https://example.link/sketch_v30_1",
        "sketch_link2": "https://example.link/sketch_v30_2",
        "mt_link1": "https://example.link/mt_v30_1",
        "mt_link2": "https://example.link/mt_v30_2",
    },
    "🌟 VIP INJECTOR PROJECT V29": {
        "vip_link1": "https://example.link/v29_1",
        "vip_link2": "https://example.link/v29_2",
        "macro_link1": "https://example.link/macro_v29_1",
        "macro_link2": "https://example.link/macro_v29_2",
        "holo_link1": "https://example.link/holo_v29_1",
        "holo_link2": "https://example.link/holo_v29_2",
        "sketch_link1": "https://example.link/sketch_v29_1",
        "sketch_link2": "https://example.link/sketch_v29_2",
        "mt_link1": "https://example.link/mt_v29_1",
        "mt_link2": "https://example.link/mt_v29_2",
    }
}

# 🌟 Main Header Text
HEADER_TEXT = (
    f"{ROSHAN_BIG_TEXT}\n"
    "<b><i>👑 CREATED BY ROSHAN GUPTA 👑</i></b>\n"
    "<b><i>⚙️ VERSION 3.9.0 ⚙️</i></b>\n\n"
    "<b>🌐 <i>OUR OFFICIAL SOCIAL LINKS:</i></b>\n"
    f"<b>▶️ <i>YOUTUBE:</i></b> <a href='{YOUTUBE_LINK}'><b><i>CLICK HERE</i></b></a>\n"
    f"<b>📢 <i>TELEGRAM 1:</i></b> <a href='{TELEGRAM_LINK_1}'><b><i>CLICK HERE</i></b></a>\n"
    f"<b>📢 <i>TELEGRAM 2:</i></b> <a href='{TELEGRAM_LINK_2}'><b><i>CLICK HERE</i></b></a>\n"
    f"<b>💬 <i>WHATSAPP:</i></b> <a href='{WHATSAPP_LINK}'><b><i>CLICK HERE</i></b></a>\n"
    f"<b>📸 <i>INSTAGRAM:</i></b> <a href='{INSTA_LINK}'><b><i>CLICK HERE</i></b></a>\n"
    f"<b>📘 <i>FACEBOOK:</i></b> <a href='{FACEBOOK_LINK}'><b><i>CLICK HERE</i></b></a>\n\n"
    "<b>━━━━━━━━━━━━━━━━━━━━━━━━━━━</b>\n"
    "<b>👇 <i>SELECT A PROJECT TO DOWNLOAD</i> 👇</b>"
)

# /start Command Handler
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_name = update.effective_user.first_name

    keyboard = [
        ["🔥 VIP INJECTOR PROJECT V34", "⚡ VIP INJECTOR PROJECT V33"],
        ["💎 VIP INJECTOR PROJECT V32", "🚀 VIP INJECTOR PROJECT V31"],
        ["🎯 VIP INJECTOR PROJECT V30", "🌟 VIP INJECTOR PROJECT V29"]
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
    text = update.message.text
    
    if text in PROJECT_DATA:
        links = PROJECT_DATA[text]
        
        response_text = (
            f"{ROSHAN_BIG_TEXT}\n"
            "<b><i>👑 CREATED BY ROSHAN GUPTA 👑</i></b>\n"
            "<b><i>⚙️ VERSION 3.9.0 ⚙️</i></b>\n\n"
            "<b>━━━━━━━━━━━━━━━━━━━━━━━━━━━</b>\n\n"
            f"<b><i>{text} :</i></b>\n"
            f"╔═══════════════════════════╗\n"
            f"  <b><i>{links['vip_link1']}</i></b>\n"
            f"  <b><i>{links['vip_link2']}</i></b>\n"
            f"╚═══════════════════════════╝\n\n"
            "<b><i>MACRO BOX :</i></b>\n"
            f"╔═══════════════════════════╗\n"
            f"  <b><i>{links['macro_link1']}</i></b>\n"
            f"  <b><i>{links['macro_link2']}</i></b>\n"
            f"╚═══════════════════════════╝\n\n"
            "<b><i>HOLOGRAM ALL TYPES FILES :</i></b>\n"
            f"╔═══════════════════════════╗\n"
            f"  <b><i>{links['holo_link1']}</i></b>\n"
            f"  <b><i>{links['holo_link2']}</i></b>\n"
            f"╚═══════════════════════════╝\n\n"
            "<b><i>Sketchware Pro Apks :</i></b>\n"
            f"╔═══════════════════════════╗\n"
            f"  <b><i>{links['sketch_link1']}</i></b>\n"
            f"  <b><i>{links['sketch_link2']}</i></b>\n"
            f"╚═══════════════════════════╝\n\n"
            "<b><i>Mt Manager Apk :</i></b>\n"
            f"╔═══════════════════════════╗\n"
            f"  <b><i>{links['mt_link1']}</i></b>\n"
            f"  <b><i>{links['mt_link2']}</i></b>\n"
            f"╚═══════════════════════════╝\n\n"
            "<b>[ <i>DIRECT LINK PAY 30 RUPEES</i> ]</b>\n\n"
            "<b><i>DM</i> = @Xit_Macro ❗</b>"
        )
        
        await update.message.reply_text(
            text=response_text,
            parse_mode="HTML",
            disable_web_page_preview=True
        )
    else:
        await update.message.reply_text(
            "<b>⚠️ <i>Kripya niche diye gaye menu se sahi option select karein!</i></b>",
            parse_mode="HTML"
        )

if __name__ == '__main__':
    request = HTTPXRequest(connect_timeout=20.0, read_timeout=20.0)
    app = ApplicationBuilder().token(BOT_TOKEN).request(request).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_buttons))

    print("🔥 Roshan Gupta V3.9.0 Bot Fully Fixed & Online! 🔥")
    app.run_polling()
