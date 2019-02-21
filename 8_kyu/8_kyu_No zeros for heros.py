""" All tasks come from www.codewars.com """

"""
TASK: No zeros for heros

Numbers ending with zeros are boring.

They might be fun in your world, but not here.

Get rid of them. Only the ending ones.

1450 -> 145
960000 -> 96
1050 -> 105
-1050 -> -105

Zero alone is fine, don't worry about it. Poor guy anyway
"""


def no_boring_zeros(n):
    if n != 0:
        return int(str(n).rstrip("0"))
    else:
        return 0

