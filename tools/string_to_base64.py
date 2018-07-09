# -*- coding: utf-8 -*-
import base64


def string_to_base64(input, output):
    """Encode a text file to base64.

    Args:
        input (str): Text file.
        output (str): Base64 file.

    """
    with open(input, 'rb') as f:
        with open(output, 'w') as f1:
            f1.write(base64.b64encode(f.read()).decode('utf-8'))
