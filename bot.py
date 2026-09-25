import logging
from telegram import Update, ReplyKeyboardMarkup
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, filters, ContextTypes
from telegram.request import HTTPXRequest

# Logging Setup
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)

# 🔑 Apka Bot Token (Aapka Token Yahan Add Kar Diya Gaya Hai)
BOT_TOKEN = "8867333421:AAEzbeZAHLjnqO5iEDNi8v6Il43_oh_4K8Y"

# 🌐 Social Links Setup
TELEGRAM_LINK_1 = "https://t.me/RoshanGaming_bot"
TELEGRAM_LINK_2 = "https://t.me/RoshanPass_bot"
WHATSAPP_LINK = "https://wa.me/910000000000"
YOUTUBE_LINK = "https://youtube.com/@roshangaming"
FACEBOOK_LINK = "https://facebook.com/roshangaming"
INSTA_LINK = "https://instagram.com/roshangaming"

# Projects List
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

# 📥 Download Links Dictionary
PROJECT_DATA = {
    "VIP INJECTOR PROJECT V1": {
        "vip_link1": "https://drive.google.com/file/d/1au7rs42a1Vjsol2GfxeLVfBPSiFGHoVH/view?usp=drivesdk",
        "vip_link2": "https://drive.google.com/file/d/1au7rs42a1Vjsol2GfxeLVfBPSiFGHoVH/view?usp=drivesdk",
        "roshan_link1": "https://drive.google.com/file/d/1jUSPC3BwKtNA0MhLQWt8TNnsWNLMT0bY/view?usp=drivesdk",
        "roshan_link2": "https://drive.google.com/file/d/1jUSPC3BwKtNA0MhLQWt8TNnsWNLMT0bY/view?usp=drivesdk",
        "holo_link1": "https://drive.google.com/file/d/15krf_2W9-l6_1Hkh7f0YhHvYduh4BnNB/view?usp=drivesdk",
        "holo_link2": "https://drive.google.com/file/d/15krf_2W9-l6_1Hkh7f0YhHvYduh4BnNB/view?usp=drivesdk",
        "sketch_link1": "https://drive.google.com/file/d/18a9eeiD3Jojq-Q9C2FOkpLkL0yCT78K6/view?usp=drivesdk",
        "sketch_link2": "https://drive.google.com/file/d/18a9eeiD3Jojq-Q9C2FOkpLkL0yCT78K6/view?usp=drivesdk",
        "mt_link1": "https://drive.google.com/file/d/12I5z57mtsCrPBWkiHNR33S5bV7_UXHlc/view?usp=drivesdk",
        "mt_link2": "https://drive.google.com/file/d/12I5z57mtsCrPBWkiHNR33S5bV7_UXHlc/view?usp=drivesdk",
    },
    "VIP INJECTOR PROJECT V2": {
        "vip_link1": "https://drive.google.com/file/d/1Ehij8DQUdZoV106OYvzqiRz286SU-aLs/view?usp=drivesdk",
        "vip_link2": "https://drive.google.com/file/d/1Ehij8DQUdZoV106OYvzqiRz286SU-aLs/view?usp=drivesdk",
        "roshan_link1": "https://drive.google.com/file/d/1jUSPC3BwKtNA0MhLQWt8TNnsWNLMT0bY/view?usp=drivesdk",
        "roshan_link2": "https://drive.google.com/file/d/1jUSPC3BwKtNA0MhLQWt8TNnsWNLMT0bY/view?usp=drivesdk",
        "holo_link1": "https://drive.google.com/file/d/15krf_2W9-l6_1Hkh7f0YhHvYduh4BnNB/view?usp=drivesdk",
        "holo_link2": "https://drive.google.com/file/d/15krf_2W9-l6_1Hkh7f0YhHvYduh4BnNB/view?usp=drivesdk",
        "sketch_link1": "https://drive.google.com/file/d/18a9eeiD3Jojq-Q9C2FOkpLkL0yCT78K6/view?usp=drivesdk",
        "sketch_link2": "https://drive.google.com/file/d/18a9eeiD3Jojq-Q9C2FOkpLkL0yCT78K6/view?usp=drivesdk",
        "mt_link1": "https://drive.google.com/file/d/12I5z57mtsCrPBWkiHNR33S5bV7_UXHlc/view?usp=drivesdk",
        "mt_link2": "https://drive.google.com/file/d/12I5z57mtsCrPBWkiHNR33S5bV7_UXHlc/view?usp=drivesdk",
    },
    "VIP INJECTOR PROJECT V3": {
        "vip_link1": "https://drive.google.com/file/d/1sUfk0eUrtqXyHtRBjzCmtuwxxRyS83xK/view?usp=drivesdk",
        "vip_link2": "https://drive.google.com/file/d/1sUfk0eUrtqXyHtRBjzCmtuwxxRyS83xK/view?usp=drivesdk",
        "roshan_link1": "https://drive.google.com/file/d/1jUSPC3BwKtNA0MhLQWt8TNnsWNLMT0bY/view?usp=drivesdk",
        "roshan_link2": "https://drive.google.com/file/d/1jUSPC3BwKtNA0MhLQWt8TNnsWNLMT0bY/view?usp=drivesdk",
        "holo_link1": "https://drive.google.com/file/d/15krf_2W9-l6_1Hkh7f0YhHvYduh4BnNB/view?usp=drivesdk",
        "holo_link2": "https://drive.google.com/file/d/15krf_2W9-l6_1Hkh7f0YhHvYduh4BnNB/view?usp=drivesdk",
        "sketch_link1": "https://drive.google.com/file/d/18a9eeiD3Jojq-Q9C2FOkpLkL0yCT78K6/view?usp=drivesdk",
        "sketch_link2": "https://drive.google.com/file/d/18a9eeiD3Jojq-Q9C2FOkpLkL0yCT78K6/view?usp=drivesdk",
        "mt_link1": "https://drive.google.com/file/d/12I5z57mtsCrPBWkiHNR33S5bV7_UXHlc/view?usp=drivesdk",
        "mt_link2": "https://drive.google.com/file/d/12I5z57mtsCrPBWkiHNR33S5bV7_UXHlc/view?usp=drivesdk",
    },
    "VIP INJECTOR PROJECT V4": {
        "vip_link1": "https://drive.google.com/file/d/1z0sgE8V68tUOLhKfzOmFDK30om2ApqYu/view?usp=drivesdk",
        "vip_link2": "https://drive.google.com/file/d/1z0sgE8V68tUOLhKfzOmFDK30om2ApqYu/view?usp=drivesdk",
        "roshan_link1": "https://drive.google.com/file/d/1jUSPC3BwKtNA0MhLQWt8TNnsWNLMT0bY/view?usp=drivesdk",
        "roshan_link2": "https://drive.google.com/file/d/1jUSPC3BwKtNA0MhLQWt8TNnsWNLMT0bY/view?usp=drivesdk",
        "holo_link1": "https://drive.google.com/file/d/15krf_2W9-l6_1Hkh7f0YhHvYduh4BnNB/view?usp=drivesdk",
        "holo_link2": "https://drive.google.com/file/d/15krf_2W9-l6_1Hkh7f0YhHvYduh4BnNB/view?usp=drivesdk",
        "sketch_link1": "https://drive.google.com/file/d/18a9eeiD3Jojq-Q9C2FOkpLkL0yCT78K6/view?usp=drivesdk",
        "sketch_link2": "https://drive.google.com/file/d/18a9eeiD3Jojq-Q9C2FOkpLkL0yCT78K6/view?usp=drivesdk",
        "mt_link1": "https://drive.google.com/file/d/12I5z57mtsCrPBWkiHNR33S5bV7_UXHlc/view?usp=drivesdk",
        "mt_link2": "https://drive.google.com/file/d/12I5z57mtsCrPBWkiHNR33S5bV7_UXHlc/view?usp=drivesdk",
    },
    "VIP INJECTOR PROJECT V5": {
        "vip_link1": "https://drive.google.com/file/d/1lZ3zRc3ftHhiId6rB-jbtinzR07S0V6E/view?usp=drivesdk",
        "vip_link2": "https://drive.google.com/file/d/1lZ3zRc3ftHhiId6rB-jbtinzR07S0V6E/view?usp=drivesdk",
        "roshan_link1": "https://drive.google.com/file/d/1jUSPC3BwKtNA0MhLQWt8TNnsWNLMT0bY/view?usp=drivesdk",
        "roshan_link2": "https://drive.google.com/file/d/1jUSPC3BwKtNA0MhLQWt8TNnsWNLMT0bY/view?usp=drivesdk",
        "holo_link1": "https://drive.google.com/file/d/15krf_2W9-l6_1Hkh7f0YhHvYduh4BnNB/view?usp=drivesdk",
        "holo_link2": "https://drive.google.com/file/d/15krf_2W9-l6_1Hkh7f0YhHvYduh4BnNB/view?usp=drivesdk",
        "sketch_link1": "https://drive.google.com/file/d/18a9eeiD3Jojq-Q9C2FOkpLkL0yCT78K6/view?usp=drivesdk",
        "sketch_link2": "https://drive.google.com/file/d/18a9eeiD3Jojq-Q9C2FOkpLkL0yCT78K6/view?usp=drivesdk",
        "mt_link1": "https://drive.google.com/file/d/12I5z57mtsCrPBWkiHNR33S5bV7_UXHlc/view?usp=drivesdk",
        "mt_link2": "https://drive.google.com/file/d/12I5z57mtsCrPBWkiHNR33S5bV7_UXHlc/view?usp=drivesdk",
    },
    "VIP INJECTOR PROJECT V6": {
        "vip_link1": "https://example.link/v29_1",
        "vip_link2": "https://example.link/v29_2",
        "roshan_link1": "https://drive.google.com/file/d/1jUSPC3BwKtNA0MhLQWt8TNnsWNLMT0bY/view?usp=drivesdk",
        "roshan_link2": "https://drive.google.com/file/d/1jUSPC3BwKtNA0MhLQWt8TNnsWNLMT0bY/view?usp=drivesdk",
        "holo_link1": "https://drive.google.com/file/d/15krf_2W9-l6_1Hkh7f0YhHvYduh4BnNB/view?usp=drivesdk",
        "holo_link2": "https://drive.google.com/file/d/15krf_2W9-l6_1Hkh7f0YhHvYduh4BnNB/view?usp=drivesdk",
        "sketch_link1": "https://drive.google.com/file/d/18a9eeiD3Jojq-Q9C2FOkpLkL0yCT78K6/view?usp=drivesdk",
        "sketch_link2": "https://drive.google.com/file/d/18a9eeiD3Jojq-Q9C2FOkpLkL0yCT78K6/view?usp=drivesdk",
        "mt_link1": "https://drive.google.com/file/d/12I5z57mtsCrPBWkiHNR33S5bV7_UXHlc/view?usp=drivesdk",
        "mt_link2": "https://drive.google.com/file/d/12I5z57mtsCrPBWkiHNR33S5bV7_UXHlc/view?usp=drivesdk",
    },
    "VIP INJECTOR PROJECT V7": {
        "vip_link1": "https://drive.google.com/file/d/1HXv7WfVQxH564FeEas0TLSWhaJR0i2hp/view?usp=drivesdk",
        "vip_link2": "https://drive.google.com/file/d/1HXv7WfVQxH564FeEas0TLSWhaJR0i2hp/view?usp=drivesdk",
        "roshan_link1": "https://drive.google.com/file/d/1jUSPC3BwKtNA0MhLQWt8TNnsWNLMT0bY/view?usp=drivesdk",
        "roshan_link2": "https://drive.google.com/file/d/1jUSPC3BwKtNA0MhLQWt8TNnsWNLMT0bY/view?usp=drivesdk",
        "holo_link1": "https://drive.google.com/file/d/15krf_2W9-l6_1Hkh7f0YhHvYduh4BnNB/view?usp=drivesdk",
        "holo_link2": "https://drive.google.com/file/d/15krf_2W9-l6_1Hkh7f0YhHvYduh4BnNB/view?usp=drivesdk",
        "sketch_link1": "https://drive.google.com/file/d/18a9eeiD3Jojq-Q9C2FOkpLkL0yCT78K6/view?usp=drivesdk",
        "sketch_link2": "https://drive.google.com/file/d/18a9eeiD3Jojq-Q9C2FOkpLkL0yCT78K6/view?usp=drivesdk",
        "mt_link1": "https://drive.google.com/file/d/12I5z57mtsCrPBWkiHNR33S5bV7_UXHlc/view?usp=drivesdk",
        "mt_link2": "https://drive.google.com/file/d/12I5z57mtsCrPBWkiHNR33S5bV7_UXHlc/view?usp=drivesdk",
    },
    "VIP INJECTOR PROJECT V8": {
        "vip_link1": "https://drive.google.com/file/d/1n_8T2SQo3_YTuCpmZpmo4td0nqWf8TCd/view?usp=drivesdk",
        "vip_link2": "https://drive.google.com/file/d/1n_8T2SQo3_YTuCpmZpmo4td0nqWf8TCd/view?usp=drivesdk",
        "roshan_link1": "https://drive.google.com/file/d/1jUSPC3BwKtNA0MhLQWt8TNnsWNLMT0bY/view?usp=drivesdk",
        "roshan_link2": "https://drive.google.com/file/d/1jUSPC3BwKtNA0MhLQWt8TNnsWNLMT0bY/view?usp=drivesdk",
        "holo_link1": "https://drive.google.com/file/d/15krf_2W9-l6_1Hkh7f0YhHvYduh4BnNB/view?usp=drivesdk",
        "holo_link2": "https://drive.google.com/file/d/15krf_2W9-l6_1Hkh7f0YhHvYduh4BnNB/view?usp=drivesdk",
        "sketch_link1": "https://drive.google.com/file/d/18a9eeiD3Jojq-Q9C2FOkpLkL0yCT78K6/view?usp=drivesdk",
        "sketch_link2": "https://drive.google.com/file/d/18a9eeiD3Jojq-Q9C2FOkpLkL0yCT78K6/view?usp=drivesdk",
        "mt_link1": "https://drive.google.com/file/d/12I5z57mtsCrPBWkiHNR33S5bV7_UXHlc/view?usp=drivesdk",
        "mt_link2": "https://drive.google.com/file/d/12I5z57mtsCrPBWkiHNR33S5bV7_UXHlc/view?usp=drivesdk",
    },
    "VIP INJECTOR PROJECT V9": {
        "vip_link1": "https://drive.google.com/file/d/1v_thD83lIuB5KeVrA5XmQdFpUH3sBnzl/view?usp=drivesdk",
        "vip_link2": "https://drive.google.com/file/d/1v_thD83lIuB5KeVrA5XmQdFpUH3sBnzl/view?usp=drivesdk",
        "roshan_link1": "https://drive.google.com/file/d/1jUSPC3BwKtNA0MhLQWt8TNnsWNLMT0bY/view?usp=drivesdk",
        "roshan_link2": "https://drive.google.com/file/d/1jUSPC3BwKtNA0MhLQWt8TNnsWNLMT0bY/view?usp=drivesdk",
        "holo_link1": "https://drive.google.com/file/d/15krf_2W9-l6_1Hkh7f0YhHvYduh4BnNB/view?usp=drivesdk",
        "holo_link2": "https://drive.google.com/file/d/15krf_2W9-l6_1Hkh7f0YhHvYduh4BnNB/view?usp=drivesdk",
        "sketch_link1": "https://drive.google.com/file/d/18a9eeiD3Jojq-Q9C2FOkpLkL0yCT78K6/view?usp=drivesdk",
        "sketch_link2": "https://drive.google.com/file/d/18a9eeiD3Jojq-Q9C2FOkpLkL0yCT78K6/view?usp=drivesdk",
        "mt_link1": "https://drive.google.com/file/d/12I5z57mtsCrPBWkiHNR33S5bV7_UXHlc/view?usp=drivesdk",
        "mt_link2": "https://drive.google.com/file/d/12I5z57mtsCrPBWkiHNR33S5bV7_UXHlc/view?usp=drivesdk",
    },
    "VIP INJECTOR PROJECT V10": {
        "vip_link1": "https://drive.google.com/file/d/1bNSHkL3KwlYpCGxKG2CEZ9tbCexPDw6x/view?usp=drivesdk",
        "vip_link2": "https://drive.google.com/file/d/1bNSHkL3KwlYpCGxKG2CEZ9tbCexPDw6x/view?usp=drivesdk",
        "roshan_link1": "https://drive.google.com/file/d/1jUSPC3BwKtNA0MhLQWt8TNnsWNLMT0bY/view?usp=drivesdk",
        "roshan_link2": "https://drive.google.com/file/d/1jUSPC3BwKtNA0MhLQWt8TNnsWNLMT0bY/view?usp=drivesdk",
        "holo_link1": "https://drive.google.com/file/d/15krf_2W9-l6_1Hkh7f0YhHvYduh4BnNB/view?usp=drivesdk",
        "holo_link2": "https://drive.google.com/file/d/15krf_2W9-l6_1Hkh7f0YhHvYduh4BnNB/view?usp=drivesdk",
        "sketch_link1": "https://drive.google.com/file/d/18a9eeiD3Jojq-Q9C2FOkpLkL0yCT78K6/view?usp=drivesdk",
        "sketch_link2": "https://drive.google.com/file/d/18a9eeiD3Jojq-Q9C2FOkpLkL0yCT78K6/view?usp=drivesdk",
        "mt_link1": "https://drive.google.com/file/d/12I5z57mtsCrPBWkiHNR33S5bV7_UXHlc/view?usp=drivesdk",
        "mt_link2": "https://drive.google.com/file/d/12I5z57mtsCrPBWkiHNR33S5bV7_UXHlc/view?usp=drivesdk",
    },
    "VIP INJECTOR PROJECT V11": {
        "vip_link1": "https://drive.google.com/file/d/1YmG6jtbqayGYtr94eLT4XmnmMAHct11q/view?usp=drivesdk",
        "vip_link2": "https://drive.google.com/file/d/1YmG6jtbqayGYtr94eLT4XmnmMAHct11q/view?usp=drivesdk",
        "roshan_link1": "https://drive.google.com/file/d/1jUSPC3BwKtNA0MhLQWt8TNnsWNLMT0bY/view?usp=drivesdk",
        "roshan_link2": "https://drive.google.com/file/d/1jUSPC3BwKtNA0MhLQWt8TNnsWNLMT0bY/view?usp=drivesdk",
        "holo_link1": "https://drive.google.com/file/d/15krf_2W9-l6_1Hkh7f0YhHvYduh4BnNB/view?usp=drivesdk",
        "holo_link2": "https://drive.google.com/file/d/15krf_2W9-l6_1Hkh7f0YhHvYduh4BnNB/view?usp=drivesdk",
        "sketch_link1": "https://drive.google.com/file/d/18a9eeiD3Jojq-Q9C2FOkpLkL0yCT78K6/view?usp=drivesdk",
        "sketch_link2": "https://drive.google.com/file/d/18a9eeiD3Jojq-Q9C2FOkpLkL0yCT78K6/view?usp=drivesdk",
        "mt_link1": "https://drive.google.com/file/d/12I5z57mtsCrPBWkiHNR33S5bV7_UXHlc/view?usp=drivesdk",
        "mt_link2": "https://drive.google.com/file/d/12I5z57mtsCrPBWkiHNR33S5bV7_UXHlc/view?usp=drivesdk",
    },
    "VIP INJECTOR PROJECT V12": {
        "vip_link1": "https://drive.google.com/file/d/1soKiHBq0SPNrc2aYs5VrO0NFfUXQ6itS/view?usp=drivesdk",
        "vip_link2": "https://drive.google.com/file/d/1soKiHBq0SPNrc2aYs5VrO0NFfUXQ6itS/view?usp=drivesdk",
        "roshan_link1": "https://drive.google.com/file/d/1jUSPC3BwKtNA0MhLQWt8TNnsWNLMT0bY/view?usp=drivesdk",
        "roshan_link2": "https://drive.google.com/file/d/1jUSPC3BwKtNA0MhLQWt8TNnsWNLMT0bY/view?usp=drivesdk",
        "holo_link1": "https://drive.google.com/file/d/15krf_2W9-l6_1Hkh7f0YhHvYduh4BnNB/view?usp=drivesdk",
        "holo_link2": "https://drive.google.com/file/d/15krf_2W9-l6_1Hkh7f0YhHvYduh4BnNB/view?usp=drivesdk",
        "sketch_link1": "https://drive.google.com/file/d/18a9eeiD3Jojq-Q9C2FOkpLkL0yCT78K6/view?usp=drivesdk",
        "sketch_link2": "https://drive.google.com/file/d/18a9eeiD3Jojq-Q9C2FOkpLkL0yCT78K6/view?usp=drivesdk",
        "mt_link1": "https://drive.google.com/file/d/12I5z57mtsCrPBWkiHNR33S5bV7_UXHlc/view?usp=drivesdk",
        "mt_link2": "https://drive.google.com/file/d/12I5z57mtsCrPBWkiHNR33S5bV7_UXHlc/view?usp=drivesdk",
    },
    "VIP INJECTOR PROJECT V13": {
        "vip_link1": "https://drive.google.com/file/d/1Oi0cuz-1ueBN0_IhfQPDLDTVlnnOhaME/view?usp=drivesdk",
        "vip_link2": "https://drive.google.com/file/d/1Oi0cuz-1ueBN0_IhfQPDLDTVlnnOhaME/view?usp=drivesdk",
        "roshan_link1": "https://drive.google.com/file/d/1jUSPC3BwKtNA0MhLQWt8TNnsWNLMT0bY/view?usp=drivesdk",
        "roshan_link2": "https://drive.google.com/file/d/1jUSPC3BwKtNA0MhLQWt8TNnsWNLMT0bY/view?usp=drivesdk",
        "holo_link1": "https://drive.google.com/file/d/15krf_2W9-l6_1Hkh7f0YhHvYduh4BnNB/view?usp=drivesdk",
        "holo_link2": "https://drive.google.com/file/d/15krf_2W9-l6_1Hkh7f0YhHvYduh4BnNB/view?usp=drivesdk",
        "sketch_link1": "https://drive.google.com/file/d/18a9eeiD3Jojq-Q9C2FOkpLkL0yCT78K6/view?usp=drivesdk",
        "sketch_link2": "https://drive.google.com/file/d/18a9eeiD3Jojq-Q9C2FOkpLkL0yCT78K6/view?usp=drivesdk",
        "mt_link1": "https://drive.google.com/file/d/12I5z57mtsCrPBWkiHNR33S5bV7_UXHlc/view?usp=drivesdk",
        "mt_link2": "https://drive.google.com/file/d/12I5z57mtsCrPBWkiHNR33S5bV7_UXHlc/view?usp=drivesdk",
    },
    "VIP INJECTOR PROJECT V14": {
        "vip_link1": "https://drive.google.com/file/d/1dlX6EW4QuZgtBhtFtRIMOvxxyflpYR0S/view?usp=drivesdk",
        "vip_link2": "https://drive.google.com/file/d/1dlX6EW4QuZgtBhtFtRIMOvxxyflpYR0S/view?usp=drivesdk",
        "roshan_link1": "https://drive.google.com/file/d/1jUSPC3BwKtNA0MhLQWt8TNnsWNLMT0bY/view?usp=drivesdk",
        "roshan_link2": "https://drive.google.com/file/d/1jUSPC3BwKtNA0MhLQWt8TNnsWNLMT0bY/view?usp=drivesdk",
        "holo_link1": "https://drive.google.com/file/d/15krf_2W9-l6_1Hkh7f0YhHvYduh4BnNB/view?usp=drivesdk",
        "holo_link2": "https://drive.google.com/file/d/15krf_2W9-l6_1Hkh7f0YhHvYduh4BnNB/view?usp=drivesdk",
        "sketch_link1": "https://drive.google.com/file/d/18a9eeiD3Jojq-Q9C2FOkpLkL0yCT78K6/view?usp=drivesdk",
        "sketch_link2": "https://drive.google.com/file/d/18a9eeiD3Jojq-Q9C2FOkpLkL0yCT78K6/view?usp=drivesdk",
        "mt_link1": "https://drive.google.com/file/d/12I5z57mtsCrPBWkiHNR33S5bV7_UXHlc/view?usp=drivesdk",
        "mt_link2": "https://drive.google.com/file/d/12I5z57mtsCrPBWkiHNR33S5bV7_UXHlc/view?usp=drivesdk",
    },
    "VIP INJECTOR PROJECT V15": {
        "vip_link1": "https://drive.google.com/file/d/1SyHFPtnoQY8Y7YmXxmNw3uLg42vwMc6i/view?usp=drivesdk",
        "vip_link2": "https://drive.google.com/file/d/1SyHFPtnoQY8Y7YmXxmNw3uLg42vwMc6i/view?usp=drivesdk",
        "roshan_link1": "https://drive.google.com/file/d/1jUSPC3BwKtNA0MhLQWt8TNnsWNLMT0bY/view?usp=drivesdk",
        "roshan_link2": "https://drive.google.com/file/d/1jUSPC3BwKtNA0MhLQWt8TNnsWNLMT0bY/view?usp=drivesdk",
        "holo_link1": "https://drive.google.com/file/d/15krf_2W9-l6_1Hkh7f0YhHvYduh4BnNB/view?usp=drivesdk",
        "holo_link2": "https://drive.google.com/file/d/15krf_2W9-l6_1Hkh7f0YhHvYduh4BnNB/view?usp=drivesdk",
        "sketch_link1": "https://drive.google.com/file/d/18a9eeiD3Jojq-Q9C2FOkpLkL0yCT78K6/view?usp=drivesdk",
        "sketch_link2": "https://drive.google.com/file/d/18a9eeiD3Jojq-Q9C2FOkpLkL0yCT78K6/view?usp=drivesdk",
        "mt_link1": "https://drive.google.com/file/d/12I5z57mtsCrPBWkiHNR33S5bV7_UXHlc/view?usp=drivesdk",
        "mt_link2": "https://drive.google.com/file/d/12I5z57mtsCrPBWkiHNR33S5bV7_UXHlc/view?usp=drivesdk",
    },
    "VIP INJECTOR PROJECT V16": {
        "vip_link1": "https://drive.google.com/file/d/1pxSfjk744ICXchDyHx4lmCK3W1nvxKK4/view?usp=drivesdk",
        "vip_link2": "https://drive.google.com/file/d/1pxSfjk744ICXchDyHx4lmCK3W1nvxKK4/view?usp=drivesdk",
        "roshan_link1": "https://drive.google.com/file/d/1jUSPC3BwKtNA0MhLQWt8TNnsWNLMT0bY/view?usp=drivesdk",
        "roshan_link2": "https://drive.google.com/file/d/1jUSPC3BwKtNA0MhLQWt8TNnsWNLMT0bY/view?usp=drivesdk",
        "holo_link1": "https://drive.google.com/file/d/15krf_2W9-l6_1Hkh7f0YhHvYduh4BnNB/view?usp=drivesdk",
        "holo_link2": "https://drive.google.com/file/d/15krf_2W9-l6_1Hkh7f0YhHvYduh4BnNB/view?usp=drivesdk",
        "sketch_link1": "https://drive.google.com/file/d/18a9eeiD3Jojq-Q9C2FOkpLkL0yCT78K6/view?usp=drivesdk",
        "sketch_link2": "https://drive.google.com/file/d/18a9eeiD3Jojq-Q9C2FOkpLkL0yCT78K6/view?usp=drivesdk",
        "mt_link1": "https://drive.google.com/file/d/12I5z57mtsCrPBWkiHNR33S5bV7_UXHlc/view?usp=drivesdk",
        "mt_link2": "https://drive.google.com/file/d/12I5z57mtsCrPBWkiHNR33S5bV7_UXHlc/view?usp=drivesdk",
    },
    "VIP INJECTOR PROJECT V17": {
        "vip_link1": "https://drive.google.com/file/d/1s_YA_RT1rINzGgIV4qg3V6S5_gfedpMk/view?usp=drivesdk",
        "vip_link2": "https://drive.google.com/file/d/1s_YA_RT1rINzGgIV4qg3V6S5_gfedpMk/view?usp=drivesdk",
        "roshan_link1": "https://drive.google.com/file/d/1jUSPC3BwKtNA0MhLQWt8TNnsWNLMT0bY/view?usp=drivesdk",
        "roshan_link2": "https://drive.google.com/file/d/1jUSPC3BwKtNA0MhLQWt8TNnsWNLMT0bY/view?usp=drivesdk",
        "holo_link1": "https://drive.google.com/file/d/15krf_2W9-l6_1Hkh7f0YhHvYduh4BnNB/view?usp=drivesdk",
        "holo_link2": "https://drive.google.com/file/d/15krf_2W9-l6_1Hkh7f0YhHvYduh4BnNB/view?usp=drivesdk",
        "sketch_link1": "https://drive.google.com/file/d/18a9eeiD3Jojq-Q9C2FOkpLkL0yCT78K6/view?usp=drivesdk",
        "sketch_link2": "https://drive.google.com/file/d/18a9eeiD3Jojq-Q9C2FOkpLkL0yCT78K6/view?usp=drivesdk",
        "mt_link1": "https://drive.google.com/file/d/12I5z57mtsCrPBWkiHNR33S5bV7_UXHlc/view?usp=drivesdk",
        "mt_link2": "https://drive.google.com/file/d/12I5z57mtsCrPBWkiHNR33S5bV7_UXHlc/view?usp=drivesdk",
    },
    "VIP INJECTOR PROJECT V18": {
        "vip_link1": "https://drive.google.com/file/d/1alziTL13ZrJ_vJK1YwYRu9IXkxbBbvgu/view?usp=drivesdk",
        "vip_link2": "https://drive.google.com/file/d/1alziTL13ZrJ_vJK1YwYRu9IXkxbBbvgu/view?usp=drivesdk",
        "roshan_link1": "https://drive.google.com/file/d/1jUSPC3BwKtNA0MhLQWt8TNnsWNLMT0bY/view?usp=drivesdk",
        "roshan_link2": "https://drive.google.com/file/d/1jUSPC3BwKtNA0MhLQWt8TNnsWNLMT0bY/view?usp=drivesdk",
        "holo_link1": "https://drive.google.com/file/d/15krf_2W9-l6_1Hkh7f0YhHvYduh4BnNB/view?usp=drivesdk",
        "holo_link2": "https://drive.google.com/file/d/15krf_2W9-l6_1Hkh7f0YhHvYduh4BnNB/view?usp=drivesdk",
        "sketch_link1": "https://drive.google.com/file/d/18a9eeiD3Jojq-Q9C2FOkpLkL0yCT78K6/view?usp=drivesdk",
        "sketch_link2": "https://drive.google.com/file/d/18a9eeiD3Jojq-Q9C2FOkpLkL0yCT78K6/view?usp=drivesdk",
        "mt_link1": "https://drive.google.com/file/d/12I5z57mtsCrPBWkiHNR33S5bV7_UXHlc/view?usp=drivesdk",
        "mt_link2": "https://drive.google.com/file/d/12I5z57mtsCrPBWkiHNR33S5bV7_UXHlc/view?usp=drivesdk",
    },
    "VIP INJECTOR PROJECT V19": {
        "vip_link1": "https://drive.google.com/file/d/1EQKXvLSOIE114gzxd8ZCOhznBqK5LwwT/view?usp=drivesdk",
        "vip_link2": "https://drive.google.com/file/d/1EQKXvLSOIE114gzxd8ZCOhznBqK5LwwT/view?usp=drivesdk",
        "roshan_link1": "https://drive.google.com/file/d/1jUSPC3BwKtNA0MhLQWt8TNnsWNLMT0bY/view?usp=drivesdk",
        "roshan_link2": "https://drive.google.com/file/d/1jUSPC3BwKtNA0MhLQWt8TNnsWNLMT0bY/view?usp=drivesdk",
        "holo_link1": "https://drive.google.com/file/d/15krf_2W9-l6_1Hkh7f0YhHvYduh4BnNB/view?usp=drivesdk",
        "holo_link2": "https://drive.google.com/file/d/15krf_2W9-l6_1Hkh7f0YhHvYduh4BnNB/view?usp=drivesdk",
        "sketch_link1": "https://drive.google.com/file/d/18a9eeiD3Jojq-Q9C2FOkpLkL0yCT78K6/view?usp=drivesdk",
        "sketch_link2": "https://drive.google.com/file/d/18a9eeiD3Jojq-Q9C2FOkpLkL0yCT78K6/view?usp=drivesdk",
        "mt_link1": "https://drive.google.com/file/d/12I5z57mtsCrPBWkiHNR33S5bV7_UXHlc/view?usp=drivesdk",
        "mt_link2": "https://drive.google.com/file/d/12I5z57mtsCrPBWkiHNR33S5bV7_UXHlc/view?usp=drivesdk",
    },
    "VIP INJECTOR PROJECT V20": {
        "vip_link1": "https://drive.google.com/file/d/1J_jqNV3CSpNSBr15TSFVhl09AQcRwRTq/view?usp=drivesdk",
        "vip_link2": "https://drive.google.com/file/d/1J_jqNV3CSpNSBr15TSFVhl09AQcRwRTq/view?usp=drivesdk",
        "roshan_link1": "https://drive.google.com/file/d/1jUSPC3BwKtNA0MhLQWt8TNnsWNLMT0bY/view?usp=drivesdk",
        "roshan_link2": "https://drive.google.com/file/d/1jUSPC3BwKtNA0MhLQWt8TNnsWNLMT0bY/view?usp=drivesdk",
        "holo_link1": "https://drive.google.com/file/d/15krf_2W9-l6_1Hkh7f0YhHvYduh4BnNB/view?usp=drivesdk",
        "holo_link2": "https://drive.google.com/file/d/15krf_2W9-l6_1Hkh7f0YhHvYduh4BnNB/view?usp=drivesdk",
        "sketch_link1": "https://drive.google.com/file/d/18a9eeiD3Jojq-Q9C2FOkpLkL0yCT78K6/view?usp=drivesdk",
        "sketch_link2": "https://drive.google.com/file/d/18a9eeiD3Jojq-Q9C2FOkpLkL0yCT78K6/view?usp=drivesdk",
        "mt_link1": "https://drive.google.com/file/d/12I5z57mtsCrPBWkiHNR33S5bV7_UXHlc/view?usp=drivesdk",
        "mt_link2": "https://drive.google.com/file/d/12I5z57mtsCrPBWkiHNR33S5bV7_UXHlc/view?usp=drivesdk",
    },
    "VIP INJECTOR PROJECT V21": {
        "vip_link1": "https://example.link/v14_1",
        "vip_link2": "https://example.link/v14_2",
        "roshan_link1": "https://drive.google.com/file/d/1jUSPC3BwKtNA0MhLQWt8TNnsWNLMT0bY/view?usp=drivesdk",
        "roshan_link2": "https://drive.google.com/file/d/1jUSPC3BwKtNA0MhLQWt8TNnsWNLMT0bY/view?usp=drivesdk",
        "holo_link1": "https://drive.google.com/file/d/15krf_2W9-l6_1Hkh7f0YhHvYduh4BnNB/view?usp=drivesdk",
        "holo_link2": "https://drive.google.com/file/d/15krf_2W9-l6_1Hkh7f0YhHvYduh4BnNB/view?usp=drivesdk",
        "sketch_link1": "https://drive.google.com/file/d/18a9eeiD3Jojq-Q9C2FOkpLkL0yCT78K6/view?usp=drivesdk",
        "sketch_link2": "https://drive.google.com/file/d/18a9eeiD3Jojq-Q9C2FOkpLkL0yCT78K6/view?usp=drivesdk",
        "mt_link1": "https://drive.google.com/file/d/12I5z57mtsCrPBWkiHNR33S5bV7_UXHlc/view?usp=drivesdk",
        "mt_link2": "https://drive.google.com/file/d/12I5z57mtsCrPBWkiHNR33S5bV7_UXHlc/view?usp=drivesdk",
    },
    "VIP INJECTOR PROJECT V22": {
        "vip_link1": "https://example.link/v13_1",
        "vip_link2": "https://example.link/v13_2",
        "roshan_link1": "https://drive.google.com/file/d/1jUSPC3BwKtNA0MhLQWt8TNnsWNLMT0bY/view?usp=drivesdk",
        "roshan_link2": "https://drive.google.com/file/d/1jUSPC3BwKtNA0MhLQWt8TNnsWNLMT0bY/view?usp=drivesdk",
        "holo_link1": "https://drive.google.com/file/d/15krf_2W9-l6_1Hkh7f0YhHvYduh4BnNB/view?usp=drivesdk",
        "holo_link2": "https://drive.google.com/file/d/15krf_2W9-l6_1Hkh7f0YhHvYduh4BnNB/view?usp=drivesdk",
        "sketch_link1": "https://drive.google.com/file/d/18a9eeiD3Jojq-Q9C2FOkpLkL0yCT78K6/view?usp=drivesdk",
        "sketch_link2": "https://drive.google.com/file/d/18a9eeiD3Jojq-Q9C2FOkpLkL0yCT78K6/view?usp=drivesdk",
        "mt_link1": "https://drive.google.com/file/d/12I5z57mtsCrPBWkiHNR33S5bV7_UXHlc/view?usp=drivesdk",
        "mt_link2": "https://drive.google.com/file/d/12I5z57mtsCrPBWkiHNR33S5bV7_UXHlc/view?usp=drivesdk",
    },
    "VIP INJECTOR PROJECT V23": {
        "vip_link1": "https://example.link/v12_1",
        "vip_link2": "https://example.link/v12_2",
        "roshan_link1": "https://drive.google.com/file/d/1jUSPC3BwKtNA0MhLQWt8TNnsWNLMT0bY/view?usp=drivesdk",
        "roshan_link2": "https://drive.google.com/file/d/1jUSPC3BwKtNA0MhLQWt8TNnsWNLMT0bY/view?usp=drivesdk",
        "holo_link1": "https://drive.google.com/file/d/15krf_2W9-l6_1Hkh7f0YhHvYduh4BnNB/view?usp=drivesdk",
        "holo_link2": "https://drive.google.com/file/d/15krf_2W9-l6_1Hkh7f0YhHvYduh4BnNB/view?usp=drivesdk",
        "sketch_link1": "https://drive.google.com/file/d/18a9eeiD3Jojq-Q9C2FOkpLkL0yCT78K6/view?usp=drivesdk",
        "sketch_link2": "https://drive.google.com/file/d/18a9eeiD3Jojq-Q9C2FOkpLkL0yCT78K6/view?usp=drivesdk",
        "mt_link1": "https://drive.google.com/file/d/12I5z57mtsCrPBWkiHNR33S5bV7_UXHlc/view?usp=drivesdk",
        "mt_link2": "https://drive.google.com/file/d/12I5z57mtsCrPBWkiHNR33S5bV7_UXHlc/view?usp=drivesdk",
    },
    "VIP INJECTOR PROJECT V24": {
        "vip_link1": "https://example.link/v11_1",
        "vip_link2": "https://example.link/v11_2",
        "roshan_link1": "https://drive.google.com/file/d/1jUSPC3BwKtNA0MhLQWt8TNnsWNLMT0bY/view?usp=drivesdk",
        "roshan_link2": "https://drive.google.com/file/d/1jUSPC3BwKtNA0MhLQWt8TNnsWNLMT0bY/view?usp=drivesdk",
        "holo_link1": "https://drive.google.com/file/d/15krf_2W9-l6_1Hkh7f0YhHvYduh4BnNB/view?usp=drivesdk",
        "holo_link2": "https://drive.google.com/file/d/15krf_2W9-l6_1Hkh7f0YhHvYduh4BnNB/view?usp=drivesdk",
        "sketch_link1": "https://drive.google.com/file/d/18a9eeiD3Jojq-Q9C2FOkpLkL0yCT78K6/view?usp=drivesdk",
        "sketch_link2": "https://drive.google.com/file/d/18a9eeiD3Jojq-Q9C2FOkpLkL0yCT78K6/view?usp=drivesdk",
        "mt_link1": "https://drive.google.com/file/d/12I5z57mtsCrPBWkiHNR33S5bV7_UXHlc/view?usp=drivesdk",
        "mt_link2": "https://drive.google.com/file/d/12I5z57mtsCrPBWkiHNR33S5bV7_UXHlc/view?usp=drivesdk",
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
            f"  ☆ <a href='{links['vip_link1']}'><b><i>Click Your File</i></b></a>\n"
            f"  ☆ <a href='{links['vip_link2']}'><b><i>Click Your File</i></b></a>\n"
            f"╚═══════════════════════════╝\n\n"
            "<b><i>ROSHAN GAMING BOX :</i></b>\n"
            f"╔═══════════════════════════╗\n"
            f"  ☆ <a href='{links['roshan_link1']}'><b><i>Click Your File</i></b></a>\n"
            f"  ☆ <a href='{links['roshan_link2']}'><b><i>Click Your File</i></b></a>\n"
            f"╚═══════════════════════════╝\n\n"
            "<b><i>HOLOGRAM ALL TYPES FILES :</i></b>\n"
            f"╔═══════════════════════════╗\n"
            f"  ☆ <a href='{links['holo_link1']}'><b><i>Click Your File</i></b></a>\n"
            f"  ☆ <a href='{links['holo_link2']}'><b><i>Click Your File</i></b></a>\n"
            f"╚═══════════════════════════╝\n\n"
            "<b><i>Sketchware Pro Apks :</i></b>\n"
            f"╔═══════════════════════════╗\n"
            f"  ☆ <a href='{links['sketch_link1']}'><b><i>Click Your File</i></b></a>\n"
            f"  ☆ <a href='{links['sketch_link2']}'><b><i>Click Your File</i></b></a>\n"
            f"╚═══════════════════════════╝\n\n"
            "<b><i>Mt Manager Apk :</i></b>\n"
            f"╔═══════════════════════════╗\n"
            f"  ☆ <a href='{links['mt_link1']}'><b><i>Click Your File</i></b></a>\n"
            f"  ☆ <a href='{links['mt_link2']}'><b><i>Click Your File</i></b></a>\n"
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
