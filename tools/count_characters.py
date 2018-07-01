# -*- coding: utf-8 -*-
def count_characters(file):
    """Count the number of characters in a text file.

    Args:
        file (str): Path of a fext file.

    Returns:
        int: Return number of characters in a text file.

    """
    with open(file) as f:
        lines = f.readlines()
    return len(''.join([l for l in lines]))
