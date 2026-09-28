#!/usr/bin/python3

def pascal_triangle(n):
    result = []
    if n <= 0:
        return result

    idx = 0
    while idx < n:
        row_list = []

        row_idx = 0
        while row_idx <= idx:
            if row_idx == 0 or row_idx == idx:
                row_list.append(1)
            else:
                sum = result[idx - 1][row_idx - 1] + result[idx - 1][row_idx]
                row_list.append(sum)
            row_idx = row_idx + 1

        result.append(row_list)
        idx = idx + 1

    return result
