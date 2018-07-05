# -*- coding: utf-8 -*-
import functools
import os


def get_directory_structure(root_dir):
    """Create a dictionary that represents the folder structure of directory.

    Args:
        root_dir (str): Root directory.

    Returns:
        dict: Return directory structure in nested dictionary.

    """
    dict = {}
    root_dir = root_dir.rstrip(os.sep)
    start = root_dir.rfind(os.sep) + 1
    for path, dirs, files in os.walk(root_dir):
        folders = path[start:].split(os.sep)
        subdir = dict.fromkeys(files)
        parent = functools.reduce(dict.get, folders[:-1], dict)
        parent[folders[-1]] = subdir
    return dict
