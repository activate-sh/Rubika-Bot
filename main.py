from pyrubi import Client
from random import randint
from requests import get
from datetime import datetime
from os import system, uname

groups = [
    "", # group one
    "", # group two
    # and...
]

token = "295809:6517005fc9455"
# personal token to perform translation operations
# to get your personal token, visit one-api.ir

def clearPage() -> None:
    if uname()[0] == "Linux":
        system("clear")
    else:
        system("cls")


clearPage()

def main():
    client = Client(session=".myAccount")  # session for account
    statrBot(client=client) # send message start bot
    for update in client.on_message(filters=["Channel", "User"]):
        if update.object_guid in groups:

            if update.text.startswith("+"):
                message_id = update.message_id
                if update.text == "+":
                    client.send_text(
                        object_guid=update.object_guid,
                        text="**please enter a text**",
                        message_id=message_id)
                else:
                    client.send_text(
                        object_guid=update.object_guid,
                        text="**please waith...**",
                        message_id=message_id
                    )
                    url = "https://pyrubi.b80.xyz/chat.php/?text=%s"
                    try:
                        responce = get(url % update.text[1:]).json()
                        client.send_text(
                            object_guid=update.object_guid,
                            text=responce[0]["text"],
                            message_id=message_id
                        )
                    except TimeoutError:
                        client.send_text(
                            object_guid=update.object_guid,
                            text="TimeoutError",
                            message_id=message_id
                        )


            elif update.text.startswith("-"):
                message_id = update.message_id
                message_id = update.message_id
                if update.text == "+":
                    client.send_text(
                        object_guid=update.object_guid,
                        text="**please enter a text**",
                        message_id=message_id)
                else:
                    client.send_text(
                        object_guid=update.object_guid,
                        text="**please waith...**",
                        message_id=message_id
                    )
                    url = "https://pyrubi.b80.xyz/chat2.php?text=%s"
                    responce = get(url % update.text[0:]).json()
                    try:
                        client.send_text(
                            object_guid=update.object_guid,
                            text=responce["result"],
                            message_id=message_id)
                    except TimeoutError:
                        client.send_text(
                            object_guid=update.object_guid,
                            text="**TimeoutError**",
                            message_id=message_id)


            elif update.text.startswith("logo"):
                message_id = update.message_id
                if update.text == "logo":
                    client.send_text(
                        object_guid=update.object_guid,
                        text="**please enter a text**",
                        message_id=message_id)
                else:
                    client.send_text(
                        object_guid=update.object_guid,
                        text="**please waith...**",
                        message_id=message_id
                    )
                    url = "https://pyrubi.b80.xyz/Logo.php?style=%s&text=%s"
                    try:
                        request = get(url % (randint(0, 9), update.text[3:])).json()
                        responce = get(request["result"][randint(0, len(request["result"]))])
                        with open(".img.png", "wb") as file:
                            file.write(responce.content)

                        client.send_image(
                            object_guid=update.object_guid,
                            file=".img.png",
                            message_id=message_id,
                            text="your logo is ready👍\ncontent:\"%s\"\nprogrammer: @khode_linux" % update.text[3:]
                        )
                    except TimeoutError:
                        client.send_text(
                            object_guid=update.object_guid,
                            text="TimeoutError",
                            message_id=message_id
                        )


            elif update.text.startswith("voice"):
                message_id = update.message_id
                if update.text == "voice":
                    client.send_text(
                        object_guid=update.object_guid,
                        text="**please enter a text**",
                        message_id=message_id)
                else:
                    client.send_text(
                        object_guid=update.object_guid,
                        text="**please waith...**",
                        message_id=message_id
                    )
                    url = "https://pyrubi.b80.xyz/voice.php?text=%s&mod=women"
                    try:
                        request = get(url % update.text[4:]).json()
                        responce = get(request["result"]["url"])
                        with open(".voice.mp3", "wb") as file:
                            file.write(responce.content)

                        client.send_voice(
                            object_guid=update.object_guid,
                            file=".voice.mp3",
                            message_id=message_id,
                            text="your voice is ready👍\ncontent:\"%s\"\nprogrammer: @khode_linux" % update.text[3:]
                        )
                    except TimeoutError:
                        client.send_text(
                            object_guid=update.object_guid,
                            text="TimeoutError",
                            message_id=message_id
                        )


            elif update.text.startswith("font"):
                message_id = update.message_id
                client.send_text(
                    object_guid=update.object_guid,
                    text="**please waith...**",
                    message_id=message_id
                )
                if update.text == "font":
                    client.send_text(
                        object_guid=update.object_guid,
                        text="**please enter a text**",
                        message_id=message_id
                    )
                else:
                    url = "http://api.codebazan.ir/font/?text=%s"
                    try:
                        responce = get(url % update.text[4:]).json()
                        client.send_text(
                            object_guid=update.object_guid,
                            text=responce["result"][str(randint(0, 138))],
                            message_id=message_id
                        )
                    except KeyError:
                        url = "https://api.codebazan.ir/font/?type=fa&text=%s"

                        responce = get(url % update.text[4:]).json()
                        client.send_text(
                            object_guid=update.object_guid,
                            text=responce["Result"][str(randint(0, 10))],
                            message_id=message_id
                        )
                    except TimeoutError:
                        client.send_text(
                            object_guid=update.object_guid,
                            text="**TimeoutError**",
                            message_id=message_id
                        )


            elif update.text.startswith("*"):
                message_id = update.message_id
                client.send_text(
                    object_guid=update.object_guid,
                    text="**please waith...**",
                    message_id=message_id
                )
                url = "https://one-api.ir/translate/?token=%s&action=google&lang=%s&q=%s"
                try:
                    responce = get(url % (token, update.text[1:3], update.text[4:])).json()
                    client.send_text(
                        object_guid=update.object_guid,
                        text="**your text has been translated:**\n\n``%s``" % responce["result"],
                        message_id=message_id
                    )
                except TimeoutError:
                    client.send_text(
                        object_guid=update.object_guid,
                        text="**TimeoutError**",
                        message_id=message_id
                    )


            elif update.text == "test":
                message_id = update.message_id
                client.send_text(
                    object_guid=update.object_guid,
                    text="**the bot is active ✅**",
                    message_id=message_id
                )


            elif update.text == "time":
                message_id = update.message_id
                request = get("https://pyrubi.b80.xyz/time.php").json()
                client.send_text(
                    object_guid=update.object_guid,
                    text=request["result"],
                    message_id=message_id)


            elif update.text == "link":
                message_id = update.message_id
                client.send_text(
                    object_guid=update.object_guid,
                    text="``%s``" % client.get_link(update.object_guid)["join_link"],
                    message_id=message_id
                )


            elif update.text == "?":
                message_id = update.message_id
                client.send_text(
                    object_guid=update.object_guid,
                    text="""
✨ Robot commands for regular users ✨

💬 ChatGPT 3.5
- Example: ``+hello``

❗💬 BratGpt
- Example: ``-hello``


🖼💭 Logo generation: 
- Example: ``logo text``

🔊📢 Voice generation: 
- Example: ``voice hi``

🌐🗣 Translate Persian to English: 
- Example: ``*en persian text``

🌐🗣 Translate English to Persian: 
- Example: ``*fa english text``

⌚️ Time: 
- Example: ``time``

🎨🔠 Font generation: 
- Example: ``font english text or persian text``""",
                    message_id=message_id
                )


            elif update.event_type == "JoinedGroupByLink" or update.event_type == "AddedGroupMembers":
                message_id = update.message_id
                results = client.get_chat_info(update.object_guid)
                group_name = results["group"]["group_title"]
                client.send_text(
                    object_guid=update.object_guid,
                    text="hello🖐🏻 welcome to %s group 💞💖" % group_name,
                    message_id=message_id
                )


            elif update.event_type == "LeaveGroup":
                client.send_text(
                    object_guid=update.object_guid,
                    text="by 👋🏻👋🏻👋🏻",
                    message_id=message_id
                )


if __name__ == "__main__":
    main()
