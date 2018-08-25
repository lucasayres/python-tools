# -*- coding: utf-8 -*-
import os


def count_directories(path):
    """Count number of folders in a diectory recursively.

    Args:
        path (str): Directory.

    Returns:
        int: Return number of folders.

    """
    count = 0
    for root, dirs, files in os.walk(path):
        for d in dirs:
            count += 1
    return count
