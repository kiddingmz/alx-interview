#!/usr/bin/python3
"""UTF-8 Validation"""


def validUTF8(data):
    """Determines if a given data set represents a valid UTF-8 encoding"""

    def check(num):
        mask = 1 << (8 - 1)
        i = 0
        while num & mask:
            mask >>= 1
            i += 1
        return i

    i = 0
    while i < len(data):
        j = check(data[i])
        k = i + j - (j != 0)
        i += 1
        if j == 1 or j > 4 or k >= len(data):
            return False
        while i < len(data) and i <= k:
            current = check(data[i])
            if current != 1:
                return False
            i += 1  # Go to next number
    return True
