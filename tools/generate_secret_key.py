# -*- coding: utf-8 -*-
import os
import binascii


def generate_secret_key():
    """Generate a flask secret key.

    Returns:
        str: Return a secret key.

    """
    return binascii.hexlify(os.urandom(24))
