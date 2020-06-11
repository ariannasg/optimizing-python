#!usr/bin/env python3

from collections import deque
from timeit import timeit


class TaskQueue:
    """Task queue using list"""

    def __init__(self):
        self._tasks = []

    def push(self, task):
        self._tasks.insert(0, task)  # O(n)

    def pop(self):
        return self._tasks.pop()  # O(1)

    def __len__(self):
        return len(self._tasks)  # O(1)


class DTaskQueue:
    """Task queue using deque"""

    def __init__(self):
        self._tasks = deque()

    def push(self, task):
        self._tasks.append(task)

    def pop(self):
        return self._tasks.popleft()

    def __len__(self):
        return len(self._tasks)


def test_queue(count=10, *, cls):
    tq = cls()

    for i in range(count):
        tq.push(i)
        assert len(tq) == i + 1

    for i in range(count):
        assert tq.pop() == i
        assert len(tq) == count - i - 1


if __name__ == '__main__':
    test_queue(cls=TaskQueue)
    test_queue(cls=DTaskQueue)
    print('using a list',
          timeit('test_queue(cls=TaskQueue)',
                 'from __main__ import test_queue, TaskQueue'))
    print('using a deque',
          timeit('test_queue(cls=DTaskQueue)',
                 'from __main__ import test_queue, DTaskQueue'))

# using a deque is always a bit faster
# 12.596856459/13.187268659 = 0.9552286212355992 -> we have around 5% speedup

# CONSOLE OUTPUT (it varies)
# using a list 13.187268659
# using a deque 12.596856459
