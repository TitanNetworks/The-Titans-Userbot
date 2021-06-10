#Copyright@2021 by TitanNetwork
# ASCII text can be added if imported random, but I don't want to waste much time on this.


from telethon.sessions import StringSession
from telethon.sync import TelegramClient

print("")
print("""Welcome To ⚜️ Tʜᴇ ᴛɪᴛᴀɴꜱ ᴜꜱᴇʀʙᴏᴛ ⚜️\nGenerator By @THETITANS_USERBOT\n\n""")
print("""Enter Your Valid Details To Continue!\n\n """)

API_KEY = input("API_ID:  ")
API_HASH = input("API_HASH:  ")

while True:
    try:
        with TelegramClient(StringSession(), API_KEY, API_HASH) as client:
            print(
                "String Session Sucessfully Sent To Your Saved Message, Store It To A Safe Place!!\n\n "
            )
            print("")
            session = client.session.save()
            client.send_message(
                "me",
                f"Here is your TELEGRAM STRING SESSION\n(Tap to copy it and paste in heroku deploy page)👇 \n\n `{session}` \n\n If you face any problem,head to @THETITANS_USERBOT!\n\n",
            )

            print(
                "⚜️ Tʜᴇ ᴛɪᴛᴀɴꜱ ᴜꜱᴇʀʙᴏᴛ ⚜️ thanks you for showing your trust in us..... please do terminate the old session if you come back to generate new one"
            )
    except:
        print("")
        print(
            "I think you have entered wrong number \n make sure its with correct country code. Example : +916262889xxx Kindly Retry"
        )
        print("")
        continue
    break
