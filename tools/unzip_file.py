# -*- coding: utf-8 -*-
import zipfile


def unzip_file(input, output):
    """Unzip file.

    Args:
        input (str): Zip file.
        output (str): Target directory.

    """
    with zipfile.ZipFile(input, 'r') as zip:
        zip.extractall(output)
