# -*- coding: utf-8 -*-
import string
import random


def generate_password(length=8):
    """Generate a random password.

    Args:
        length (int): Password length.

    Returns:
        str: Return a random password.

    """
    alphabet = string.ascii_letters + string.digits
    return ''.join(random.choice(alphabet) for _ in range(length))
