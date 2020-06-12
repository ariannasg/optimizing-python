#!usr/bin/env python3
from argparse import ArgumentParser
from os.path import expanduser, join, dirname, abspath

from Levenshtein import distance as levenshtein
from joblib import Memory

# There are time that we like to keep the computation cache between program
# runs. There are cache services like Redis and memcached, but in this case
# I'd like to avoid installing servers and configuring them.
# Also, both of these services will lose all data if they are restarted.
# Let's look at a simplest solution using joblib cache service.
memory = Memory(expanduser('~/.cache/spell'), verbose=0)
words_file = join(dirname(dirname(abspath(__file__))), 'src/words.txt')


@memory.cache
def load_words():
    with open(words_file) as fp:
        return tuple(line.strip().lower() for line in fp)


@memory.cache
def spell(word, count=10, dict_words=None):
    dict_words = load_words() if dict_words is None else dict_words
    return sorted(dict_words, key=lambda dw: levenshtein(word, dw))[:count]


if __name__ == '__main__':
    parser = ArgumentParser(description='spell checker')
    parser.add_argument('word', help='word to check', nargs='?')
    parser.add_argument('--count', type=int, default=10,
                        help='number of words to return')
    parser.add_argument('--clear-cache', help='clear cache',
                        action='store_true', default=False)
    args = parser.parse_args()

    if args.clear_cache:
        memory.clear()
        raise SystemExit

    if not args.word:
        raise SystemExit('no word given')

    for word in spell(args.word, args.count):
        print(word)

# On Mac or Linux we have a built in time command that runs a program and
# reports how much time it took. We run this file in the console and can see
# that the 1st times it takes 1.06s, the 2nd takes 0.13s because is cached; and
# if we clear the cache then it takes 0.98s which is around the same time as
# the 1st run.

# (optimizing-python) ➜ time python src/using_joblib.py fiat
# fiat
# fiat
# fat
# feat
# fiats
# fist
# fit
# flat
# frat
# at
# python src/using_joblib.py fiat  1.06s user 0.13s system 103% cpu 1.154 total
# (optimizing-python) ➜ time python src/using_joblib.py fiat
# fiat
# fiat
# fat
# feat
# fiats
# fist
# fit
# flat
# frat
# at
# python src/using_joblib.py fiat  0.30s user 0.06s system 114% cpu 0.313 total
# (optimizing-python) ➜ python src/using_joblib.py --clear-cache
# WARNING:root:[Memory(location=/Users/Ari/.cache/spell/joblib)]: Flushing completely the cache
# (optimizing-python) ➜ time python src/using_joblib.py fiat
# fiat
# fiat
# fat
# feat
# fiats
# fist
# fit
# flat
# frat
# at
# python src/using_joblib.py fiat  0.98s user 0.08s system 103% cpu 1.024 total
