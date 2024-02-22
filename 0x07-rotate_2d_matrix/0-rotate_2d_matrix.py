#!/usr/bin/python3
"""Rotation of 2D Matrix"""


def rotate_2d_matrix(matrix):
    """Rotates matrix 90 deg clockwise"""

    rot = [[row[col] for row in matrix[::-1]] for col in range(len(matrix))]
    for row in range(len(matrix)):
        for col in range(len(matrix)):
            matrix[row][col] = rot[row][col]
