#!usr/bin/env python3
from collections import namedtuple
from datetime import datetime
from itertools import cycle, islice

# Tracemalloc doesn't exist in python 2, for python 2 we need
# to use memory_profiler

Event = namedtuple('Event', ['type', 'time', 'user', 'url', 'site'])


class EncodeError(Exception):
    pass


class Encoder:
    """Event encoder"""

    def __init__(self, stream):
        self.stream = stream
        self._fields = {
            'click': ['time', 'user'],
            'view': ['time', 'user', 'url'],
            'enter': ['user', 'url', 'site'],
        }

    def encode(self, event):
        """Encode event to stream"""
        fields = self._fields.get(event.type)
        if not fields:
            raise EncodeError('unknown event type: {}'.format(event.type))

        self.stream.write('{}'.format(len(fields)))
        for field in fields:
            value = getattr(event, field)
            if isinstance(value, datetime):
                value = value.isoformat()
            self.stream.write('|{}={}'.format(field, value))
        stream.write('\n')


def encode_event(event, stream):
    """Encode event to stream"""
    enc = Encoder(stream)
    return enc.encode(event)


if __name__ == '__main__':
    import tracemalloc
    from tempfile import NamedTemporaryFile

    # Generate test cases
    events = []
    for typ in ('click', 'view', 'enter'):
        events.append(
            Event(typ, datetime.now(), 'root', '/buy/carrot', 'acme.com'))

    events = islice(cycle(events), 1000)
    stream = NamedTemporaryFile(mode='wt', delete=False)
    print('encoding to {}'.format(stream.name))

    tracemalloc.start()

    for event in events:
        encode_event(event, stream)

    snapshot = tracemalloc.take_snapshot()
    for stat in snapshot.statistics('lineno')[:10]:
        print(stat)

# CONSOLE OUTPUT:
# encoding to /var/folders/x5/7_2_6w4d70d12t74wnr_3vz40000gn/T/tmp8t_nvle3
# <...>/optimizing-python/src/using_tracemalloc.py:35: size=27.1 KiB, count=417, average=66 B
# /Library/Frameworks/Python.framework/Versions/3.8/lib/python3.8/tempfile.py:474: size=6344 B, count=1, average=6344 B
# <...>/optimizing-python/src/using_tracemalloc.py:30: size=504 B, count=2, average=252 B
# <...>/optimizing-python/src/using_tracemalloc.py:36: size=496 B, count=2, average=248 B
# <...>/optimizing-python/src/using_tracemalloc.py:42: size=480 B, count=1, average=480 B
# <...>/optimizing-python/src/using_tracemalloc.py:41: size=440 B, count=1, average=440 B
# <...>/optimizing-python/src/using_tracemalloc.py:62: size=432 B, count=1, average=432 B
# <...>/optimizing-python/src/using_tracemalloc.py:64: size=424 B, count=1, average=424 B
# /Library/Frameworks/Python.framework/Versions/3.8/lib/python3.8/tempfile.py:473: size=368 B, count=3, average=123 B
# /Library/Frameworks/Python.framework/Versions/3.8/lib/python3.8/functools.py:75: size=168 B, count=1, average=168 B
