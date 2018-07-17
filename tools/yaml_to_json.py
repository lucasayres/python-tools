# -*- coding: utf-8 -*-
import json
import yaml


def yaml_to_json(yaml_file, json_file):
    """Convert YAML to JSON.

    Args:
        yaml_file (str): Input YAML file name.
        json_file (str): Output JSON file name.

    """
    with open(yaml_file) as f:
        with open(json_file, 'w') as f1:
            f1.write(json.dumps(yaml.load(f.read()), ensure_ascii=False))
