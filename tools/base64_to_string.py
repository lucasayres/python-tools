# -*- coding: utf-8 -*-
import base64


def base64_to_string(input, output):
    """Decode base64 file to string.

    Args:
        input (str): Base64 file.
        output (str): Text file.

    """
    with open(input, 'rb') as f:
        with open(output, 'w') as f1:
            f1.write(base64.b64decode(f.read()).decode('utf-8'))
