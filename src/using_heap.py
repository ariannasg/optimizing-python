#!usr/bin/env python3

from heapq import heappop, heappush
from random import random, seed, randint
from timeit import timeit


class PriorityQueue:
    """Priority queue using list + sort"""

    def __init__(self):
        self._tasks = []

    def push(self, task, priority):
        self._tasks.append((priority, task))
        self._tasks.sort(reverse=True)

    def pop(self):
        return self._tasks.pop()[1]

    def __len__(self):
        return len(self._tasks)


class HPriorityQueue:
    """Priority queue using heap"""

    def __init__(self):
        self._tasks = []

    def push(self, task, priority):
        heappush(self._tasks, (priority, task))

    def pop(self):
        return heappop(self._tasks)[1]

    def __len__(self):
        return len(self._tasks)


def test_pqueue(cls):
    pq = cls()

    todo = [
        (2, 'fix bug'),
        (10, 'read email'),
        (4, 'add feature'),
        (6, 'eat lunch'),
    ]

    for priority, task in todo:
        pq.push(task, priority)

    tasks = [pq.pop(), pq.pop()]

    # Don't forget to nap
    pq.push('nap', 5)

    while pq:
        tasks.append(pq.pop())

    expected = [item[1] for item in sorted(todo + [(5, 'nap')])]
    assert tasks == expected


def gen_cases(count):
    seed(353)  # Same cases every time

    cases = []
    for _ in range(count):
        if random() < 0.5:
            cases.append(-1)
        else:
            cases.append(randint(1, 100))
    return cases


def benchmark_pq(cases, *, cls):
    pq = cls()

    for i, case in enumerate(cases):
        if case < 0 and pq:
            pq.pop()
        elif case > 0:
            pq.push(f'task {i}', case)


if __name__ == '__main__':
    test_pqueue(cls=PriorityQueue)
    test_pqueue(cls=HPriorityQueue)

    cases = gen_cases(10)
    print('using list + sort',
          timeit('benchmark_pq(cases, cls=PriorityQueue)',
                 'from __main__ import benchmark_pq, cases, PriorityQueue'))
    print('using a heap',
          timeit('benchmark_pq(cases, cls=HPriorityQueue)',
                 'from __main__ import benchmark_pq, cases, HPriorityQueue'))

# using a heap is always a bit faster
# 6.514968917999999/7.282896069 = 0.894557447514771 -> we have around 10%
# speedup

# CONSOLE OUTPUT (it varies):
# using list + sort 7.282896069
# using a heap 6.514968917999999
