#!/usr/bin/python3
"""UTF-8 validation module."""


def validUTF8(data):
    remaining = 0

    for num in data:
        byte = format(num & 255, '08b')

        if remaining == 0:
            if byte.startswith('0'):
                continue
            elif byte.startswith('110'):
                remaining = 1
            elif byte.startswith('1110'):
                remaining = 2
            elif byte.startswith('11110'):
                remaining = 3
            else:
                return False
        else:
            if not byte.startswith('10'):
                return False

            remaining -= 1

    return remaining == 0

