# -*- coding: utf-8 -*-
from gtts import gTTS


def text_to_speech_online(text, lang='en'):
    """Convert text to speech using Google Translate’s and save in mp3. Need an internet connection.

    Args:
        text (str): Text.
        lang (str): Language (Ex: pt-br).

    """
    tts = gTTS(text=text, lang=lang)
    tts.save("sound.mp3")
