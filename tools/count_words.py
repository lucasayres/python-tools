# -*- coding: utf-8 -*-
import string


def count_words(text):
    """Count the occurrences of each word in a given sentence.

    Args:
        text (str): Text.

    Returns:
        dict: Return a dictionary with the occurrences of each word.

    """
    output = []
    for char in text:
        if char not in string.punctuation:
            output.append(char)

    output = (''.join(output)).split()

    my_dict = {}
    for word in output:
        my_dict.update({word: output.count(word)})

    return my_dict
