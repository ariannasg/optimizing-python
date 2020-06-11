#!usr/bin/env python3
from bisect import bisect
from timeit import timeit

cutoffs = [60, 70, 80, 90]
names = 'FDCBA'


def grade(score):
    """Give a letter grade from numeric score

    >>> grade(80)
    'C'
    """
    for cutoff, name in zip(cutoffs, names):
        if score < cutoff:
            return name
    return 'A'


def grade2(score):
    """Give a letter grade from numeric score

    >>> grade(80)
    'B'
    """
    i = bisect(cutoffs, score)
    return names[i]


def test_grades(fn=grade):
    cases = [
        (100, 'A'),
        (92, 'A'),
        (87, 'B'),
        (76, 'C'),
        (62, 'D'),
        (60, 'D'),
        (0, 'F'),
    ]

    for score, expected in cases:
        assert fn(score) == expected


if __name__ == '__main__':
    test_grades()
    test_grades(fn=grade2)
    print('using loop', timeit('grade(74)', 'from __main__ import grade'))
    print('using bisect', timeit('grade2(74)', 'from __main__ import grade2'))

# using bisect is always faster.
# 0.317963424/0.62431804 = 0.5092971908996895 -> we have around 50% speedup

# CONSOLE OUTPUT (it varies):
# using loop 0.62431804
# using bisect 0.317963424
