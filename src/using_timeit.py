#!usr/bin/env python3
from timeit import timeit

items = {
    'a': 1,
    'b': 2,
}
default = -1


def use_catch(key):
    """Use try/catch to get a key with default"""
    try:
        return items[key]
    except KeyError:
        return default


def use_get(key):
    """Use dict.get to get a key with default"""
    return items.get(key, default)


if __name__ == '__main__':
    # Key is in the dictionary
    print('catch', timeit('use_catch("a")', 'from __main__ import use_catch'))
    print('get', timeit('use_get("a")', 'from __main__ import use_get'))

    # Key is missing from the dictionary
    print('catch', timeit('use_catch("x")', 'from __main__ import use_catch'))
    print('get', timeit('use_get("x")', 'from __main__ import use_get'))


# the try-catch is always faster when the key is in the dict -> 25% faster.
# the get is faster when the key is not in the dict -> 50% faster.
# we should decide what's more likely to happen in our code and go with
# that solution.
# 0.13891867400000002/0.18536753300000008 = 0.7494228992085683
# 0.20828379099999994/0.4114921249999999 =  0.5061671374634448

# CONSOLE OUTPUT (it varies)
# catch 0.13891867400000002
# get 0.18536753300000008
# catch 0.4114921249999999
# get 0.20828379099999994
