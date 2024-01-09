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
    if not boxes or not isinstance(boxes, list):
        return False

    opened_boxes = set()
    opened_boxes.add(0)

    unopened_boxes = set(opened_boxes)

    while unopened_boxes:
        box = unopened_boxes.pop()
        keys = boxes[box]

        opened_boxes.update(keys)
        unopened_boxes.update(set(keys) - opened_boxes)

    return len(opened_boxes) == len(boxes)


if __name__ == "__main__":
    boxes1 = [[1], [2], [3], [4], []]
    print(canUnlockAll(boxes1))

    boxes2 = [[1, 4, 6], [2], [0, 4, 1], [5, 6, 2], [3], [4, 1], [6]]
    print(canUnlockAll(boxes2))

    boxes3 = [[1, 4], [2], [0, 4, 1], [3], [], [4, 1], [5, 6]]
    print(canUnlockAll(boxes3))
