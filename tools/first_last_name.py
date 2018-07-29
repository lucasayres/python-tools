# -*- coding: utf-8 -*-
def first_last_name(name):
    """Extract the first and last name from a full name.

    Args:
        name (str): Full name.

    Returns:
        str: Return 'first_name last_name'.

    """
    name = name.strip().split()
    first_last = ''
    if len(name):
        first = name[0]
        last = ' '.join(name[-1:])
        if last == first or last == '':
            first_last = first
        else:
            first_last = first + ' ' + last

    return first_last
