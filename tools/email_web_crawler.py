# -*- coding: utf-8 -*-
import re
from urllib.request import urlopen
from urllib import parse


def email_web_crawler(urls):
    """Web crawler for grabbing emails from a website.

    Args:
        urls (list): List of URLs.

    Returns:
        list: Return list of emails.

    """
    list_emails = []
    for url in urls:
        if not parse.urlparse(url.strip()).scheme:
            url = 'http://' + url.strip()
        try:
            response = urlopen(url.strip(), timeout=5)
            html = response.read().decode('utf-8')
            for email in re.findall('([\w\.,]+@[\w\.,]+\.\w+)', html):
                if email not in list_emails:
                    list_emails.append(email)
        except Exception:
            pass
    return list_emails
