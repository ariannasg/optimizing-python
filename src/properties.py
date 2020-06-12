#!usr/bin/env python3
from timeit import timeit


# to know more about the usage of @property:
# https://www.programiz.com/python-programming/property
# In Python we use properties only if you have a good reason and not by
# default like with Java or C++ where you add getter and setter to everything!
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y


class PPoint:
    def __init__(self, x, y):
        self._x = x
        self._y = y

    @property
    def x(self):
        return self._x

    @x.setter
    def x(self, value):
        if not isinstance(value, (int, float)):
            raise TypeError(type(value))
        self._x = value

    @property
    def y(self):
        return self._y

    @y.setter
    def y(self, value):
        if not isinstance(value, (int, float)):
            raise TypeError(type(value))
        self._y = value


if __name__ == '__main__':
    point1 = Point(1, 2)
    point2 = PPoint(1, 2)

    print('accessing an attribute object',
          timeit('point1.x', 'from __main__ import point1'))

    print('accessing a property object',
          timeit('point2.x', 'from __main__ import point2'))

# 0.04458180700000003/0.14007672999999998 = 0.31826704549713597
# accessing the attr adds around 70% speedup
# 0.14007672999999998/0.04458180700000003 = 3.142015531133583
# accessing the property it's more than 3 times slower than accessing the attr

# CONSOLE OUTPUT:
# accessing an attribute object 0.04458180700000003
# accessing a property object 0.14007672999999998
