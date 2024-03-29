#!/usr/bin/python3
"""
  Load Add Save Module
"""
import sys
import os
import json
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file


if not os.path.exists("add_item.json"):
    with open('add_item.json', 'w') as f:
        json.dump([], f)
ancien = load_from_json_file('add_item.json')
args = []
for i in range(1, len(sys.argv)):
    args += [sys.argv[i]]
args = ancien + args
save_to_json_file(args, 'add_item.json')
