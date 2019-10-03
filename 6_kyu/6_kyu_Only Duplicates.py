""" All tasks come from www.codewars.com """

"""
TASK: Only Duplicates

Given a string, remove any characters that are unique from the string.

Example:
input: "abccdefee"
output: "cceee"
"""


def only_duplicates(string):
    return ''.join([x for x in string if string.count(x) >= 2])

