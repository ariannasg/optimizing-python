#!usr/bin/env python3
from functools import lru_cache


@lru_cache()
def fib(n):
    """Return n'th fibonacci number"""
    if n < 2:
        return 1
    return fib(n - 1) + fib(n - 2)


# this test is using the benchmark fixture from pytest-benchmark
def test_fib(benchmark):
    result = benchmark(fib, 30)
    assert result == 1346269
