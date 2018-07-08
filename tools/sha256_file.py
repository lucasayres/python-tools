# -*- coding: utf-8 -*-
import hashlib


def sha256_file(file):
    """Calculate SHA256 Hash of a file.

    Args:
        file (str): Input file.

    Retruns:
        str: Return the SHA256 Hash of a file.

    """
    sha256 = hashlib.sha256()
    with open(file, 'rb') as f:
        for block in iter(lambda: f.read(65536), b''):
            sha256.update(block)
    return sha256.hexdigest()
