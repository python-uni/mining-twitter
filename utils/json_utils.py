import json


def pretty_json(json_content):
    print json.dumps(
        json_content,
        sort_keys=True,
        indent=4,
        separators=(',', ': ')
    )
