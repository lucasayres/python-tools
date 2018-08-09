# -*- coding: utf-8 -*-
import os


def remove_pyc(path):
    """Remove all .pyc files in the path recursively.

    Args:
        path (str): Path.

    """
    for root, _, files in os.walk(path):
        for f in files:
            fullpath = os.path.join(root, f)
            if os.path.splitext(f)[1] == '.pyc':
                os.remove(fullpath)
