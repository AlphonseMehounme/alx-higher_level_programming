#!/usr/bin/python3
"""
  Save To Json file Module
"""
import json


def save_to_json_file(my_obj, filename):
    """
      save object to file
    """
    with open(filename, 'w') as f:
        json.dump(my_obj, f)
