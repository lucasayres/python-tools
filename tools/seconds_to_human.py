# -*- coding: utf-8 -*-
def seconds_to_human(seconds):
    """Convert seconds to a human readable format.

    Args:
        seconds (int): Seconds.

    Returns:
        str: Return seconds into human readable format.

    """
    units = (
        ('week', 60 * 60 * 24 * 7),
        ('day', 60 * 60 * 24),
        ('hour', 60 * 60),
        ('min', 60),
        ('sec', 1)
    )
    if seconds == 0:
        return '0 secs'
    parts = []
    for unit, div in units:
        amount, seconds = divmod(int(seconds), div)
        if amount > 0:
            parts.append('{} {}{}'.format(
                amount, unit, '' if amount == 1 else 's'))
    return ' '.join(parts)
