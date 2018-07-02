# -*- coding: utf-8 -*-
import ipgetter


def my_ip():
    """Get your external IP.

    Returns:
        str: Return your external IP.

    """
    return ipgetter.IPgetter().get_externalip()
