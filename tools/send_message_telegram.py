# -*- coding: utf-8 -*-
import telegram


def send_message_telegram(msg, chat_id, token):
    """Send a message to a telegram user. The token can be generated talking with @BotFather on telegram.

    Args:
        msg (str): Message.
        chat_id (int): Number.
        token (str): Authentication Key.

    """
    bot = telegram.Bot(token=token)
    bot.sendMessage(chat_id=chat_id, text=msg)
