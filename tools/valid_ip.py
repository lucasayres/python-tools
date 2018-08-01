# -*- coding: utf-8 -*-
import ipaddress


def valid_ip(ip):
    """Check if IP address is valid.

    Args:
        ip (str): IPv4 or IPv6.

    Returns:
        bool: Return True if in valid IP format (IPv4/IPv6) and False if not.

    """
    try:
        ipaddress.ip_address(ip)
        return True
    except Exception:
        return False
