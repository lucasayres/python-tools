# -*- coding: utf-8 -*-
from dicttoxml import dicttoxml


def dict_to_xml(dict):
    """Convert dict to xml.

    Args:
        dict (dict): Dictionary.

    Returns:
        str: Return a XML representation of an dict.

    """
    return dicttoxml(dict).decode()
