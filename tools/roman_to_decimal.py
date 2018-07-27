# -*- coding: utf-8 -*-
def roman_to_decimal(roman):
    """Convert roman numerals to decimal number.

    Args:
        roman (str): Roman numerals.

    Returns:
        int: Return decimal number.

    """
    roman = roman.strip().upper()
    rom_val = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    int_val = 0
    for i in range(len(roman)):
        if i > 0 and rom_val[roman[i]] > rom_val[roman[i - 1]]:
            int_val += rom_val[roman[i]] - 2 * rom_val[roman[i - 1]]
        else:
            int_val += rom_val[roman[i]]
    return int_val
