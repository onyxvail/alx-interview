#!/usr/bin/python3
"""
Minimum Operations module
"""


def minOperations(n):
    """
    Calculates the fewest number of operations
    needed to result in exactly n H characters in the file.

    Args:
        n (int): The target number of H characters.

    Returns:
        int: The minimum number of operations required.
    """
    nb_operations = 0
    min_operations = 2
    while n > 1:
        while n % min_operations == 0:
            nb_operations += min_operations
            n /= min_operations
        min_operations += 1
    return nb_operations
