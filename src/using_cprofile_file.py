#!usr/bin/env python3
import cProfile

from src.using_cprofile import gen_cases, bench_login


def bench_targeted_login_with_file(cases):
    bench_login(cases)


# Here we run the file without "-m cProfile"
if __name__ == '__main__':
    n = 2
    cases = list(gen_cases(n))

    # Here we run cProfile after we generated the test cases and use an
    # output file and use pstats to drill it.
    cProfile.run('bench_targeted_login_with_file(cases)', filename='prof.out')
