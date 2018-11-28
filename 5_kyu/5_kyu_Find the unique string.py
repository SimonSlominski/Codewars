""" All tasks come from www.codewars.com """

"""
TASK: Find the unique string

There is an array of strings. All strings contains similar letters except one. Try to find it!

find_uniq([ 'Aa', 'aaa', 'aaaaa', 'BbBb', 'Aaaa', 'AaAaAa', 'a' ]) # => 'BbBb'
find_uniq([ 'abc', 'acb', 'bac', 'foo', 'bca', 'cab', 'cba' ]) # => 'foo'

Strings may contain spaces. Spaces is not significant, only non-spaces symbols matters. 
E.g. string that contains only spaces is like empty string.

It’s guaranteed that array contains more than 3 strings."""


from collections import defaultdict

def find_uniq(arr):
    d = {}
    c = defaultdict(int)
    for e in arr:
        t = frozenset(e.strip().lower())
        d[t] = e
        c[t] += 1

    return d[next(filter(lambda k: c[k] == 1, c))]

