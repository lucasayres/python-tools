# -*- coding: utf-8 -*-
import pyttsx3


def text_to_speech_offline(text, lang='english'):
    """Convert text to speech offline. It uses different speech engines based on your operating system.

    Args:
        text (str): Text.
        lang (str): Language (Ex: brazil).

    """
    engine = pyttsx3.init()
    rate = engine.getProperty('rate')
    engine.setProperty('rate', rate - 50)
    engine.setProperty('voice', lang)
    engine.say(text)
    engine.runAndWait()
