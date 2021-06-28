#━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
#Copyright@2021 by TitanNetwork                                                                                                   │                                                                                                                       │
#━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
#This bot is owned by TitanNetwork                                                                                                │       
#━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
#We created this bot with our own skills, Yeah we kanged some things but We will give credits                                     │                                                                                   │
#━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━




from TITAN import bot
from sys import argv
import sys
from telethon.errors.rpcerrorlist import PhoneNumberInvalidError
import os
from telethon import TelegramClient
from var import Var
from .Config import Config
from .utils import load_module
from TITAN import LOAD_PLUG, LOGS, Titanversion
from pathlib import Path
import asyncio
import telethon.utils
os.system("pip install -U telethon")


async def add_bot(bot_token):
    await bot.start(bot_token)
    bot.me = await bot.get_me() 
    bot.uid = telethon.utils.get_peer_id(bot.me)


# beautification credits to @ranger_nex_op with the help of https://www.symbolsofit.com/en/line/ 
if len(argv) not in (1, 3, 4):
    bot.disconnect()
else:
    bot.tgbot = None
    if Var.TG_BOT_USER_NAME_BF_HER is not None:
        print("╠――Initiating Inline Bot――╣")
        # ForTheGreatrerGood of beautification
        bot.tgbot = TelegramClient(
            "TG_BOT_TOKEN",
            api_id=Var.APP_ID,
            api_hash=Var.API_HASH
        ).start(bot_token=Var.TG_BOT_TOKEN_BF_HER)
        print("╠――Initialisation finished with no errors――╣")
        print("Starting ⚜️ Tʜᴇ ᴛɪᴛᴀɴꜱ ᴜꜱᴇʀʙᴏᴛ ⚜️")
        bot.loop.run_until_complete(add_bot(Var.TG_BOT_USER_NAME_BF_HER))
        print("╋——Startup Completed——╋")
    else:
        bot.start()


import glob
path = 'userbot/plugins/*.py'
files = glob.glob(path)
for name in files:
    with open(name) as f:
        path1 = Path(f.name)
        shortname = path1.stem
        load_module(shortname.replace(".py", ""))

import userbot._core

print(f"""⚜️ Tʜᴇ ᴛɪᴛᴀɴꜱ ᴜꜱᴇʀʙᴏᴛ ⚜️ IS ON!!! ᴛɪᴛᴀɴꜱ ᴜꜱᴇʀʙᴏ VERSION :- {Titanversion}
JOIN OFFICIAL CHAT GROUP AND UPDATES CHANNEL
OFFICIAL CHANNEL :- @THETITANS_USERBOT
OFFICIAL GROUP :- @THETITANS_USERBOT_HELP
DO .alive OR .ping CHECK IF I'M ON!
IF YOU FACE ANY ISSUE THEN ASK AT CHAT GROUP.""")

if len(argv) not in (1, 3, 4):
    bot.disconnect()
else:
    bot.run_until_disconnected()
