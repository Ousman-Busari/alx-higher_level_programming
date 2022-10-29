#!/usr/bin/python3
"""
100-append_after
"""


def append_after(filename="", search_string="", new_string=""):
    """
    append_after
    """
    with open(filename, mode="r", encoding="utf-8") as f:
        list_all_lines = f.readlines()

    new_content = []
    line_num = 0;
    for line in list_all_lines:
        new_content.append(line)
        if search_string in line:
            new_content.append(new_string)

    with open(filename, mode='w', encoding='utf-8') as f:
        f.write("".join(new_content))
