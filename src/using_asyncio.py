#!usr/bin/env python3
import asyncio
import json
import ssl
from collections import namedtuple
from datetime import datetime
from urllib.request import urlopen

# In asyncio, each work unit is known as a task. At a time interval, the work
# units themselves tell the scheduler, known as the event loop, when they are
# going to be blocked on I/O. Then, the scheduler gives some other task
# time to run. This paradigm is also known as cooperative multitasking.

# We need to be careful with asynchio. Since everything is running in the same
# thread if a task blocks for some reason, everything else is blocked as well.
# For example, if you access a database you need to find an async version of
# the driver since the regular driver is probably working in a blocking
# manner. Asyncio has an option to shut off potentially blocking or just
# long-work  threads and processes. Asyncio is a new and exciting library
# and there are already many tools and libraries built around it. However, if
# you need a more mature solution with many more features, have a look at
# Twisted.

# we don't have a built in asyncio http client in the standard library so
# we need to do our own http requests.
host = 'api.github.com'
request_template = '''
GET /users/{{}} HTTP/1.1
Host: {}
User-Agent: python/asyncio
Connection: Close
'''.format(host)

User = namedtuple('User', 'login name joined')


def user_info(login):
    """Get user information from GitHub"""
    _unverified_https_context = ssl._create_unverified_context()
    fp = urlopen('https://api.github.com/users/{}'.format(login),
                 context=_unverified_https_context)
    reply = json.load(fp)

    joined = datetime.strptime(reply['created_at'], '%Y-%m-%dT%H:%M:%SZ')
    return User(login, reply['name'], joined)


# using async def means that this function is a coroutine
async def user_info_aio(login, accumulator):
    """Get user information from GitHub"""
    # 
    reader, writer = await asyncio.open_connection(host, 443, ssl=True)
    request = request_template.format(login)
    writer.write(request.encode('utf-8'))

    in_body = False
    body = []

    # An async for will wait until there's a line ready to read from the
    # circuit and only then continue with the following logic
    async for line in reader:
        if line[:1] == b'{':
            in_body = True
            body.append(line)
        elif in_body:
            body.append(line)

    body = b'\n'.join(body)
    body = body.decode('utf-8')
    reply = json.loads(body)

    joined = datetime.strptime(reply['created_at'], '%Y-%m-%dT%H:%M:%SZ')
    accumulator.append(User(login, reply['name'], joined))


def users_info(logins):
    """Get users information from GitHub"""
    return [user_info(login) for login in logins]


# here we define an auxiliary task called make_task that creates a new future
def users_info_aio(logins):
    """Get information on several users from GitHub API"""
    users = []

    # this is an utility function that makes an asyncio task
    def make_task(login):
        return asyncio.ensure_future(user_info_aio(login, users))

    tasks = [make_task(login) for login in logins]
    loop = asyncio.get_event_loop()  # this is the scheduler
    loop.run_until_complete(asyncio.wait(tasks))
    return users


if __name__ == '__main__':
    logins = [
        'ariannasg',
        'kisenshi',
        'tebeka',
    ]

# In [15]: %run src/using_asyncio.py
#
# In [16]: %time _ = users_info(logins)
# CPU times: user 12.9 ms, sys: 2.38 ms, total: 15.3 ms
# Wall time: 1.08 s
#
# In [17]: %time _ = users_info_aio(logins)
# CPU times: user 11.2 ms, sys: 5 ms, total: 16.2 ms
# Wall time: 482 ms
