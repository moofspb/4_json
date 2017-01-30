import os
import sys
import json


def load_data(filepath):
    if not os.path.exists(filepath):
        return None
    with open(filepath, 'r') as handler:
        return json.load(handler)


def pretty_print_json(data):
    return json.dumps(data, indent=4, sort_keys=True,
                      ensure_ascii=False)


if __name__ == '__main__':
    print(pretty_print_json(load_data(sys.argv[1])))
