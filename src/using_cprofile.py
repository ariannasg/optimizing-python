#!usr/bin/env python3
from random import random

from src.login import login


# When using cProfile we get the number of calls, the total time, the time per
# call, etc., etc. We run it by doing:
# python -m cProfile src/using_cprofile.py
# Using cProfile will slow down the program. If we need a more lightweight
# statistical profiler then we can take a look at the vn prof package.
def gen_cases(n):
    """Generate tests cases. We try to emulate real data"""
    for _ in range(n):
        if random() > 0.1:  # 90% of logins are OK
            yield 'daffy', 'rabbit season'
        else:  # no such user
            if random() < 0.2:
                yield 'tweety', 'puddy tat'
            else:  # bad pwd
                yield 'daffy', 'duck season'


def bench_login(cases):
    """Benchmark login with test cases"""
    for user, passwd in cases:
        login(user, passwd)


if __name__ == '__main__':
    n = 2
    cases = list(gen_cases(n))

    # Here the output will be quite big, there's a lot of setup code. This is
    # because we are profiling the whole file, including the generation of the
    # test cases.
    bench_login(cases)
