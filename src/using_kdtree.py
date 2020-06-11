#!usr/bin/env python3

import math
from random import random
from timeit import timeit

from scipy.spatial import KDTree  # quick nearest-neighbor lookup


def distance(loc1, loc2):
    x1, y1 = loc1
    x2, y2 = loc2

    return math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)


def find_closest(loc, drivers):
    """Find closest driver using min"""

    def dist(driver):
        return distance(driver, loc)

    return min(drivers, key=dist)


def find_closest_kd(loc, tree):
    """Find closes driver using KDTree"""
    _, idx = tree.query(loc)
    return tuple(tree.data[idx])


def gen_drivers(lat, lng):
    """Generate list of drivers"""
    # 1 degree is ~ 69miles/110km
    return [(lat + random(), lng + random()) for _ in range(10)]


def test_find_closest(kd=False):
    lat, lng = 34.3852712, -119.487444  # lynda office

    drivers = gen_drivers(lat, lng)
    if kd:
        tree = KDTree(drivers)
        closest = find_closest_kd((lat, lng), tree)
    else:
        closest = find_closest((lat, lng), drivers)

    assert closest in drivers

    loc = (lat, lng)
    min_dist = distance(loc, closest)

    for driver in drivers:
        if driver == closest:
            continue
        assert distance(driver, loc) >= min_dist


if __name__ == '__main__':
    test_find_closest()
    test_find_closest(kd=True)

    lat, lng = 34.3852712, -119.487444
    drivers = gen_drivers(lat, lng)
    tree = KDTree(drivers)
    print('using math calcs',
          timeit('find_closest((lat, lng), drivers)',
                 'from __main__ import find_closest, lat, lng, drivers'))
    print('using a KD tree',
          timeit('find_closest_kd((lat, lng), tree)',
                 'from __main__ import find_closest_kd, lat, lng, tree'))

# we should've got 8 times faster results with KD tree but
# that's not the case...not sure way.
# atm the KDTree is slower by almost 99%
# 7.084976138/75.635740505 = 0.09367233123779145

# CONSOLE OUTPUT (it varies):
# using math calcs 7.084976138
# using a KD tree 75.635740505
