#!usr/bin/env python3
from os.path import join, dirname, abspath
import sqlite3
import string
from crypt import crypt

db_path = join(dirname(dirname(abspath(__file__))), 'passwords.db')
db = sqlite3.connect(db_path)
db.row_factory = sqlite3.Row  # Access columns by names


def user_passwd(user):
    """Get user passwd from db"""
    cur = db.cursor()
    cur.execute('SELECT passwd FROM users WHERE user = ?', (user,))
    row = cur.fetchone()
    if row is None:  # No such user
        raise KeyError(user)
    # if we don't have db.row_factory as above, the next line will throw
    # TypeError: tuple indices must be integers or slices, not str
    return row['passwd']


def encrypt_passwd(passwd):
    """Encrypt user passwd"""
    # Bad security on the way of passing the salt, store safely
    return crypt(passwd, string.ascii_letters)


def login(user, passwd):
    """Return True is user/passwd pair matches"""
    try:
        db_passwd = user_passwd(user)
    except KeyError:
        return False

    passwd = encrypt_passwd(passwd)
    return passwd == db_passwd
