# -*- coding: utf-8 -*-
import yaml


def yaml_to_json(yaml_file):
    """Convert YAML to JSON.

    Args:
        yaml_file (str): YAML file name.

    Returns:
        json: Return JSON object.

    """
    with open(yaml_file) as f:
        document = f.read()
    return yaml.load(document)
