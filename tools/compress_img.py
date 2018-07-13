# -*- coding: utf-8 -*-
from PIL import Image


def compress_img(path):
    """Compress image.

    Args:
        path (str): Path of a image file.

    """
    img = Image.open(path)
    w, h = img.size
    img = img.convert('RGB')
    img.save('compressed_' + path.rsplit('.', 1)[0] + '.jpg', format='JPEG', optimize=True, quality=95)
