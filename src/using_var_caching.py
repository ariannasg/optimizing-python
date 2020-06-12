#!usr/bin/env python3
import dis
import random
from timeit import timeit


# dis is the module for disassembling Python byte code into mnemonics.
# Mnemonic code is code that can be remembered comparatively easily and that
# aids its user in recalling the information it represents.
# Mnemonics are widely used in computer programming and communications system
# operations to specify instructions.
# while using dis.dis we can look for "LOAD_ATTR" AND "LOAD_METHOD" that exist
# inside loops ("GET_ITER" and "FOR_ITER" in this case) to try and optimize.
# be aware of code complexity -> is it a good trade-off?
class Config:
    """Global configuration"""
    factor = 7.3
    threshold = 12


def normalize(numbers):
    """Normalize list of numbers"""
    norm = []
    for num in numbers:
        if num > Config.threshold:
            num /= Config.factor
        norm.append(num)
    return norm


def normalize2(numbers):
    """Normalize list of numbers, caching names"""
    thr = Config.threshold
    fact = Config.factor

    norm = []
    for num in numbers:
        if num > thr:
            num /= fact
        norm.append(num)
    return norm


def normalize3(numbers):
    """Normalize list of numbers, caching names and append"""
    thr = Config.threshold
    fact = Config.factor

    norm = []
    append = norm.append

    for num in numbers:
        if num > thr:
            num /= fact
        append(num)
    return norm


if __name__ == '__main__':
    # note: it's better to use disassemble in IPython
    print('Disassembling normalize to see what optimizations we can do')
    dis.dis(normalize)
    print('================================')
    print('Disassembling normalize2 to see optimizations done and '
          'what else we can do')
    dis.dis(normalize2)
    print('================================')
    print('Disassembling normalize3 to see optimizations done and '
          'what else we can do')
    dis.dis(normalize3)

    random.seed(353)
    numbers = [random.randint(5, 50) for _ in range(10)]

    print('================================')
    print('Timeit:')
    print('normalize', timeit('normalize(numbers)',
                              'from __main__ import normalize, numbers'))
    print('normalize2', timeit('normalize2(numbers)',
                               'from __main__ import normalize2, numbers'))
    print('normalize3', timeit('normalize3(numbers)',
                               'from __main__ import normalize3, numbers'))

# we can see the gains on time:
# normalize:
# 1.992294239
# normalize2:
# 1.6807818069999998/1.992294239 = 0.8436413528172632 -> 15% faster than normalize
# normalize3:
# 1.3995182750000001/1.6807818069999998 = 0.8326591049304476 -> 17% faster than normalize2
# 1.3995182750000001/1.992294239 = 0.7024656537191343 -> 30% faster than normalize and

# CONSOLE OUTPUT:
# Disassembling normalize to see what optimizations we can do
#  13           0 BUILD_LIST               0
#               2 STORE_FAST               1 (norm)
#
#  14           4 LOAD_FAST                0 (numbers)
#               6 GET_ITER
#         >>    8 FOR_ITER                34 (to 44)
#              10 STORE_FAST               2 (num)
#
#  15          12 LOAD_FAST                2 (num)
#              14 LOAD_GLOBAL              0 (Config)
#              16 LOAD_ATTR                1 (threshold)
#              18 COMPARE_OP               4 (>)
#              20 POP_JUMP_IF_FALSE       32
#
#  16          22 LOAD_FAST                2 (num)
#              24 LOAD_GLOBAL              0 (Config)
#              26 LOAD_ATTR                2 (factor)
#              28 INPLACE_TRUE_DIVIDE
#              30 STORE_FAST               2 (num)
#
#  17     >>   32 LOAD_FAST                1 (norm)
#              34 LOAD_METHOD              3 (append)
#              36 LOAD_FAST                2 (num)
#              38 CALL_METHOD              1
#              40 POP_TOP
#              42 JUMP_ABSOLUTE            8
#
#  18     >>   44 LOAD_FAST                1 (norm)
#              46 RETURN_VALUE
# ================================
# Disassembling normalize2 to see optimizations done and what else we can do
#  23           0 LOAD_GLOBAL              0 (Config)
#               2 LOAD_ATTR                1 (threshold)
#               4 STORE_FAST               1 (thr)
#
#  24           6 LOAD_GLOBAL              0 (Config)
#               8 LOAD_ATTR                2 (factor)
#              10 STORE_FAST               2 (fact)
#
#  26          12 BUILD_LIST               0
#              14 STORE_FAST               3 (norm)
#
#  27          16 LOAD_FAST                0 (numbers)
#              18 GET_ITER
#         >>   20 FOR_ITER                30 (to 52)
#              22 STORE_FAST               4 (num)
#
#  28          24 LOAD_FAST                4 (num)
#              26 LOAD_FAST                1 (thr)
#              28 COMPARE_OP               4 (>)
#              30 POP_JUMP_IF_FALSE       40
#
#  29          32 LOAD_FAST                4 (num)
#              34 LOAD_FAST                2 (fact)
#              36 INPLACE_TRUE_DIVIDE
#              38 STORE_FAST               4 (num)
#
#  30     >>   40 LOAD_FAST                3 (norm)
#              42 LOAD_METHOD              3 (append)
#              44 LOAD_FAST                4 (num)
#              46 CALL_METHOD              1
#              48 POP_TOP
#              50 JUMP_ABSOLUTE           20
#
#  31     >>   52 LOAD_FAST                3 (norm)
#              54 RETURN_VALUE
# ================================
# Disassembling normalize3 to see optimizations done and what else we can do
#  36           0 LOAD_GLOBAL              0 (Config)
#               2 LOAD_ATTR                1 (threshold)
#               4 STORE_FAST               1 (thr)
#
#  37           6 LOAD_GLOBAL              0 (Config)
#               8 LOAD_ATTR                2 (factor)
#              10 STORE_FAST               2 (fact)
#
#  39          12 BUILD_LIST               0
#              14 STORE_FAST               3 (norm)
#
#  40          16 LOAD_FAST                3 (norm)
#              18 LOAD_ATTR                3 (append)
#              20 STORE_FAST               4 (append)
#
#  42          22 LOAD_FAST                0 (numbers)
#              24 GET_ITER
#         >>   26 FOR_ITER                28 (to 56)
#              28 STORE_FAST               5 (num)
#
#  43          30 LOAD_FAST                5 (num)
#              32 LOAD_FAST                1 (thr)
#              34 COMPARE_OP               4 (>)
#              36 POP_JUMP_IF_FALSE       46
#
#  44          38 LOAD_FAST                5 (num)
#              40 LOAD_FAST                2 (fact)
#              42 INPLACE_TRUE_DIVIDE
#              44 STORE_FAST               5 (num)
#
#  45     >>   46 LOAD_FAST                4 (append)
#              48 LOAD_FAST                5 (num)
#              50 CALL_FUNCTION            1
#              52 POP_TOP
#              54 JUMP_ABSOLUTE           26
#
#  46     >>   56 LOAD_FAST                3 (norm)
#              58 RETURN_VALUE
# ================================
# Timeit:
# normalize 1.992294239
# normalize2 1.6807818069999998
# normalize3 1.3995182750000001
