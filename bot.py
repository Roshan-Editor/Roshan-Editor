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

# Projects List (बिना एक्स्ट्रा स्पेस के)
PROJECT_LIST = [
    "VIP INJECTOR PROJECT V1",
    "VIP INJECTOR PROJECT V2",
    "VIP INJECTOR PROJECT V3",
    "VIP INJECTOR PROJECT V4",
    "VIP INJECTOR PROJECT V5",
    "VIP INJECTOR PROJECT V6",
    "VIP INJECTOR PROJECT V7",
    "VIP INJECTOR PROJECT V8",
    "VIP INJECTOR PROJECT V9",
    "VIP INJECTOR PROJECT V10",
    "VIP INJECTOR PROJECT V11",
    "VIP INJECTOR PROJECT V12",
    "VIP INJECTOR PROJECT V13",
    "VIP INJECTOR PROJECT V14",
    "VIP INJECTOR PROJECT V15",
    "VIP INJECTOR PROJECT V16",
    "VIP INJECTOR PROJECT V17",
    "VIP INJECTOR PROJECT V18",
    "VIP INJECTOR PROJECT V19",
    "VIP INJECTOR PROJECT V20",
    "VIP INJECTOR PROJECT V21",
    "VIP INJECTOR PROJECT V22",
    "VIP INJECTOR PROJECT V23",
    "VIP INJECTOR PROJECT V24",
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

# 📥 Download Links Dictionary (Keys बिना एक्स्ट्रा स्पेस के)
PROJECT_DATA = {
    "VIP INJECTOR PROJECT V1": {
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
    "VIP INJECTOR PROJECT V2": {
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
    "VIP INJECTOR PROJECT V3": {
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
    "VIP INJECTOR PROJECT V4": {
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
    "VIP INJECTOR PROJECT V5": {
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
    "VIP INJECTOR PROJECT V6": {
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
    },
    "VIP INJECTOR PROJECT V7": {
        "vip_link1": "https://example.link/v28_1",
        "vip_link2": "https://example.link/v28_2",
        "macro_link1": "https://example.link/macro_v28_1",
        "macro_link2": "https://example.link/macro_v28_2",
        "holo_link1": "https://example.link/holo_v28_1",
        "holo_link2": "https://example.link/holo_v28_2",
        "sketch_link1": "https://example.link/sketch_v28_1",
        "sketch_link2": "https://example.link/sketch_v28_2",
        "mt_link1": "https://example.link/mt_v28_1",
        "mt_link2": "https://example.link/mt_v28_2",
    },
    "VIP INJECTOR PROJECT V8": {
        "vip_link1": "https://example.link/v27_1",
        "vip_link2": "https://example.link/v27_2",
        "macro_link1": "https://example.link/macro_v27_1",
        "macro_link2": "https://example.link/macro_v27_2",
        "holo_link1": "https://example.link/holo_v27_1",
        "holo_link2": "https://example.link/holo_v27_2",
        "sketch_link1": "https://example.link/sketch_v27_1",
        "sketch_link2": "https://example.link/sketch_v27_2",
        "mt_link1": "https://example.link/mt_v27_1",
        "mt_link2": "https://example.link/mt_v27_2",
    },
    "VIP INJECTOR PROJECT V9": {
        "vip_link1": "https://example.link/v26_1",
        "vip_link2": "https://example.link/v26_2",
        "macro_link1": "https://example.link/macro_v26_1",
        "macro_link2": "https://example.link/macro_v26_2",
        "holo_link1": "https://example.link/holo_v26_1",
        "holo_link2": "https://example.link/holo_v26_2",
        "sketch_link1": "https://example.link/sketch_v26_1",
        "sketch_link2": "https://example.link/sketch_v26_2",
        "mt_link1": "https://example.link/mt_v26_1",
        "mt_link2": "https://example.link/mt_v26_2",
    },
    "VIP INJECTOR PROJECT V10": {
        "vip_link1": "https://example.link/v25_1",
        "vip_link2": "https://example.link/v25_2",
        "macro_link1": "https://example.link/macro_v25_1",
        "macro_link2": "https://example.link/macro_v25_2",
        "holo_link1": "https://example.link/holo_v25_1",
        "holo_link2": "https://example.link/holo_v25_2",
        "sketch_link1": "https://example.link/sketch_v25_1",
        "sketch_link2": "https://example.link/sketch_v25_2",
        "mt_link1": "https://example.link/mt_v25_1",
        "mt_link2": "https://example.link/mt_v25_2",
    },
    "VIP INJECTOR PROJECT V11": {
        "vip_link1": "https://example.link/v24_1",
        "vip_link2": "https://example.link/v24_2",
        "macro_link1": "https://example.link/macro_v24_1",
        "macro_link2": "https://example.link/macro_v24_2",
        "holo_link1": "https://example.link/holo_v24_1",
        "holo_link2": "https://example.link/holo_v24_2",
        "sketch_link1": "https://example.link/sketch_v24_1",
        "sketch_link2": "https://example.link/sketch_v24_2",
        "mt_link1": "https://example.link/mt_v24_1",
        "mt_link2": "https://example.link/mt_v24_2",
    },
    "VIP INJECTOR PROJECT V12": {
        "vip_link1": "https://example.link/v23_1",
        "vip_link2": "https://example.link/v23_2",
        "macro_link1": "https://example.link/macro_v23_1",
        "macro_link2": "https://example.link/macro_v23_2",
        "holo_link1": "https://example.link/holo_v23_1",
        "holo_link2": "https://example.link/holo_v23_2",
        "sketch_link1": "https://example.link/sketch_v23_1",
        "sketch_link2": "https://example.link/sketch_v23_2",
        "mt_link1": "https://example.link/mt_v23_1",
        "mt_link2": "https://example.link/mt_v23_2",
    },
    "VIP INJECTOR PROJECT V13": {
        "vip_link1": "https://example.link/v22_1",
        "vip_link2": "https://example.link/v22_2",
        "macro_link1": "https://example.link/macro_v22_1",
        "macro_link2": "https://example.link/macro_v22_2",
        "holo_link1": "https://example.link/holo_v22_1",
        "holo_link2": "https://example.link/holo_v22_2",
        "sketch_link1": "https://example.link/sketch_v22_1",
        "sketch_link2": "https://example.link/sketch_v22_2",
        "mt_link1": "https://example.link/mt_v22_1",
        "mt_link2": "https://example.link/mt_v22_2",
    },
    "VIP INJECTOR PROJECT V14": {
        "vip_link1": "https://example.link/v21_1",
        "vip_link2": "https://example.link/v21_2",
        "macro_link1": "https://example.link/macro_v21_1",
        "macro_link2": "https://example.link/macro_v21_2",
        "holo_link1": "https://example.link/holo_v21_1",
        "holo_link2": "https://example.link/holo_v21_2",
        "sketch_link1": "https://example.link/sketch_v21_1",
        "sketch_link2": "https://example.link/sketch_v21_2",
        "mt_link1": "https://example.link/mt_v21_1",
        "mt_link2": "https://example.link/mt_v21_2",
    },
    "VIP INJECTOR PROJECT V15": {
        "vip_link1": "https://example.link/v20_1",
        "vip_link2": "https://example.link/v20_2",
        "macro_link1": "https://example.link/macro_v20_1",
        "macro_link2": "https://example.link/macro_v20_2",
        "holo_link1": "https://example.link/holo_v20_1",
        "holo_link2": "https://example.link/holo_v20_2",
        "sketch_link1": "https://example.link/sketch_v20_1",
        "sketch_link2": "https://example.link/sketch_v20_2",
        "mt_link1": "https://example.link/mt_v20_1",
        "mt_link2": "https://example.link/mt_v20_2",
    },
    "VIP INJECTOR PROJECT V16": {
        "vip_link1": "https://example.link/v19_1",
        "vip_link2": "https://example.link/v19_2",
        "macro_link1": "https://example.link/macro_v19_1",
        "macro_link2": "https://example.link/macro_v19_2",
        "holo_link1": "https://example.link/holo_v19_1",
        "holo_link2": "https://example.link/holo_v19_2",
        "sketch_link1": "https://example.link/sketch_v19_1",
        "sketch_link2": "https://example.link/sketch_v19_2",
        "mt_link1": "https://example.link/mt_v19_1",
        "mt_link2": "https://example.link/mt_v19_2",
    },
    "VIP INJECTOR PROJECT V17": {
        "vip_link1": "https://example.link/v18_1",
        "vip_link2": "https://example.link/v18_2",
        "macro_link1": "https://example.link/macro_v18_1",
        "macro_link2": "https://example.link/macro_v18_2",
        "holo_link1": "https://example.link/holo_v18_1",
        "holo_link2": "https://example.link/holo_v18_2",
        "sketch_link1": "https://example.link/sketch_v18_1",
        "sketch_link2": "https://example.link/sketch_v18_2",
        "mt_link1": "https://example.link/mt_v18_1",
        "mt_link2": "https://example.link/mt_v18_2",
    },
    "VIP INJECTOR PROJECT V18": {
        "vip_link1": "https://example.link/v17_1",
        "vip_link2": "https://example.link/v17_2",
        "macro_link1": "https://example.link/macro_v17_1",
        "macro_link2": "https://example.link/macro_v17_2",
        "holo_link1": "https://example.link/holo_v17_1",
        "holo_link2": "https://example.link/holo_v17_2",
        "sketch_link1": "https://example.link/sketch_v17_1",
        "sketch_link2": "https://example.link/sketch_v17_2",
        "mt_link1": "https://example.link/mt_v17_1",
        "mt_link2": "https://example.link/mt_v17_2",
    },
    "VIP INJECTOR PROJECT V19": {
        "vip_link1": "https://example.link/v16_1",
        "vip_link2": "https://example.link/v16_2",
        "macro_link1": "https://example.link/macro_v16_1",
        "macro_link2": "https://example.link/macro_v16_2",
        "holo_link1": "https://example.link/holo_v16_1",
        "holo_link2": "https://example.link/holo_v16_2",
        "sketch_link1": "https://example.link/sketch_v16_1",
        "sketch_link2": "https://example.link/sketch_v16_2",
        "mt_link1": "https://example.link/mt_v16_1",
        "mt_link2": "https://example.link/mt_v16_2",
    },
    "VIP INJECTOR PROJECT V20": {
        "vip_link1": "https://example.link/v15_1",
        "vip_link2": "https://example.link/v15_2",
        "macro_link1": "https://example.link/macro_v15_1",
        "macro_link2": "https://example.link/macro_v15_2",
        "holo_link1": "https://example.link/holo_v15_1",
        "holo_link2": "https://example.link/holo_v15_2",
        "sketch_link1": "https://example.link/sketch_v15_1",
        "sketch_link2": "https://example.link/sketch_v15_2",
        "mt_link1": "https://example.link/mt_v15_1",
        "mt_link2": "https://example.link/mt_v15_2",
    },
    "VIP INJECTOR PROJECT V21": {
        "vip_link1": "https://example.link/v14_1",
        "vip_link2": "https://example.link/v14_2",
        "macro_link1": "https://example.link/macro_v14_1",
        "macro_link2": "https://example.link/macro_v14_2",
        "holo_link1": "https://example.link/holo_v14_1",
        "holo_link2": "https://example.link/holo_v14_2",
        "sketch_link1": "https://example.link/sketch_v14_1",
        "sketch_link2": "https://example.link/sketch_v14_2",
        "mt_link1": "https://example.link/mt_v14_1",
        "mt_link2": "https://example.link/mt_v14_2",
    },
    "VIP INJECTOR PROJECT V22": {
        "vip_link1": "https://example.link/v13_1",
        "vip_link2": "https://example.link/v13_2",
        "macro_link1": "https://example.link/macro_v13_1",
        "macro_link2": "https://example.link/macro_v13_2",
        "holo_link1": "https://example.link/holo_v13_1",
        "holo_link2": "https://example.link/holo_v13_2",
        "sketch_link1": "https://example.link/sketch_v13_1",
        "sketch_link2": "https://example.link/sketch_v13_2",
        "mt_link1": "https://example.link/mt_v13_1",
        "mt_link2": "https://example.link/mt_v13_2",
    },
    "VIP INJECTOR PROJECT V23": {
        "vip_link1": "https://example.link/v12_1",
        "vip_link2": "https://example.link/v12_2",
        "macro_link1": "https://example.link/macro_v12_1",
        "macro_link2": "https://example.link/macro_v12_2",
        "holo_link1": "https://example.link/holo_v12_1",
        "holo_link2": "https://example.link/holo_v12_2",
        "sketch_link1": "https://example.link/sketch_v12_1",
        "sketch_link2": "https://example.link/sketch_v12_2",
        "mt_link1": "https://example.link/mt_v12_1",
        "mt_link2": "https://example.link/mt_v12_2",
    },
    "VIP INJECTOR PROJECT V24": {
        "vip_link1": "https://example.link/v11_1",
        "vip_link2": "https://example.link/v11_2",
        "macro_link1": "https://example.link/macro_v11_1",
        "macro_link2": "https://example.link/macro_v11_2",
        "holo_link1": "https://example.link/holo_v11_1",
        "holo_link2": "https://example.link/holo_v11_2",
        "sketch_link1": "https://example.link/sketch_v11_1",
        "sketch_link2": "https://example.link/sketch_v11_2",
        "mt_link1": "https://example.link/mt_v11_1",
        "mt_link2": "https://example.link/mt_v11_2",
    },
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
    "<b>👇 <i>SELECT A PROJECT TO DOWNLOAD</i> 👇</b>"
)

# /start Command Handler
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_name = update.effective_user.first_name

    keyboard = [
        ["VIP INJECTOR PROJECT V1", "VIP INJECTOR PROJECT V2"],
        ["VIP INJECTOR PROJECT V3", "VIP INJECTOR PROJECT V4"],
        ["VIP INJECTOR PROJECT V5", "VIP INJECTOR PROJECT V6"],
        ["VIP INJECTOR PROJECT V7", "VIP INJECTOR PROJECT V8"],
        ["VIP INJECTOR PROJECT V9", "VIP INJECTOR PROJECT V10"],
        ["VIP INJECTOR PROJECT V11", "VIP INJECTOR PROJECT V12"],
        ["VIP INJECTOR PROJECT V13", "VIP INJECTOR PROJECT V14"],
        ["VIP INJECTOR PROJECT V15", "VIP INJECTOR PROJECT V16"],
        ["VIP INJECTOR PROJECT V17", "VIP INJECTOR PROJECT V18"],
        ["VIP INJECTOR PROJECT V19", "VIP INJECTOR PROJECT V20"],
        ["VIP INJECTOR PROJECT V21", "VIP INJECTOR PROJECT V22"],
        ["VIP INJECTOR PROJECT V23", "VIP INJECTOR PROJECT V24"]
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
    # .strip() लगाकर एक्स्ट्रा स्पेस की समस्या हमेशा के लिए हल कर दी गई है
    text = update.message.text.strip()

    if text in PROJECT_DATA:
        links = PROJECT_DATA[text]

        response_text = (
            f"{ROSHAN_BIG_TEXT}\n"
            "<b><i>👑 CREATED BY ROSHAN GUPTA 👑</i></b>\n"
            "<b><i>⚙️ VERSION 46.56.90.89 ⚙️</i></b>\n\n"
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
            "<b><i>DM</i> = @RoshanGaming ❗</b>"
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

