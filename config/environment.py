import json


def get_config():
    with open('resources/config.json') as json_file:
        return json.load(json_file)
