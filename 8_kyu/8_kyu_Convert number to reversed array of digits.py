""" All tasks come from www.codewars.com """

"""
TASK: Convert number to reversed array of digits

You have to return the digits of this number within an array in reverse order.

Example:
348597 => [7,9,5,8,4,3]
"""


def digitize(n):
    return list(reversed([int(x) for x in str(n)]))

