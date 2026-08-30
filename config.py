import logging

from telethon import TelegramClient

from os import getenv
from RAUSHAN.data import ALTRON


logging.basicConfig(format='[%(levelname) 5s/%(asctime)s] %(name)s: %(message)s', level=logging.WARNING)


# VALUES REQUIRED FOR XBOTS
API_ID = "34929833"
API_HASH = "f1bf670e54f5732bbb9079e26c469da4"
CMD_HNDLR = getenv("CMD_HNDLR", default=".")
HEROKU_APP_NAME = getenv("HEROKU_APP_NAME", None)
HEROKU_API_KEY = getenv("HEROKU_API_KEY", "cb2147ff-d743-49fc-a18e-6a40aec75e77")

BOT_TOKEN = "8696386138:AAHhe4c-dRoS78nAxuTvgLIx0LvNasToRFM"
BOT_TOKEN2 = "7968906067:AAEQSucRuDEIPNCHKMft3Aqu5xNg_uAie40"
BOT_TOKEN3 = "8893886562:AAHLAmq540sETAZEHLjfe4nKMki3olDPwPo"
BOT_TOKEN4 = "8927544648:AAG0uDOSrDHB97ahm8t0HSp80biGUq6Vd5U"
BOT_TOKEN5 = "8909202914:AAGJUBXzoe5zvCguX-4UlunltaxEsoGh-LI"
BOT_TOKEN6 = "8705262279:AAHEckIUmNvk-2IG8u-tryBFrRPvrGkY8Fw"
BOT_TOKEN7 = "8998647534:AAHrZ9h8v9vKF05kujyOuhG6mlL8Zpo-DMk"
BOT_TOKEN8 = "8967151295:AAGLAcWEq011bVij3LZcpMDK-JmFcG9J3Xw"
BOT_TOKEN9 = "8729334114:AAGZGl7jO62ZbClz4gWJoATxcKc4tHIyt_M"
BOT_TOKEN10 = "8814110908:AAHiUZdMW8ZsFCqez9amMMFTg4nBexqQHEI"

SUDO_USERS = list(map(lambda x: int(x), getenv("SUDO_USERS", default="6275672724").split()))
for x in ALTRON:
    SUDO_USERS.append(x)
OWNER_ID = int(getenv("OWNER_ID", default="6275672724"))
SUDO_USERS.append(OWNER_ID)

try:
    with open("sudo_users.txt", "r") as f:
        for user in f:
            user = user.strip()
            if user.isdigit():
                SUDO_USERS.append(int(user))
except FileNotFoundError:
    pass


# ------------- CLIENTS -------------

X1 = TelegramClient('X1', API_ID, API_HASH).start(bot_token=BOT_TOKEN)
X2 = TelegramClient('X2', API_ID, API_HASH).start(bot_token=BOT_TOKEN2)
X3 = TelegramClient('X3', API_ID, API_HASH).start(bot_token=BOT_TOKEN3)
X4 = TelegramClient('X4', API_ID, API_HASH).start(bot_token=BOT_TOKEN4)
X5 = TelegramClient('X5', API_ID, API_HASH).start(bot_token=BOT_TOKEN5)
X6 = TelegramClient('X6', API_ID, API_HASH).start(bot_token=BOT_TOKEN6)
X7 = TelegramClient('X7', API_ID, API_HASH).start(bot_token=BOT_TOKEN7)
X8 = TelegramClient('X8', API_ID, API_HASH).start(bot_token=BOT_TOKEN8)
X9 = TelegramClient('X9', API_ID, API_HASH).start(bot_token=BOT_TOKEN9)
X10 = TelegramClient('X10', API_ID, API_HASH).start(bot_token=BOT_TOKEN10)
