# -*- coding: utf-8 -*-
def count_vowels(text):
    """Count the number of vowels in a text.

    Args:
        text (str): Text.

    Returns:
        int: Return number of vowels in a text.

    """
    vowels = ['a', 'e', 'i', 'o', 'u']
    count = 0
    for i in vowels:
        count += text.lower().count(i)
    return count
