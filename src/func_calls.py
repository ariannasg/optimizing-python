#!usr/bin/env python3
import random
from timeit import timeit


# try to use inline logic when possible instead of calling functions that add
# time cost.
# again, be aware of the trade-offs between optimal time and code complexity.
def empty():
    """
    Is empty on purpose
    :rtype: NoneType
    """
    pass


def abs_even(num):
    """Make even number absolute in value"""
    if num % 2 == 0 and num < 0:
        return -num
    return num


def fix_nums(nums):
    """Fix numbers with abs_even"""
    return [abs_even(num) for num in nums]


def fix_nums_inline(nums):
    """Fix numbers with inline"""
    fixed = []
    append = fixed.append

    for num in nums:
        ab_num = -num if num % 2 == 0 and num < 0 else num
        append(ab_num)
    return fixed


if __name__ == '__main__':
    random.seed(353)
    # note: we should be using a much larger range here for profiling
    numbers = [random.randint(-20, 20) for _ in range(10)]

    assert abs_even(-4) == 4
    assert abs_even(-7) == -7

    print('calling an empty func',
          timeit('empty()', 'from __main__ import empty'))

    print('calculating abs value by calling a func',
          timeit('fix_nums(numbers)',
                 'from __main__ import fix_nums, numbers'))

    print('calculating abs value whilst avoiding calling a func',
          timeit('fix_nums_inline(numbers)',
                 'from __main__ import fix_nums_inline, numbers'))


# 1.4496156949999999/2.16791018 = 0.6686696286466998 -> almost 35% speed-up
# when not calling a function

# CONSOLE OUTPUT:
# calling an empty func 0.09769977000000002
# calculating abs value by calling a func 2.16791018
# calculating abs value whilst avoiding calling a func 1.4496156949999999
