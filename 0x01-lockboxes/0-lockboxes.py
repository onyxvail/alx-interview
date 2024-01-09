#!/usr/bin/python3

def canUnlockAll(boxes):
    x = len(boxes)
    item = [False] * x
    item[0] = True
    stack = [0]

    while stack:
        box = stack.pop()
        for each in boxes[box]:
            if each >= 0 and each < x and not item[each]:
                item[each] = True
                stack.append(each)

    return all(item)
