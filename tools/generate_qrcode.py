# -*- coding: utf-8 -*-
import qrcode
import cv2
import numpy


def generate_qrcode(data):
    """Generate a QR Code.

    Args:
        data (str): Data.

    """
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=1,
    )
    qr.add_data(data.strip())
    qr.make(fit=True)
    img = qr.make_image(fill_color='black', back_color='white')
    imcv = numpy.asarray(img.convert('L'))
    cv2.imwrite('qrcode.png', imcv)
