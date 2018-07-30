# -*- coding: utf-8 -*-
def is_palindrome(string):
    """Check if string is a Palindrome.

    Args:
        string (str): String.

    Returns:
        bool: Return True if string is a palindrome and False if not.

    """
    string = string.strip()
    if string == string[::-1]:
        return True
    else:
        return False
