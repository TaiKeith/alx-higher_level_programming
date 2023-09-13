#!/usr/bin/python3
"""
This module returns the JSON representation of an object(string)
"""
import json


def to_json_string(my_obj):
    """A function that returns the JSON representation of an object"""
    return json.dumps(my_obj)
