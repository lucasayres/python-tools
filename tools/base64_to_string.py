# -*- coding: utf-8 -*-
import base64


def base64_to_string(input, output):
    """Decode base64 file to plaintext.

    Args:
        input (str): Base64 file.
        output (str): Plaintext file.

    """
    with open(input) as f:
        with open(output, 'w') as f1:
            f1.write(base64.b64decode(f.read()).decode('utf-8'))
