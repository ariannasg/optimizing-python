#!usr/bin/env python3
from time import perf_counter


def upto_for(n):
    """Sum 1...n with a for loop"""
    total = 0
    for i in range(n):
        total += i
    return total


def upto_sum(n):
    """Sum 1...n with built-in sum and range"""
    return sum(range(n))


if __name__ == '__main__':
    n = 1_000_000

    start = perf_counter()
    upto_for(n)
    duration = perf_counter() - start
    print('upto_for', duration)

    start = perf_counter()
    upto_sum(n)
    duration = perf_counter() - start
    print('upto_sum', duration)

# CONSOLE OUTPUT (it varies but sum is always lower by half or more):
# upto_for 0.076320889
# upto_sum 0.02653118900000001
