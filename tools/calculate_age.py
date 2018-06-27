# -*- coding: utf-8 -*-
from datetime import date


def calculate_age(birth):
    """Calculate age from date of birth.

    Args:
        birth (date/datetime): Birthday.

    Returns:
        int: Return value in years.

    """
    today = date.today()
    return today.year - birth.year - ((today.month, today.day) < (birth.month, birth.day))
