#!/usr/bin/python3
"""
Minimum Operations
"""
import math


def minOperations(n: int) -> int:
    """Return the sum of prime factors of a given number.

    That is the minimum number of operations required to get the
    exact number of `H` characters. Since at each point, n is divisible by that
    particular number dividing it and the remainder will always be 0,
    I used integer division to avoid type errors.
    """
    # If n is impossible to achieve, return 0
    if n <= 1:
        return 0

    result = 0

    # While n is divisble by 2
    while n % 2 == 0:
        # Divide n by 2
        n = n // 2
        # Add 2 to result
        result += 2

    # n is odd at this point
    # Divide n repeatedly by i where i = i + 2 starting from 3
    for i in range(3, int(math.sqrt(n)) + 1, 2):
        # While n is divisible by i
        while n % i == 0:
            # Divide n by i
            n = n // i
            # Add i to result
            result += i

    # If n is a prime number that is not 2,
    # then n is greater than 2 at this point
    if n > 2:
        # Just add n to the result
        result += n

    return result