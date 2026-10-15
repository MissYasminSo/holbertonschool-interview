#!/usr/bin/python3
"""Module: Min Operation."""


def minOperations(n):
    """Minimum operation problem"""

    if n <= 1:
        return 0
    if n == 2:
        return 2

    result = 0
    divisor = 2

    while n != 1:
        if n % divisor == 0:
            n = n / divisor
            result = result + divisor
        else:
            divisor = divisor + 1

    return result
