# -*- coding: utf-8 -*-
import re


def valid_email(email):
    """Check for a valid email address.

    Args:
        email (str): Email.

    Returns:
        bool: Return True if in valid email format and False if not.

    """
    return bool(re.match('^[a-zA-Z0-9.!#$%&’*+/=?^_`{|}~-]+@[a-zA-Z0-9-]+(?:\.[a-zA-Z0-9-]+)*$', email))
