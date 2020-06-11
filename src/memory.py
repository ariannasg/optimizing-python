#!usr/bin/env python3

# Data is stored in the computer memory, known as the heap.
# Every time we create a new object, we need to allocate storage for it and
# this operation takes time.
# This is one reason for why we care about memory allocation.
# Another reason is that accessing memory in modern computers is done in
# layers.

# We have the CPU, and then we have L1 and L2 caches.
# Then we have the memory.
# Finally we have the SSD disk.

# Accessing layer 1 cache is about 0.5 ns.
# Accessing layer 2 cache is about 0.7 ns.
# Accessing the main memory is about 100 ns.
# Accessing the SSD disk is about 16,000 ms (ms vs ns!).

# Modern operating systems give us the appearance of having infinite memory.
# i.e: The computer I use right now has 16 GB of memory, but programs can use
# much more than that. This is done by swapping some section of memory into
# the hard drive. When we try to access the section memory that is currently
# swapped to disk, the operating system will pick another section of memory,
# will write to the disk, and then load the section memory we require into
# actual memory. This is also known as a page fault, and it's a very
# costly operation.
