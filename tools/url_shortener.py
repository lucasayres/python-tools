# -*- coding: utf-8 -*-
import requests
from urllib import parse


def url_shortener(url):
    """Create a shortened URL with TinyURL.

    Args:
        url (str): URL.

    Returns:
        str: Return a shortened URL.

    """
    url = url.strip()
    if not parse.urlparse(url).scheme:
        url = 'http://' + url
    query_url = 'http://tinyurl.com/api-create.php?url={}'.format(url)
    return requests.get(query_url).text
