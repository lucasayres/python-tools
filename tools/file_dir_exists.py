# -*- coding: utf-8 -*-
import os


def file_dir_exists(path):
    """Check if file or directory exists.

    Args:
        path (str): File name or Directory name.

    Returns:
        bool: Return True if exists and False if not.

    """
    return os.path.exists(path)
