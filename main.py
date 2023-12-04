from pyrubi import Client
from random import randint
from requests import post, get
from json import dumps

groups = ['g0Dahu6056d578a540e1ba8ae673cee5']

token = '295809:6517005fc9455'
# personal token to perform translation operations
# to get your personal token, visit one-api.ir


def main():
    # client = Client(session='session')  # session for account
    client = Client(auth='mbezkzljpbrkzaxvdwcvnyuirelpqkzy', private='MIICXAIBAAKBgQCtPdKJzZQogEz4AKwVGXeap1xl7sb4NSkj50BkQQYkrLCY9B1B\n2pOjb+mzbe0XkVvesHnqZFS4dhhJKxXWZlCNfStVu8RvPhmuwGrfdmcQ415/oVP9\nnhONUeCdsEZeKwG3HL1MyEzcSH6390IY8J1hQRQDKEqHU5BnvhMdQq+WAQIDAQAB\nAoGAFITTRDeZcf+aPjCEMT6SNDrY3ojcv6a6P/KipY0vD1Z11zPoqDVdkbjOXw5o\ny8cPcM2JrxmhkDSKlVX5UOrO5PUGZ4DaTaPWXVPGfho0HbRVPZj/t/dKFv+kLBEQ\nnmWU9aSKlXDe6x5oJJ3aZG/z3qOF5vkQr0kqKTuLE3Vf4s0CQQC8A7oNWaT104gS\nt51M5iy7+y0CQIzcAzUEB+WSZsSmKILSRxzeAOyvqOYQvr+hbVBtWtr0Zs/kbn7G\nEEZhQsSdAkEA6+KSUJIA94v5C7++1kd3tWkUftPSrQES6h4FJGfXg9Sv036wOdU1\nMvesWkoeZ1gEpPj7Yj8CrMx+sRwxWtzvtQJAUh7Kl+Qs0haXm51JfnoW1fCKoy4w\nmDRqZp1QX5a1k+Gj6laXPDxpJPx/qJa4Orj1ZR5G/nMdoKfGhZo8M2UnXQJAV+tU\nE7nHqHzAb7OhQqbSpIgs/nSfQqJy1VYpHn+h4V4lxtOihXvFX2DXGbQkjupMmNzA\nfcb0jUmPMx5J+w78PQJBAIXWU4RVy17AD3nlWRdBsb5D0nDs7lCoa2iut8fQsh1i\nAkPQfgNfhG2s7oydW+OY3fAZ/oIlm3b396JnUPTPrH4=')
    for guid in groups:
        group_name = client.get_chat_info(object_guid=guid)
        group_name = group_name['group']['group_title']
        client.send_text(
            object_guid=guid,
            text=f'The bot was successfully activated in chat {group_name}'
        )
    for update in client.on_message(filters=['Channel', 'User']):
        if update.object_guid in groups:
            try:
                if update.text.startswith('+'):
                    message_id = update.message_id
                    try:
                        if update.text == '+':
                            client.send_text(
                                object_guid=update.object_guid,
                                text='please enter a text',
                                message_id=message_id)
                        else:
                            client.send_text(
                                object_guid=update.object_guid,
                                text='please wait...',
                                message_id=message_id
                            )
                            url = 'https://chatgpt-api3.onrender.com'
                            headers = {
                                'Content-Type': 'application/json; charset=utf-8'
                            }
                            data = {
                                'text': update.text[1:]
                            }
                            responce = post(url, headers=headers, data=dumps(data)).json()
                            client.send_text(
                                object_guid=update.object_guid,
                                text=responce['message'],
                                message_id=message_id
                            )
                    except TimeoutError:
                        client.send_text(
                            object_guid=update.object_guid,
                            text='TimeoutError',
                            message_id=message_id
                        )


                elif update.text.startswith('logo'):
                    message_id = update.message_id
                    try:
                        if update.text == 'logo':
                            client.send_text(
                                object_guid=update.object_guid,
                                text='please enter a text',
                                message_id=message_id)
                        else:
                            client.send_text(
                                object_guid=update.object_guid,
                                text='please wait...',
                                message_id=message_id
                            )
                            request = post('https://pyrubi.b80.xyz'
                                   f'/Logo.php?style={randint(0, 9)}&text={update.text[5:]}').json()
                            try:
                                responce = get(request['result'][randint(0, len(request['result']))])
                            except IndexError:
                                client.send_text(
                                    object_guid=update.object_guid,
                                    text='IndexError',
                                    message_id=message_id
                                )
                            with open('.img.png', 'wb') as file:
                                file.write(responce.content)

                            client.send_image(
                                object_guid=update.object_guid,
                                file='.img.png',
                                message_id=message_id,
                                text='your logo is ready👍'
                                     f'\ncontent:\"{update.text[5:]}\"\nprogrammer: @activate_sh'
                            )
                    except TimeoutError:
                        client.send_text(
                            object_guid=update.object_guid,
                            text='TimeoutError',
                            message_id=message_id
                        )


                elif update.text.startswith('img'):
                    message_id = update.message_id
                    try:
                        if update.text == 'img':
                            client.send_text(
                                object_guid=update.object_guid,
                                text='please enter a text',
                                message_id=message_id
                            )
                        else:
                            client.send_text(
                                object_guid=update.object_guid,
                                text='please wait...',
                                message_id=message_id
                            )
                            request = get(f'https://haji-api.ir/prompts/?text={update.text[4:]}').json()
                            responce = get(request['result'][randint(0, 19)])
                            with open('.img.png', 'wb') as file:
                                file.write(responce.content)

                            client.send_image(
                                object_guid=update.object_guid,
                                file='.img.png',
                                message_id=message_id,
                                text='your image is ready👍'
                                     f'\ncontent:\"{update.text[4:]}\"\nprogrammer: @activate_sh'
                            )
                    except TimeoutError:
                        client.send_text(
                            object_guid=update.object_guid,
                            text='TimeoutError',
                            message_id=message_id
                        )
                    except UnboundLocalError:
                        client.send_text(
                            object_guid=update.object_guid,
                            text='Please enter Persian text',
                            message_id=message_id
                        )


                elif update.text.startswith('voice'):
                    message_id = update.message_id
                    try:
                        client.send_text(
                            object_guid=update.object_guid,
                            text='please wait...',
                            message_id=message_id
                        )
                        if update.text[6:9] == 'man':
                            voice_mod = 'man'
                            message = update.text.split('man')[-1].strip()
                        else:
                            voice_mod = 'women'
                            message = update.text.split('woman')[-1].strip()

                        request = post('https://pyrubi.b80.xyz/'
                                       f'voice.php?text={message}&mod={voice_mod}').json()

                        responce = post(request['result']['url'])
                        with open('.voice.mp3', 'wb') as file:
                            file.write(responce.content)

                        client.send_voice(
                            object_guid=update.object_guid,
                            file='.voice.mp3',
                            message_id=message_id,
                            text='your voice is ready👍'
                                 f'\ncontent:\"{message}\"\nprogrammer: @activate_sh'
                        )
                    except TimeoutError:
                        client.send_text(
                            object_guid=update.object_guid,
                            text='TimeoutError',
                            message_id=message_id
                        )
                    except:
                        client.send_text(
                            object_guid=update.object_guid,
                            text='The information entered is not correct\n'
                                 'Send ``?`` to display commands',
                            message_id=message_id
                        )


                elif update.text.startswith('font'):
                    message_id = update.message_id
                    try:
                        client.send_text(
                            object_guid=update.object_guid,
                            text='please wait...',
                            message_id=message_id
                        )
                        if update.text == 'font':
                            client.send_text(
                                object_guid=update.object_guid,
                                text='please enter a text',
                                message_id=message_id
                            )
                        else:
                            responce = post(
                                f'http://api.codebazan.ir/font/?text={update.text[5:]}').json()

                            client.send_text(
                                object_guid=update.object_guid,
                                text=responce['result'][str(randint(0, 138))],
                                message_id=message_id
                            )
                    except KeyError:
                        responce = post(f'https://api.codebazan.ir/font'
                                        f'/?type=fa&text={update.text[5:]}').json()

                        client.send_text(
                            object_guid=update.object_guid,
                            text=responce['Result'][str(randint(0, 10))],
                            message_id=message_id
                        )
                    except TimeoutError:
                        client.send_text(
                            object_guid=update.object_guid,
                            text='TimeoutError',
                            message_id=message_id
                        )


                elif update.text.startswith('-'):
                    message_id = update.message_id
                    try:
                        if update.text == '-':
                            client.send_text(
                                object_guid=update.object_guid,
                                text='please enter a text',
                                message_id=message_id
                            )
                        else:
                            client.send_text(
                                object_guid=update.object_guid,
                                text='please wait...',
                                message_id=message_id
                            )
                            responce = post('https://one-api.ir/translate'
                                   f'/?token={token}&'
                                   f'action=google&lang={update.text[1:3]}&q={update.text[4:]}').json()

                            responce = responce['result']
                            client.send_text(
                                object_guid=update.object_guid,
                                text=f'your text has been translated:\n\n``{responce}``',
                                message_id=message_id
                            )
                    except TimeoutError:
                        client.send_text(
                            object_guid=update.object_guid,
                            text='TimeoutError',
                            message_id=message_id
                        )


                elif update.text == 'test':
                    message_id = update.message_id
                    try:
                        client.send_text(
                            object_guid=update.object_guid,
                            text='The bot is active ✅',
                            message_id=message_id
                        )
                    except TimeoutError:
                        client.send_text(
                            object_guid=update.object_guid,
                            text='TimeoutError',
                            message_id=message_id
                        )


                elif update.text == 'time':
                    message_id = update.message_id
                    try:
                        request = post('https://pyrubi.b80.xyz/time.php').json()
                        client.send_text(
                            object_guid=update.object_guid,
                            text=request['result'],
                            message_id=message_id
                        )
                    except TimeoutError:
                        client.send_text(
                            object_guid=update.object_guid,
                            text='TimeoutError',
                            message_id=message_id
                        )


                elif update.text == 'link':
                    message_id = update.message_id
                    grups_link = client.get_link(update.object_guid)['join_link']
                    client.send_text(
                        object_guid=update.object_guid,
                        text=f'``{grups_link}``',
                        message_id=message_id
                    )


                elif update.text == '?' or update.text == 'info' or update.text == 'help':
                    message_id = update.message_id
                    try:
                        client.send_text(
                            object_guid=update.object_guid,
                            text='''
✨ Robot commands for regular users ✨

💬 ChatGPT 3.5
- Example: ``+hello``

🖼💭 Image generation: 
- Example: ``img text``

🖼💭 Logo generation: 
- Example: ``logo text``

🔊📢 Voice generation: 
- Example: ``voice man hi``
- Example: ``voice woman hi``

🌐🗣 Translate Persian to English: 
- Example: ``-en text``

🌐🗣 Translate English to Persian: 
- Example: ``-fa text``

⌚️ Time: 
- Example: ``time``

🎨🔠 Font generation: 
- Example: ``font text``    ''',
                            message_id=message_id
                            )
                    except TimeoutError:
                        client.send_text(
                            object_guid=update.object_guid,
                            text='TimeoutError',
                            message_id=message_id
                        )


                elif (
                        update.event_type == 'JoinedGroupByLink' or
                        update.event_type == 'AddedGroupMembers'
                ):
                    message_id = update.message_id
                    results = client.get_chat_info(object_guid=update.object_guid)
                    group_name = results['group']['group_title']
                    client.send_text(
                        object_guid=update.object_guid,
                        text=f'hello🖐🏻 welcome to {group_name}',
                        message_id=message_id
                    )


                elif update.event_type == 'LeaveGroup':
                    message_id = update.message_id
                    client.send_text(
                        object_guid=update.object_guid,
                        text='by 👋🏻👋🏻👋🏻',
                        message_id=message_id
                    )

            except:
                pass


if __name__ == '__main__':
    main()
