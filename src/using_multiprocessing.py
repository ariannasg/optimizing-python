#!usr/bin/env python3
import bz2
from concurrent.futures import ProcessPoolExecutor


def unpack(requests):
    """Unpack a list of requests compressed in bz2"""
    return [bz2.decompress(request) for request in requests]


def unpack_proc(requests):
    """Unpack a list of requests compressed in bz2 using a process pool"""
    # Default to numbers of cores
    with ProcessPoolExecutor() as pool:
        return list(pool.map(bz2.decompress, requests))


if __name__ == '__main__':
    with open('src/huck-finn.txt', 'rb') as fp:
        data = fp.read()

    bz2data = bz2.compress(data)
    print(len(bz2data) / len(data))  # About 27%
    print(bz2.decompress(bz2data) == data)  # Loseless

    requests = [bz2data] * 300

# attention to the way we're using %time here: the _ = is so we discard the
# output.
# by seeing that the CPU time and the Wall time were very close, we knew
# that this unpack was a CPU-bound operations, we could optimise it by using
# multiprocessing. the diff in performance is almost the double:
# from 9.76 s to 5.47 s -> almost 2 times faster

# In [5]: %run src/using_multiprocessing.py
# 0.27078187856861546
# True
#
# In [6]: %time _ = unpack(requests)
# CPU times: user 9.37 s, sys: 244 ms, total: 9.61 s
# Wall time: 9.76 s
#
# In [7]: %prun -l 10 unpack(requests)
#          1205 function calls in 9.544 seconds
#
#    Ordered by: internal time
#
#    ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#       300    9.521    0.032    9.521    0.032 {method 'decompress' of '_bz2.BZ2Decompressor' objects}
#         1    0.014    0.014    9.543    9.543 <string>:1(<module>)
#         1    0.004    0.004    9.530    9.530 using_multiprocessing.py:9(<listcomp>)
#       300    0.004    0.000    9.526    0.032 bz2.py:341(decompress)
#       300    0.000    0.000    0.000    0.000 {method 'append' of 'list' objects}
#       300    0.000    0.000    0.000    0.000 {method 'join' of 'bytes' objects}
#         1    0.000    0.000    9.544    9.544 {built-in method builtins.exec}
#         1    0.000    0.000    9.530    9.530 using_multiprocessing.py:7(unpack)
#         1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
#
# In [8]: %time _ = unpack_proc(requests)
# CPU times: user 436 ms, sys: 423 ms, total: 859 ms
# Wall time: 5.47 s
