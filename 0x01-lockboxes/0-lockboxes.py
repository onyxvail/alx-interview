#!/usr/bin/python3
''' lockbox module '''


def canUnlockAll(boxes):

    '''
        CanUnockAll
    '''
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
