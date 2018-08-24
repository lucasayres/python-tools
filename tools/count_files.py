# -*- coding: utf-8 -*-
import os


def count_files(path):
    """Count number of files in a diectory recursively.

    Args:
        path (str): Directory.

    Returns:
        int: Return number of files.

    """
    count = 0
    for root, dirs, files in os.walk(path):
        for f in files:
            count += 1
    return count
