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
        json.dump([], add_item.json)

newlist = load_from_json_file('add_item.json')
for i in range(1, len(newlist)):
    newlist += [sys.argv[i]]

save_to_json_file('add_item.json')
