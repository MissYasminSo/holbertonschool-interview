#!/usr/bin/python3
"""Module: Lockbox"""


def canUnlockAll(boxes):
    """Return bool if boxes can be unlocked"""

    box_perm = []
    for i in range(len(boxes)):
        box_perm.append(0)
    box_perm[0] = 1

    while True:
        change = False
        for index, box in enumerate(boxes):
            if box_perm[index] == 1:
                for item in box:
                    if item >= len(boxes):
                        continue
                    if box_perm[item] != 1:
                        change = True
                        box_perm[item] = 1
        if change is False:
            break

    return 0 not in box_perm
