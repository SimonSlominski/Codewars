""" All tasks come from www.codewars.com """

"""
TASK: Plus - minus - plus - plus - ... - Count

Count how often sign changes in array.

result
number from 0 to ... . Empty array returns 0

example
const arr = [1, -3, -4, 0, 5]

| elem | count |
|------|-------|
|  1   |  0    |
| -3   |  1    |
| -4   |  1    |
|  0   |  2    |
|  5   |  2    |

return 2;
"""


import itertools

def catch_sign_change(lst):
    return max(sum(1 for key in itertools.groupby(lst, lambda x: x >= 0)) - 1, 0)
