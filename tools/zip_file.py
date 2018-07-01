# -*- coding: utf-8 -*-
import os
import zipfile


def zip_file(directory, output):
    """Create a zip file.

    Args:
        directory (str): Directory to be compressed.
        output (str): Output file .zip.

    """
    relroot = os.path.abspath(os.path.join(directory, os.pardir))
    with zipfile.ZipFile(output, "w", zipfile.ZIP_DEFLATED) as zip:
        for root, dirs, files in os.walk(directory):
            zip.write(root, os.path.relpath(root, relroot))
            for file in files:
                filename = os.path.join(root, file)
                if os.path.isfile(filename):
                    arcname = os.path.join(os.path.relpath(root, relroot), file)
                    zip.write(filename, arcname)
