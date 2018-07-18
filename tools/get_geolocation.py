# -*- coding: utf-8 -*-
import json
from urllib import parse
from urllib import request


def get_geolocation(url):
    """Get geolocation information from IP address or hostname (150 requests per minutes).

    Args:
        url (str): IP address or hostname.

    Returns:
        dict: Return a JSON object with the geolocation information.

    """
    url = url.strip()
    if not parse.urlparse(url).scheme:
        url = 'http://' + url
    parsed = parse.urlparse(url)
    resp = request.urlopen('http://ip-api.com/json/{}'.format(parsed.netloc))
    data = resp.read().decode('utf-8')
    return json.loads(data)
