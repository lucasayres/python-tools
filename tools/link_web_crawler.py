# -*- coding: utf-8 -*-
import re
from urllib.request import urlopen
from urllib import parse


def link_web_crawler(urls):
    """Web crawler for grabbing all links from a website.

    Args:
        urls (list): List of URLs.

    Returns:
        list: Return list of links.

    """
    list_links = []
    for url in urls:
        if not parse.urlparse(url.strip()).scheme:
            url = 'http://' + url.strip()
        try:
            response = urlopen(url.strip(), timeout=5)
            html = response.read().decode('utf-8')
            for link in re.findall(r'href\s?=\s?[\'"]?([^\'" >]+)', html):
                if link not in list_links:
                    list_links.append(link)
        except Exception:
            pass
    return list_links
