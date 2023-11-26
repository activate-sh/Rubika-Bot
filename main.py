from pyrubi import Client
from random import randint
from requests import post, get
from json import dumps

groups = [
    'g0Dahu6056d578a540e1ba8ae673cee5',
]

token = '295809:6517005fc9455'
# personal token to perform translation operations
# to get your personal token, visit one-api.ir


def main():
    # client = Client(session='session')  # session for account
    client = Client(auth='tijmmwidcfuvswuqpgtdlfsaavhmrgla', private='MIICXAIBAAKBgQDciD0LhesW6K3d3ZjJJxJTrPkbLTUBPz6na84uzF+SOFZ19SNg\nuDDyDKo4fmig61eShW7v7vvEEfGGRy0yA9PFfXW1ckupUh35kynYI4BCJ929uysf\nsIdG+MbUijioKJ7n++mbGHjt7gRTzUPL2UfKXocD88/3MbR6JTWqMO34rQIDAQAB\nAoGALYFDL2SDvOdoMPavtxoD0xZHFI+Ad3Boaj15fviW4+ISHSbnFOcM2nU4jo2u\n4z2MhWRZHtMuSif1sWJwdfiKMrzvm7RJRPVOyWf54g1r6f6CSQkDIyVs/yYpOyTO\ndlGx3i5O0yzGfT4fLwGGeXVWEYDNro6Ps7Ndtt/F4dPuTTUCQQDk7xGCdgqKKBFf\nbUczx4MnZtCS6SmX8bbssVNGB7PQyqJWWd1kwCe0+W94D2s3kYfMRFxMIQfaSsO1\nA1K0pzyLAkEA9priVaAZNskpBnyZR3J8glfGa10ftskUyU7lp7yCYJJWuAmqIp/N\n6oKIFsfsefdnVlJ+OuI2mGnD0CRg4O2upwJAWdWqREx3xFEGyDCEkUAIKk0BKbUP\nGk3Cn0zSRZe+Kv9pBoOLCf8RVcXPxQgf5ZVY+YIVydXoU/OkqoJcUQGTEwJBAMuC\nXi5ThPtVXunfgY8Yx++5CCIqI7Xwk5rd5WBbjSytF6uhLiqMvp49QpmqO1kb9sei\nJFHrxSpafiITI2/8NhkCQEmA4EeDjtkunQllzCf0CX8/sZq1C3TFiCohx0mSORI1\nIgfFKsHP/Wg7td7wlyG0VpKuoWisO3DN2d7oaTa4PdI=')  # session for account
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
                        text=f'hello🖐🏻 welcome to {group_name} 💞💖',
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
