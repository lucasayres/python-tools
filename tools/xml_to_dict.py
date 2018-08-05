# -*- coding: utf-8 -*-
import json
import xmltodict


def xml_to_dict(xml):
    """Convert xml to dict.

    Args:
        xml (str): XML.

    Returns:
        dict: Return a dict representation of an XML.

    """
    try:
        my_dict = xmltodict.parse(xml)
    except Exception:
        my_dict = {}
    return json.loads(json.dumps(my_dict))
