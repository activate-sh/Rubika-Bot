from pyrubi import Client
from rich.console import Console
from random import randint
from requests import get
from datetime import datetime
from os import system, uname

groups = [
    "g0DjNjc0eeaec8ae92ee9c9bfbdd3f95"
]

console = Console()

def clearPage():
    if uname()[0] == "Linux":
        system("clear")
    else:
        system("cls")


clearPage()

client = Client(session=".myAccount")  # session for account

with console.status(status=None, speed=1.0) as status:
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
                        text="**please wait...**",
                        message_id=message_id)

                    responce = get("https://pyrubi.b80.xyz/chat.php/?text=%s").json()
                    try:
                        client.send_text(
                            object_guid=update.object_guid,
                            text=responce[0]["text"],
                            message_id=message_id)
                    except TimeoutError:
                        client.send_text(
                            object_guid=update.object_guid,
                            text="**TimeoutError**",
                            message_id=message_id)


            elif update.text.startswith("/logo"):
                message_id = update.message_id
                if update.text == "/logo":
                    client.send_text(
                        object_guid=update.object_guid,
                        text="**please enter a text**",
                        message_id=message_id)
                else:
                    client.send_text(
                        object_guid=update.object_guid,
                        text="**please wait...**",
                        message_id=message_id)

                    url = "https://pyrubi.b80.xyz/Logo.php?style=%s&text=%s"
                    request = get(url % (randint(0, 9), update.text[6:])).json()
                    responce = get(request["result"][randint(0, len(request["result"]))])
                    with open(".img.png", "wb") as file:
                        file.write(responce.content)

                    try:
                        client.send_image(
                            object_guid=update.object_guid,
                            file=".img.png",
                            message_id=message_id,
                            text="your logo is ready👍\ncontent:\n\"%s\"\nprogrammer: @khode_linux" % update.text[6:])

                    except (TimeoutError, IndexError):
                        client.send_text(
                            object_guid=update.object_guid,
                            text="**a problem occurred!**",
                            message_id=message_id)


            elif update.text.startswith("/voice"):
                message_id = update.message_id
                if update.text == "/voice":
                    client.send_text(
                        object_guid=update.object_guid,
                        text="**please enter a text**",
                        message_id=message_id)
                else:
                    client.send_text(
                        object_guid=update.object_guid,
                        text="**please wait...**",
                        message_id=message_id)

                    url = "https://pyrubi.b80.xyz/voice.php?text=%s&mod=women"
                    request = get(url % update.text[7:]).json()
                    responce = get(request["result"]["url"])
                    with open(".voice.mp3", "wb") as file:
                        file.write(responce.content)

                    try:
                        client.send_voice(
                            object_guid=update.object_guid,
                            file=".voice.mp3",
                            message_id=message_id,
                            text="your voice is ready👍\ncontent:\n\"%s\"\nprogrammer: @khode_linux" % update.text[7:])

                    except TimeoutError:
                        client.send_text(
                            object_guid=update.object_guid,
                            text="**a problem occurred!**",
                            message_id=message_id)

            