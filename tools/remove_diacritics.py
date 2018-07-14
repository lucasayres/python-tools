# -*- coding: utf-8 -*-
import unicodedata


def remove_diacritics(text):
    """Remove diacritics from the text.

    Args:
        text (str): Text.

    Returns:
        str: Return text without diacritics.

    """
    text = unicodedata.normalize('NFD', text)
    shaved = unicodedata.normalize('NFC', ''.join(c for c in text if not unicodedata.combining(c)))
    return unicodedata.normalize('NFC', shaved)
