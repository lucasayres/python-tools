# -*- coding: utf-8 -*-
from PIL import Image


def optimize_image(path):
    """Resize and compress image.

    Args:
        path (str): Path of a image file.

    """
    img = Image.open(path)
    w, h = img.size
    img = img.convert('RGB')
    img.thumbnail((int(w / 2), int(h / 2)), Image.ANTIALIAS)
    img.save('compressed_' + path.rsplit('.', 1)[0] + '.jpg', format='JPEG', optimize=True, progressive=True, quality=95)
