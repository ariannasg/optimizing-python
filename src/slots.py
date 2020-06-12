#!usr/bin/env python3


# Python stores object attrs by default in __dict__.
# when doing self.x python is actually doing self.__dict__['x'].
# Here we're using __slots__ to reduce the objects memory.
# Check README.
# Having smaller objects might also make your program faster, since they can
# fit in a CPU cache line, which means that when the CPU tries to access them,
# it will be much faster than fetching them from main memory.
# If you have many instances, and you want to save some memory, you can use
# __slots__. The basic idea is that when you define the __slots__ class
# attribute, those attributes will get just the enough space,
# without wasting space.
# Another side effect apart __dict__ being gone, is that, as there is no
# __dict__, there is no way to add, at runtime, any attributes to the instance.
class Point:
    """A 2D point"""

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __repr__(self):
        cls_name = self.__class__.__name__
        return f'{cls_name}({self.x!r}, {self.y!r})'


class SPoint:
    """A 2D point"""
    __slots__ = ['x', 'y']

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __repr__(self):
        cls_name = self.__class__.__name__
        return f'{cls_name}({self.x!r}, {self.y!r})'


if __name__ == '__main__':
    def alloc_points(n):
        return [Point(i, i) for i in range(n)]


    def alloc_spoints(n):
        return [SPoint(i, i) for i in range(n)]


    n = 1_000_000
    points = alloc_points(n)
    spoints = alloc_spoints(n)

# Using __slots__ removes __dict__
# In [2]: dir(Point)
# Out[2]:
# ['__class__',
#  '__delattr__',
#  '__dict__',
#  '__dir__',
#  '__doc__',
#  '__eq__',
#  '__format__',
#  '__ge__',
#  '__getattribute__',
#  '__gt__',
#  '__hash__',
#  '__init__',
#  '__init_subclass__',
#  '__le__',
#  '__lt__',
#  '__module__',
#  '__ne__',
#  '__new__',
#  '__reduce__',
#  '__reduce_ex__',
#  '__repr__',
#  '__setattr__',
#  '__sizeof__',
#  '__str__',
#  '__subclasshook__',
#  '__weakref__']
#
# In [3]: dir(SPoint)
# Out[3]:
# ['__class__',
#  '__delattr__',
#  '__dir__',
#  '__doc__',
#  '__eq__',
#  '__format__',
#  '__ge__',
#  '__getattribute__',
#  '__gt__',
#  '__hash__',
#  '__init__',
#  '__init_subclass__',
#  '__le__',
#  '__lt__',
#  '__module__',
#  '__ne__',
#  '__new__',
#  '__reduce__',
#  '__reduce_ex__',
#  '__repr__',
#  '__setattr__',
#  '__sizeof__',
#  '__slots__',
#  '__str__',
#  '__subclasshook__',
#  'x',
#  'y']
