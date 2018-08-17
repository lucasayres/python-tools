# -*- coding: utf-8 -*-
import requests


def send_message_telegram(msg, chat_id, token):
    """Send a message to a telegram user. The token can be generated talking with @BotFather on telegram.

    Args:
        msg (str): Message.
        chat_id (str): Number.
        token (str): Authentication Key.

    Returns:
        dict: Return message sending status.

    """
    response = requests.get('https://api.telegram.org/bot' + token + '/sendMessage?text=' + msg + '&chat_id=' + chat_id)
    content = response.content.decode('utf8')
    return content
