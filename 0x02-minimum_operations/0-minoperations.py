#!/usr/bin/python3
"""
Minimum Operations module
"""


def min_operations(n):
    """
    Calculates the fewest number of operations
    needed to result in exactly n H characters in the file.

    Args:
        n (int): The target number of H characters.

    Returns:
        int: The minimum number of operations required.
    """
    if n <= 1:
        return 0

    operations = 0

    for i in range(2, n + 1):
        while n % i == 0:
            n //= i
            operations += i

    return operations


if __name__ == "__main__":
    n1 = 4
    print("Min # of operations to reach {} char: {}"
          .format(n1, min_operations(n1)))

    n2 = 12
    print("Min # of operations to reach {} char: {}"
          .format(n2, min_operations(n2)))
