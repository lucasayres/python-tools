# -*- coding: utf-8 -*-
import os


def get_file_size(file):
    """Get file size.

    Args:
        file (str): Input file.

    Returns:
        int: Return size of the file in bytes.

    """
    return os.stat(file).st_size
