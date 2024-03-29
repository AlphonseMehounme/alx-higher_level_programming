#!/usr/bin/python3
"""
  Load Frm Json Module
"""
import json


def load_from_json_file(filename):
    """
      Create object from a json file
    """
    with open(filename, encoding='utf-8') as f:
        return json.load(f)
