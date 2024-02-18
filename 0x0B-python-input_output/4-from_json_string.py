#!/usr/bin/python3
"""
  From Json Module
"""
import json


def from_json_string(my_str):
    """
      Return a python object from json string
    """
    return json.loads(my_str)
