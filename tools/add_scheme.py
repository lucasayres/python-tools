# -*- coding: utf-8 -*-
from urllib import parse


def add_scheme(url):
    """Add scheme to URL if not present.

    Args:
        url (str): URL.

    Returns:
        str: Return URL with scheme.

    """
    url = url.strip()
    if not parse.urlparse(url).scheme:
        url = 'http://' + url
    return url
