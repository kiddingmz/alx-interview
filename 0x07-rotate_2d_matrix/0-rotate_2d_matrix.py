#!/usr/bin/python3
"""Rotate 2D Matrix"""


def rotate_2d_matrix(matrix: list) -> list:
    """Given an n x n 2D matrix, rotate it 90 degrees clockwise.
    Args:
        matrix: list of lists
    Returns:
        list of lists"""
    n = len(matrix)

    # Transpose the matrix and convert rows to columns and vice versa
    for i in range(n):
        for j in range(i, n):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

    # Reverse each row
    for i in range(n):
        matrix[i].reverse()
