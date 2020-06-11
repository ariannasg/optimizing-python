#!usr/bin/env python3
import cProfile

from src.using_cprofile import gen_cases, bench_login


def bench_targeted_login(cases):
    bench_login(cases)


# Here we run the file without "-m cProfile"
if __name__ == '__main__':
    n = 2
    cases = list(gen_cases(n))

    # Here the output is smaller, because we're targeting the code we want to
    # profile by running cProfile after we generated the test cases.
    cProfile.run('bench_targeted_login(cases)')
