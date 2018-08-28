# -*- coding: utf-8 -*-
import os
import shutil


def remove_file_dir(path):
    """Remove a file or directory.

    Args:
        path (str): Path of file or directory.

    """
    if os.path.isfile(path):
        os.remove(path)
    else:
        shutil.rmtree(path)
