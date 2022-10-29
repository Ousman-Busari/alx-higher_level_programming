#!/usr/bin/python3
"""
12-pascal_triangle
"""


def pascal_triangle(n):
    """
    creates a pascal triangle using list in list
    """
    triangle = []
    if n <= 0 or type(n) is not int:
        return triangle

    for i in range(n):
        row = []
        j = 0
        while j <= i:
            if j == 0 or j == i:
                row.append(1)
                j += 1
                continue
            if j < i:
                row.append(prev_row[j - 1] + prev_row[j])
            j += 1
        triangle.append(row)
        prev_row = row

    return triangle
