#!/usr/bin/python3
"""

This Module reads a text file.

"""

from sys import argv
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file

ls = []
i = 1
for j in range(1, len(argv)):
    ls.append(argv[j])

try:
    ls1 = load_from_json_file("add_item.json")
except FileNotFoundError:
    save_to_json_file([], "add_item.json")

ls1 = load_from_json_file("add_item.json")
ls = ls1 + ls
save_to_json_file(ls, "add_item.json")
