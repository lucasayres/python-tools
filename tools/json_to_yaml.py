# -*- coding: utf-8 -*-
import json
import yaml


def json_to_yaml(json_file, yaml_file):
    """Convert JSON to YAML.

    Args:
        json_file (str): Input JSON file name.
        yaml_file (str): Output YAML file name.

    """
    with open(json_file) as f:
        with open(yaml_file, 'w') as f1:
            json_data = json.loads(f.read())
            converted_json_data = json.dumps(json_data)
            f1.write(yaml.dump(yaml.load(converted_json_data), default_flow_style=False))
