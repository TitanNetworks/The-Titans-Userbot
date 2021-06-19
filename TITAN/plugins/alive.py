#━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
#Copyright@2021 by TitanNetwork                                                                                                   │                                                                                                                │
#━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
#This bot is owned by TitanNetwork                                                                                                │            
#━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
#We created this bot with our own skills, Yeah we kanged some things but We will give credits                                     │                                      
#━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━



import time
from userbot import *
from TITAN.utils import *
from TITAN.cmdhelp import CmdHelp
from telethon import events, version
from telethon.events import NewMessage
from telethon.tl.custom import Dialog
from telethon.tl.types import Channel, Chat, User
from telethon import version
from TITAN import ALIVE_NAME, StartTime, Titanversion
from TITAN.utils import admin_cmd, edit_or_reply, sudo_cmd





async def reply_id(event):
    reply_to_id = None
    if event.sender_id in Config.SUDO_USERS:
        reply_to_id = event.id
    if event.reply_to_msg_id:
        reply_to_id = event.reply_to_msg_id
    return reply_to_id

ludosudo = Config.SUDO_USERS
if ludosudo:
    sudou = "True"
else:
    sudou = "False"

DEFAULTUSER = ALIVE_NAME or "Titan Master"
TITAN_IMG = Config.ALIVE_PIC
CUSTOM_ALIVE_TEXT = Config.ALIVE_MSG or "Lord ⚜️ Tʜᴇ ᴛɪᴛᴀɴꜱ ᴜꜱᴇʀʙᴏᴛ ⚜️"

USERID = bot.uid

mention = f"[{DEFAULTUSER}](tg://user?id={USERID})"


def get_readable_time(seconds: int) -> str:
    count = 0
    ping_time = ""
    time_list = []
    time_suffix_list = ["s", "m", "h", "days"]

    while count < 4:
        count += 1
        if count < 3:
            remainder, result = divmod(seconds, 60)
        else:
            remainder, result = divmod(seconds, 24)
        if seconds == 0 and remainder == 0:
            break
        time_list.append(int(result))
        seconds = int(remainder)

    for x in range(len(time_list)):
        time_list[x] = str(time_list[x]) + time_suffix_list[x]
    if len(time_list) == 4:
        ping_time += time_list.pop() + ", "

    time_list.reverse()
    ping_time += ":".join(time_list)

    return ping_time


uptime = get_readable_time((time.time() - StartTime))


@bot.on(admin_cmd(outgoing=True, pattern="alive$"))
@bot.on(sudo_cmd(pattern="alive$", allow_sudo=True))
async def amireallyalive(alive):
    if alive.fwd_from:
        return
    reply_to_id = await reply_id(alive)

    if Titan_IMG:
        Titan_caption = f"**{CUSTOM_ALIVE_TEXT}**\n\n"
        
        Titan_caption += f"     __**ㆆ⚜️ Tʜᴇ ᴛɪᴛᴀɴꜱ ᴜꜱᴇʀʙᴏᴛ ⚜️ㆆ**__\n"
        Titan_caption += f"**╔═══════════════════════╗**\n"
        Titan_caption += f"**╠══ `🔱─ᴛᴇʟᴇᴛʜᴏɴ─🔱 :** `{version.__version__}`\n"
        Titan_caption += f"**╠══ ℂ𝕦𝕣𝕣𝕖𝕟𝕥 𝕍𝕖𝕣𝕤𝕚𝕠𝕟 :**`{Titanversion}`\n"
        Titan_caption += f"**╠══ 𝕌𝕡𝕥𝕚𝕞𝕖 :** `{uptime}\n`"
        Titan_caption += f"**╠══ 𝕊𝕦𝕕𝕠       : `{sudou}`**\n"
        Titan_caption += f"**╠══ℂ𝕙𝕒𝕟𝕟𝕖𝕝   : [Join Here](https://t.me/THETITANS_USERBOT)**\n"
        Titan_caption += f"**╠══ ℂ𝕣𝕖𝕒𝕥𝕖𝕣    : [⋆✩ Pro ✩⋆ 🇮🇳](https://t.me/titan_devs)**\n"
        Titan_caption += f"**╠══ ᴍʏ ʟɪᴇɢᴇ:** {mention}\n"
        Titan_caption += f"**╚═══════════════════════╝**\n"
        Titan_caption += "[⌚Rests here⌚](https://github.com/TitanNetworks/The-Titans-Userbot/) 🔹 [✮ License ✮](https://github.com/TitanNetworks/The-Titans-Userbot/blob/master/LICENSE)"

        await alive.client.send_file(
            alive.chat_id, Titan_IMG, caption=Titan_caption, reply_to=reply_to_id
        )
        await alive.delete()
    else:
        await edit_or_reply(
            alive,
            f"**{CUSTOM_ALIVE_TEXT}**\n\n"
           f"     __**ㆆ⚜️ Tʜᴇ ᴛɪᴛᴀɴꜱ ᴜꜱᴇʀʙᴏᴛ ⚜️ㆆ**__\n"
            f"**╔═══════════════════════╗**\n"**\n"
            f"**╠══ `🔱─ᴛᴇʟᴇᴛʜᴏɴ─🔱 :** `{version.__version__}`\n"
            f"**╠══ ℂ𝕦𝕣𝕣𝕖𝕟𝕥 𝕍𝕖𝕣𝕤𝕚𝕠𝕟 :**`{Titanversion}`\n"
            f"**╠══ 𝕌𝕡𝕥𝕚𝕞𝕖 :** `{uptime}\n`"
            f"**╠══ 𝕊𝕦𝕕𝕠       : `{sudou}`**\n"
            f"**╠══ℂ𝕙𝕒𝕟𝕟𝕖𝕝   : [Join Here](https://t.me/THETITANS_USERBOT)**\n"
            f"**╠══ℂ𝕙𝕒𝕟𝕟𝕖𝕝   : [Join Here](https://t.me/THETITANS_USERBOT)**\n"
            f"**╠══ ᴍʏ ʟɪᴇɢᴇ:** {mention}\n"
            f"**┗━━━━━━━━━━━━━┛**\n"
            "[⌚Rests here⌚](https://github.com/TitanNetworks/The-Titans-Userbot/) 🔹 [✮ License ✮](https://github.com/TitanNetworks/The-Titans-Userbot/blob/master/LICENSE)",
        )

CmdHelp("alive").add_command(
  'alive', None, 'Check weather the bot is alive or not'
  ).add_info(
  'Zinda Hai Kya Bro?'
).add()


#thanks to @iisgaurav
