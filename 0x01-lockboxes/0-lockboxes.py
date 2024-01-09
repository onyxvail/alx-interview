#!/usr/bin/python3
"""
Module with the canUnlockAll function.
"""


def canUnlockAll(boxes):
    """
    Determines if all the boxes can be opened.

    Args:
        boxes (list): A list of lists where
        each box may contain keys to other boxes.

    Returns:
        bool: True if all boxes can be opened, False otherwise.
    """
    unlocked = [False] * len(boxes)
    unlocked[0] = True
    for index, box in enumerate(boxes):
        if unlocked[index]:
            for index, key in enumerate(box):
                if key < len(unlocked):
                    unlocked[key] = True
                    for i in boxes[key]:
                        unlocked[i] = True
    return all(unlocked)
