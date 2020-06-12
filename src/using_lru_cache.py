#!usr/bin/env python3
import string
from crypt import crypt
from functools import lru_cache


# Once the cache grows over the size of physical memory it will start
# swapping to this and performance will degrade.
# We'd like to limit the size of the cache and the built-in LRU cache can
# do just that. LRU cache is part of the Python 3 standard lib but can be
# installed with pip when using Python 2.
# As the name says the eviction algorithm used in LRU cache is LRU:
# "Least Recently Used". When the cache is full and we need
# to store in a new key we'll evict the key that was least recently used.
# There are many other cache replacement algorithms, least frequently used,
# most frequently used, random and others. Picking the right algorithm can
# have a big effect on code performance and you should know your data in
# order to pick the right one. LRU is very widely-used and is considered a
# good default policy.
# ATTENTION!!
# LRU cache uses all the function arguments as keys to the cache.
# It will fail if one or more of the arguments is not hashable, say a list,
# a dict, etc. Sometimes in order to be able to use LRU cache
# you need to modify your functions and make the arguments hashable.

# Note:
# The lru_cache decorator can be used to implement simply in-memory caching
# in the application. For more advanced use cases, we should use 3rd party
# modules that use on-disk caching. A great example to use lru_cache will be
# on a memoized version of the the fibonacci function.
# i.e: https://books.google.co.uk/books?id=sgyLDwAAQBAJ&pg=PA52&lpg=PA52
# We prefer joblib over lru_cache When we'd like to save cached results
# between runs.
# When using joblib, the results will be stored on disk and will persist
# between runs.

# Note: Keep in secure place
salt = string.ascii_letters

# Note:Calculate once and store in database
users = {
    crypt('bunny', salt): 'bugs',
    crypt('duck', salt): 'daffy',
    crypt('fudd', salt): 'elmer',
}


def user_from_key(key):
    return users.get(crypt(key, salt))


@lru_cache(maxsize=1024)  # max size of 1024 entries for the cache
def user_from_key_cached(key):
    return users.get(crypt(key, salt))


# ns vs µs when using the lru cache!

# In [4]: %timeit user_from_key('bunny')
# 4.16 µs ± 126 ns per loop (mean ± std. dev. of 7 runs, 100000 loops each)
#
# In [5]: %timeit user_from_key_cached('bunny')
# 102 ns ± 2.62 ns per loop (mean ± std. dev. of 7 runs, 10000000 loops each)
