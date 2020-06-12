#!usr/bin/env python3
import json
import ssl
from collections import namedtuple
from concurrent.futures import ThreadPoolExecutor
from datetime import datetime
from urllib.request import urlopen

User = namedtuple('User', 'login name joined')


def user_info(login):
    """Get user information from github"""
    _unverified_https_context = ssl._create_unverified_context()
    fp = urlopen('https://api.github.com/users/{}'.format(login),
                 context=_unverified_https_context)
    reply = json.load(fp)

    joined = datetime.strptime(reply['created_at'], '%Y-%m-%dT%H:%M:%SZ')
    return User(login, reply['name'], joined)


def users_info(logins):
    """Get user information for several users"""
    return [user_info(login) for login in logins]


def users_info_thr(logins):
    """Get user information for several users - using thread pool"""
    with ThreadPoolExecutor() as pool:
        return list(pool.map(user_info, logins))


if __name__ == '__main__':
    logins = [
        'ariannasg',
        'kisenshi',
        'tebeka',
        'mattwillo',
        'michaelcullum',
    ]

# when using prun we can see that we spend most time on I/O doing socket
# operations. we can also see this when calling time and realising the big
# diff between the CPU time and the Wall time.
# by using threads, we reduced the time of the execution from 3.6 s to 517 ms!

# In [24]: %run src/using_threads.py
#
# In [25]: %time users_info(logins)
# CPU times: user 22.4 ms, sys: 8.82 ms, total: 31.2 ms
# Wall time: 3.6 s
# Out[25]:
# [User(login='ariannasg', name='Arianna Gonzalez', joined=datetime.datetime(2014, 1, 13, 10, 57, 19)),
#  User(login='kisenshi', name='Cris Guerrero-Romero', joined=datetime.datetime(2015, 1, 4, 13, 32, 26)),
#  User(login='tebeka', name='Miki Tebeka', joined=datetime.datetime(2009, 5, 22, 21, 46, 45)),
#  User(login='mattwillo', name='Matt Williams', joined=datetime.datetime(2011, 4, 14, 10, 37, 51)),
#  User(login='michaelcullum', name='Michael Cullum', joined=datetime.datetime(2010, 2, 26, 22, 13, 10))]
#
# In [26]: %prun -l 10 users_info(logins)
#          12470 function calls (12465 primitive calls) in 2.400 seconds
#
#    Ordered by: internal time
#    List reduced from 244 to 10 due to restriction <10>
#
#    ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#        10    0.671    0.067    0.671    0.067 {method 'read' of '_ssl._SSLSocket' objects}
#         5    0.636    0.127    0.636    0.127 {method 'do_handshake' of '_ssl._SSLSocket' objects}
#         5    0.593    0.119    0.593    0.119 {method 'connect' of '_socket.socket' objects}
#         5    0.478    0.096    0.478    0.096 {built-in method _socket.getaddrinfo}
#        50    0.002    0.000    0.004    0.000 request.py:444(add_handler)
#         5    0.001    0.000    0.001    0.000 {built-in method _scproxy._get_proxies}
#        20    0.001    0.000    0.001    0.000 {built-in method __new__ of type object at 0x103959b60}
#        50    0.001    0.000    0.001    0.000 {built-in method builtins.dir}
#      1760    0.001    0.000    0.001    0.000 {method 'find' of 'str' objects}
#      1745    0.001    0.000    0.001    0.000 {method 'startswith' of 'str' objects}
#
# In [27]: %time users_info_thr(logins)
# CPU times: user 22.5 ms, sys: 4.97 ms, total: 27.4 ms
# Wall time: 517 ms
# Out[27]:
# [User(login='ariannasg', name='Arianna Gonzalez', joined=datetime.datetime(2014, 1, 13, 10, 57, 19)),
#  User(login='kisenshi', name='Cris Guerrero-Romero', joined=datetime.datetime(2015, 1, 4, 13, 32, 26)),
#  User(login='tebeka', name='Miki Tebeka', joined=datetime.datetime(2009, 5, 22, 21, 46, 45)),
#  User(login='mattwillo', name='Matt Williams', joined=datetime.datetime(2011, 4, 14, 10, 37, 51)),
#  User(login='michaelcullum', name='Michael Cullum', joined=datetime.datetime(2010, 2, 26, 22, 13, 10))]
