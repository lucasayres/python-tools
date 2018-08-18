# -*- coding: utf-8 -*-
import requests


def geocode_google(address):
    """Get latitude and longitude from address, using Google Maps Geocoding API.

    Args:
        address (str): Address.

    Returns:
        dict: Return a dictionary with lat, lng and address.

    """
    geodata = {}
    try:
        response = requests.get('https://maps.googleapis.com/maps/api/geocode/json?address=' + address).json()
    except Exception:
        return geodata
    if response['status'] == 'OK':
        geodata['lat'] = response['results'][0]['geometry']['location']['lat']
        geodata['lng'] = response['results'][0]['geometry']['location']['lng']
        geodata['address'] = response['results'][0]['formatted_address']
    return geodata
