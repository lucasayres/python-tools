# -*- coding: utf-8 -*-
import hashlib


def md5_file(file):
    """Calculate MD5 Hash of a file.

    Args:
        file (str): Input file.

    Retruns:
        str: Return the MD5 Hash of a file.

    """
    md5 = hashlib.md5()
    with open(file, 'rb') as f:
        for block in iter(lambda: f.read(65536), b''):
            md5.update(block)
    return md5.hexdigest()
