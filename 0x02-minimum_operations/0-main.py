#!/usr/bin/python3
"""
Main script for Minimum Operations module
"""

min_operations = __import__('0-minoperations').min_operations

if __name__ == "__main__":
    n1 = 4
    print("Min # of operations to reach {} char: {}"
          .format(n1, min_operations(n1)))

    n2 = 12
    print("Min # of operations to reach {} char: {}"
          .format(n2, min_operations(n2)))
