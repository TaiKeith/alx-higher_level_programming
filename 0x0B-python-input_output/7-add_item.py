#!/usr/bin/python3
"""
This module adds all arguments to a Python list and save them to a file
"""
import sys
import json

save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file

args = sys.argv[1:]
items = []

try:
    items = load_from_json_file("add_item.json")
except Exception:
    save_to_json_file(args, "add_item.json")

for arg in args:
    items.append(arg)

json_string = save_to_json_file(items, "add_item.json")
