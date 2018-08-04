# -*- coding: utf-8 -*-
import json
from sqlalchemy import inspect
from datetime import datetime


def sqlalchemy_to_dict(obj):
    """Convert SQLAlchemy object to dict.

    Args:
        query (class): SQLAlchemy Object.

    Returns:
        dict: Return a dict representation of an SQLAlchemy object.

    """
    fields = {}
    for field in [c.key for c in inspect(obj).mapper.column_attrs]:
        data = obj.__getattribute__(field)
        try:
            if isinstance(data, datetime):
                data = data.strftime('%Y-%m-%d %H:%M:%S')
            json.dumps(data)
            fields[field] = data
        except TypeError:
            fields[field] = None
    return fields
