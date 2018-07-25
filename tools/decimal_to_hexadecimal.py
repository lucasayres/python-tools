# -*- coding: utf-8 -*-
def decimal_to_hexadecimal(dec):
    """Convert Decimal to Hexadecimal.

    Args:
        dec (int): Decimal.

    Returns:
        str: Return hexadecimal value.

    """
    return format(dec, '02x').upper()
