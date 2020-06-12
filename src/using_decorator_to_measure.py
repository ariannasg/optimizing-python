#!usr/bin/env python3
from functools import wraps
from time import monotonic, sleep


# In real life, this metrics will be saved to a metrics db such as InfluxDB
# There are many systems where we could store this metrics such as Prometheus,
# InfluxDB, the Elastic Stack, Nagios, etc.
# Ensure that performance is part of the monitoring and alerting on production.
# Be aware of not making the sending the metrics a performance issue by itself.
# For example, we can send metrics over a slow network, save them to disk or
# send them in a non blocking manner.

def timed(fn):
    @wraps(fn)
    def wrapper(*args, **kwargs):
        start = monotonic()
        try:
            return fn(*args, **kwargs)
        finally:
            duration = monotonic() - start
            # Save to database
            print('{} took {:.3f}sec'.format(fn.__name__, duration))

    return wrapper


if __name__ == '__main__':
    @timed
    def add(a, b):
        sleep(a / 10)  # Simulate work
        return a + b

# In [2]: add(3, 4)
# add took 0.304sec
# Out[2]: 7
