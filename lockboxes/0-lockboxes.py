#!/usr/bin/python3

def canUnlockAll(boxes):
    box_perm = []
    for i in range(len(boxes)):
        box_perm.append(0)
    box_perm[0] = 1

    while True:
        change = False
        for index, box in enumerate(boxes):
            if box_perm[index] == 1:
                for item in box:
                    if box_perm[item] != 1:
                        change = True
                        box_perm[item] = 1
        if change is False:
            break

    return 0 not in box_perm
