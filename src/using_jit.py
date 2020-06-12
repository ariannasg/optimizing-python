#!usr/bin/env python3
import numba
from numba.typed import List


# JIT, Just-In-Time compiling, is a technology that has been used very
# successfully in several dynamic languages to gain performance.
# The idea behind Just-In-Time is that we collect information on the code at
# run time and according to this information, we generate specific machine
# code for these cases. If you're function runs only once, JIT will not help.
# But in most cases, bottlenecks are in functions that are called many times.
# Numba, this is a compiler kit called LLVM, under the hood, to generate
# machine code for Python functions.
# LLVM is an acronym that stands for low level virtual machine.
# It also refers to a compiling technology called the LLVM project, which is a
# collection of modular and reusable compiler and toolchain technologies.


def poly(coeffs, n):
    """Compute value of polynomial given coefficients"""
    total = 0
    for i, c in enumerate(coeffs):
        total += c * n ** i
    return total


@numba.jit
def poly_j(coeffs, n):
    """Compute value of polynomial given coefficients - JIT"""
    total = 0
    for i, c in enumerate(coeffs):
        total += c * n ** i
    return total


if __name__ == '__main__':
    # previously we had coeffs = [4, 8, 15, 16, 23, 42] but we were getting
    # a warning:
    # http://numba.pydata.org/numba-doc/latest/reference/deprecation.html#deprecation-of-reflection-for-list-and-set-types
    coeffs = List()
    [coeffs.append(x) for x in [4, 8, 15, 16, 23, 42]]

# In [7]: %run src/using_jit.py
#
# In [8]: poly(coeffs, 7)
# Out[8]: 767400
#
# In [9]: poly_j(coeffs, 7)
# Out[9]: 767400
#
# In [10]: %timeit poly(coeffs, 7)
# 18.6 µs ± 2.08 µs per loop (mean ± std. dev. of 7 runs, 100000 loops each)
#
# In [11]: %timeit poly_j(coeffs, 7)
# 1.67 µs ± 36.7 ns per loop (mean ± std. dev. of 7 runs, 1000000 loops each)
