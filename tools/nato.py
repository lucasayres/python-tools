# -*- coding: utf-8 -*-
def nato(input_file):
    """Convert text to NATO phonetic alphabet.

    Args:
        input_file (str): Input file.

    Returns:
        str: Return NATO phonetic alphabet.

    """
    dictionary = {
        'a': 'Alpha', 'b': 'Bravo', 'c': 'Charlie', 'd': 'Delta', 'e': 'Echo',
        'f': 'Foxtrot', 'g': 'Golf', 'h': 'Hotel', 'i': 'India', 'j': 'Juliet',
        'k': 'Kilo', 'l': 'Lima', 'm': 'Mike', 'n': 'November', 'o': 'Oscar',
        'p': 'Papa', 'q': 'Quebec', 'r': 'Romeo', 's': 'Sierra', 't': 'Tango',
        'u': 'Uniform', 'v': 'Victor', 'w': 'Whiskey', 'x': 'X-ray',
        'y': 'Yankee', 'z': 'Zulu'
    }
    result = ''
    with open(input_file) as f:
        for char in f.read():
            if char.lower() in dictionary:
                result += dictionary[char.lower()] + ' '
            elif char == '\n' or char == '\t' or char == ' ':
                result += '(space) '
            else:
                result += char + ' '
    return result.rstrip()
