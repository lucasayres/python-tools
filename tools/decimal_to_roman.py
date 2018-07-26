# -*- coding: utf-8 -*-
def decimal_to_roman(dec):
    """Convert decimal number to roman numerals.

    Args:
        dec (int): Decimal.

    Returns:
        str: Return roman numerals.

    """
    to_roman = [('M', 1000), ('CM', 900), ('D', 500),
                ('CD', 400), ('C', 100), ('XC', 90),
                ('L', 50), ('XL', 40), ('X', 10),
                ('IX', 9), ('V', 5), ('IV', 4),
                ('I', 1)]
    roman_numerals = []
    for numeral, value in to_roman:
        count = dec // value
        dec -= count * value
        roman_numerals.append(numeral * count)

    return ''.join(roman_numerals)
