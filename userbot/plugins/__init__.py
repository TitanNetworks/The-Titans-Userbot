#━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
#Copyright@2021 by TitanNetwork                                                                                                   │                                                                                                                │
#━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
#This bot is owned by TitanNetwork                                                                                                │            
#━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
#We created this bot with our own skills, Yeah we kanged some things but We will give credits                                     │                                      
#━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━



from userbot import *
from userbot.Config import Config
from userbot.helpers.functions import *
from userbot.cmdhelp import CmdHelp
from TitanBot.utils import *
from telethon import events, version
from telethon.events import NewMessage
from telethon.tl.custom import Dialog
from telethon.tl.types import Channel, Chat, User



# =================== CONSTANT ===================

USERID = bot.uid
DEFAULTUSER = str(ALIVE_NAME) if ALIVE_NAME else "Titan Master"
# mention user
mention = f"[{DEFAULTUSER}](tg://user?id={USERID})"
hmention = f"<a href = tg://user?id={USERID}>{DEFAULTUSER}</a>"
