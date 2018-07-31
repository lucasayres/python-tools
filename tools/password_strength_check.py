# -*- coding: utf-8 -*-
import re


def password_strength_check(password):
    """Check the strength of password.

    Args:
        password (str): Password.

    returns:
        dict: Return a dictionary indicating whether the password is strong.

    """
    status = False
    length = len(password) >= 8
    digit = re.search(r'\d', password) is not None
    uppercase = re.search(r'[A-Z]', password) is not None
    lowercase = re.search(r'[a-z]', password) is not None
    symbol = re.search(r'[\W_]', password) is not None
    if not length:
        message = 'Password must have 8 characters length or more'
    elif not digit:
        message = 'Password must have 1 digit or more'
    elif not uppercase:
        message = 'Password must have 1 uppercase letter or more'
    elif not lowercase:
        message = 'Password must have 1 lowercase letter or more'
    elif not symbol:
        message = 'Password must have 1 symbol or more'
    else:
        status = True
        message = 'Success'

    return {'status': status, 'message': message}
