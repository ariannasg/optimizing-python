#!usr/bin/env python3

# Modern computers have more than one core and can execute several computations
# in parallel. The operating system gives each process a slice of time to run
# on a specific core and then suspends that process.
# This gives the illusion of parallelism and is known as concurrency.
# Concurrency is about dealing with a lot of things at once.
# Parallelism is about doing a lot of things at once.

# Spreading our computation over several cores or even letting some computation
# happen while other units of work are waiting can significantly speed up our
# code. An example of waiting will be database returning results.

# Amdahl's law: S(N) = 1/(1-P)+P(/N)
# Gives the theoretical limit on speedup or latency you can get from going
# parallel. i.e" if you have a program that runs in 10 minutes and there's a
# one-minute section that can't be parallelized, then our program will run
# for at least one minute. This means we can get up to 10x faster if we go
# parallel.

# We roughly split programs into two categories
# - I/O-BOUND: programs that spend most of their time waiting on I/O,
#  input/output; such as network or disk.
# - CPU-BOUND: programs that spend most of their time doing calculations.
#
# Note: a way to know if a program is I/O-bound or CPU-bound is running the
# magic method %time in IPython.
# When the CPU time and the Wall time are about the same, it usually means the
# code spends most of its time doing computation -> the program is CPU-bound.
# When the difference between the CPU time and the Wall time is rather big,
# then it usually means that most of the time is spent on I/O operations ->
# the program is I/O-bound.
#
# Python's standard library offers 3 options for concurrency or parallelism:
# - THREADS:
# They are an independent units of execution that share the same memory space.
# This means that global variables are visible to all threads. Since most of
# Python's data structures are not thread-safe, this means that if two or more
# threads will access the same data structure, say, append to a list, the
# behavior is undefined. Threads are great for I/O-bound programs but not so
# much for CPU-bound. One reason is that CPython can use only one core from
# the CPU which is due to a global interpreter lock, known as the GIL.
# There have been many attempts to remove the GIL, so far without success.
# Use threads if you have mostly I/O-bound applications and you use traditional
# networking or database drivers.
# - PROCESSES:
# They are independent units of execution where each process have its own
# memory space, which is not shared with other processes. Using multiple
# processes means you can use all the cores on your machine, which is great
# for CPU-bound programs. This comes with a price. Since processes don't
# share memory, the communication between them is expensive. You need to
# serialize your data, send it over a socket or pipe, and deserialize it on
# the other side. This is knows as inter-process communication (IPC).
# Use processes if you have mostly CPU-bound applications and don't pass a lot
# of information between processes.
# - ASYNCIO (asynchronous input/output):
# Is a way to handle a lot of connections. Since each thread or processor
# require some resources, spending a lot of them could be a problem. You
# definitely don't want to spend 10,000 threads or processes on your machine.
# Asyncio deals with that many connections using a single thread that listens
# to all connections. Once a connection is ready, it wakes the core that deals
# with this connection and run it until it needs to read or write again.
# Asyncio is not unique to Python, this is how NGINX, Node.js, and other
# frameworks work as well.
# Use asyncio if you need to support many concurrent connections and have
# async drivers to other services.

# FROM JAVA - MULTI-THREADING:
# threads allow multiple actions to be performed at the same time inside a
# single process.
# a single process can have multiple threads working at the same time.
# like a process, a thread is an independent part of the execution that runs
# in isolation.
# each thread has its own stack, and its own local variables, so when a method
# is running on a thread, the method and local variables are only available in
# that thread.
# why not using multiple processes instead of multiple threads? -> threads are
# more closely connected to each other, they share memory with other threads.
