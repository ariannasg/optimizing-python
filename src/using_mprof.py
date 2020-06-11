#!usr/bin/env python3


# We should measure loops over time with mprof.
def sum_of_diffs(*args):
    """Compute sum of diffs"""
    total = 0
    for v1, v2 in zip(args[0], args[1]):
        total += v2 - v1

    return total


if __name__ == '__main__':
    values = list(range(1, 100_000_000, 5))
    print(sum_of_diffs(values, values))

# CONSOLE OUTPUT
# 0
