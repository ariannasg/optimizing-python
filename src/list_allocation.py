#!usr/bin/env python3
from timeit import timeit

# When you create a list and append to it, Python needs to reallocate memory
# for the list. To avoid reallocation on every append, the list grows in fixed
# sizes. The sizes are zero, four, eight, 16, 25, etc. However, when we create
# a list with multiplication, Python knows the size of the list in advance
# and creates it in one allocation.
# ATTENTION!
# Python because everything is a reference, this might have a surprising
# effect, look the example of the empty list.
# Make sure you initialized with immutable volumes, like numbers, strings,
# and tuples, otherwise you will have to get back to our initial
# implementation.
# The best option would be to use numpy which creates ultra fast arrays
import numpy


def alloc_list(size):
    """Alloc zeros with range"""
    return [0 for _ in range(size)]


def alloc_list_fixed(size):
    """Alloc zeros with *"""
    return [0] * size


if __name__ == '__main__':
    print([1, 2, 3] * 3)
    my_list = [[]] * 5
    print(my_list)
    my_list[0].append(1)
    print(my_list)

    print('allocating a list with loop',
          timeit('alloc_list(100)', 'from __main__ import alloc_list'))
    print('allocating a list with *',
          timeit('alloc_list_fixed(100)',
                 'from __main__ import alloc_list_fixed'))
    print('allocating a list with numpy',
          timeit('numpy.zeros(100)',
                 'from __main__ import numpy'))

# 0.6352753790000003/3.813065881 = 0.1666048788103801.
# we gain about 85% speed-up. The latter is about 6 times faster.

# CONSOLE OUTPUT:
# [1, 2, 3, 1, 2, 3, 1, 2, 3]
# [[], [], [], [], []]
# [[1], [1], [1], [1], [1]]
# allocating a list with loop 3.813065881
# allocating a list with * 0.6352753790000003
# allocating a list with numpy 1.0309689520000003

# In [7]: %run -n src/list_allocation.py
#
# In [8]: %timeit alloc_list(1000)
# 40.7 µs ± 3.57 µs per loop (mean ± std. dev. of 7 runs, 10000 loops each)
#
# In [9]: %timeit alloc_list_fixed(1000)
# 2.5 µs ± 84.3 ns per loop (mean ± std. dev. of 7 runs, 100000 loops each)
#
# In [10]: import numpy
#
# In [11]: %timeit numpy.zeros(1000)
# 1.31 µs ± 11.6 ns per loop (mean ± std. dev. of 7 runs, 1000000 loops each)
