#!usr/bin/env python3

# Problem:
# Let's say you're competing with Amazon and use robot walkers with an
# algorithm to pack shipments into a minimum number of boxes.
# We're going to simplify the problem and look only at volume.
# We'll get a list of items, each with its own volume, and the volume of the
# bin, called bin size, and return the optimal solution with the minimum
# number of bins that can hold all of these items.
# The 1st solution is a recursive algorithm that tries all options and
# return the best one.
# This problem is known as bin packing or the knapsack problem.
# We assume they cannot be solved in the polynomial type.
# Looking at the complexity chart, we see that two to the power of n is rising
# much, much higher than n to the power of two.
# The bin packing algorithm has been studied a lot, and there are many
# approximation algorithms for it. Let's try a greedy first fit algorithm ->
# If an item fits in a bin, we continue and don't try more solutions


def bin_pack(items, bin_size, bins=None):
    """Pack items in bins with size bin_size.
    We try all options first and then return the best one."""
    bins = [] if bins is None else bins

    if not items:
        return bins

    item = items[0]
    solutions = []
    for i, bin in enumerate(bins):
        if sum(bin) + item > bin_size:  # Can't add to bin
            continue
        sbins = bins[:]
        sbins[i].append(item)  # Add item to bin
        solutions.append(bin_pack(items[1:], bin_size, sbins))

    # Open new bin
    solutions.append(bin_pack(items[1:], bin_size, bins + [[item]]))

    return min(solutions, key=len)


def greedy_bin_pack(items, bin_size):
    """Pack items in bins with size bin_size - greedy first-fit.
    We go over every item and if it fits in the bin, we edit for the current
    bin. And if not, we create a new bin for it."""
    bins = []

    for item in items:
        for bin in bins:
            if sum(bin) + item < bin_size:
                bin.append(item)
                break
        else:  # No fitting bin
            bins.append([item])
    return bins

# Using the greedy solution is optimal in time but returns a higher number of
# bins that are needed for packing those items with a bin_size of 4.
# As business owners, we need to decide on the trade-off between time
# optimisation vs the outcome of the actual solution.

# In [1]: %run -n src/knapsack_problem.py
#
# In [2]: %timeit bin_pack([1, 2, 3] * 10, 4)
# 1.46 s ± 15.2 ms per loop (mean ± std. dev. of 7 runs, 1 loop each)
#
# In [3]: %timeit greedy_bin_pack([1, 2, 3] * 10, 4)
# 54.3 µs ± 1.16 µs per loop (mean ± std. dev. of 7 runs, 10000 loops each)
#
# In [6]: len(bin_pack([1, 2, 3] * 10, 4))
# Out[6]: 16
#
# In [7]: len(greedy_bin_pack([1, 2, 3] * 10, 4))
# Out[7]: 20
