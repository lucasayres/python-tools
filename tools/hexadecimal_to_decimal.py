# -*- coding: utf-8 -*-
def hexadecimal_to_decimal(hex):
    """Convert Hexadecimal to Decimal.

    Args:
        hex (str): Hexadecimal.

    Returns:
        int: Return decimal value.

    """
    return sum(['0123456789ABCDEF'.find(var) * 16 ** i for i, var in enumerate(reversed(hex.upper()))])
