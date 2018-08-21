# -*- coding: utf-8 -*-
def bytes_to_human(bytes):
    """Convert bytes to a human readable format.

    Args:
        bytes (int): Bytes.

    Returns:
        str: Return bytes into human readable format.

    """
    suffix = 'B'
    for unit in ['', 'K', 'M', 'G', 'T', 'P', 'E', 'Z']:
        if abs(bytes) < 1024.0:
            return '%3.1f%s%s' % (bytes, unit, suffix)
        bytes /= 1024.0
    return '%.1f%s%s' % (bytes, 'Y', suffix)
