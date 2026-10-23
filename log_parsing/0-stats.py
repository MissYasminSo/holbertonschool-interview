#!/usr/bin/python3
"""Module: Logging"""

import sys

total_size = 0
status_codes = {}
valid_codes = ["200", "301", "400", "401", "403", "404", "405", "500"]
line_count = 0


def print_info():
    """Prints info"""
    print(f"File size: {total_size}")

    for code in sorted(status_codes):
        print(f"{code}: {status_codes[code]}")


if __name__ == "__main__":
    try:
        for line in sys.stdin:
            line_count = line_count + 1
            info = line.split()

            if len(info) == 9:
                try:
                    code = info[7]

                    total_size = total_size + int(info[8])

                    if code in valid_codes:
                        if code in status_codes:
                            status_codes[code] = status_codes[code] + 1
                        else:
                            status_codes[code] = 1
                except ValueError:
                    pass

            if line_count % 10 == 0:
                print_info()

    except KeyboardInterrupt:
        print_info()
    else:
        print_info()
