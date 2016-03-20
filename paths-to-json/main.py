#!/usr/local/bin/python

import sys
import json
from pprint import pprint


def read_paths(path_to_file):
    with open(path_to_file) as f:
        _path_list = [l.strip() for l in f.readlines()]

    return _path_list


def path_list_to_dict(path_list):
    d = {}
    for path in path_list:
        current_level = d
        for part in filter(None, path.split("/")):
            if part not in current_level:
                current_level[part] = {}
            current_level = current_level[part]
    return d


def dict_to_json(dict_obj, json_path):
    json_string = json.dumps(dict_obj)
    with open(json_path, 'w+') as f:
        f.write(json_string)


def usage():
    print("Usage: ./main <path_to_paths_file> [path_to_output_json_file]")


if __name__ == '__main__':
    try:
        assert len(sys.argv) > 1
        paths_file = sys.argv[1]
        try:
            json_output_path = sys.argv[2]
        except IndexError:
            json_output_path = None

    except AssertionError:
        usage()
        sys.exit()

    path_dict = path_list_to_dict(read_paths(sys.argv[1]))

    if json_output_path:
        dict_to_json(path_dict, json_output_path)
    else:
        pprint(path_dict)

