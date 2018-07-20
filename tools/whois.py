# -*- coding: utf-8 -*-
import ipaddress
from warnings import filterwarnings
from ipwhois import IPWhois
from urllib import parse
from dns import resolver
filterwarnings(action='ignore')


def whois(url):
    """Get WHOIS from IP address or hostname.

    Args:
        url (str): IP address or hostname.

    Returns:
        dict: Return a JSON object with the WHOIS.

    """
    url = url.strip()
    if not parse.urlparse(url).scheme:
        url = 'http://' + url
    host = parse.urlparse(url).netloc
    try:
        ipaddress.ip_address(host)
        ip = host
    except Exception:
        try:
            ips = resolver.query(host, 'A')
            ip = ips[0]
        except Exception:
            return {}

    obj = IPWhois(ip)
    return obj.lookup_whois()
