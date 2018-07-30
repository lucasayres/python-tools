# -*- coding: utf-8 -*-
def is_prime(number):
    """Check if a number is a prime number.

    Args:
        number (int): Number.

    Returns:
        bool: Return True if number is a prime number and False if not.

    """
    if number <= 1:
        return False
    for x in range(2, number):
        if not number % x:
            return False
    return True
