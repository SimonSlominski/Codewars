""" All tasks come from www.codewars.com """

"""
TASK: Ordered Count of Characters

Count the number of occurrences of each character and return it as a list of tuples in order of appearance.

Example:
ordered_count("abracadabra") == [('a', 5), ('b', 2), ('r', 2), ('c', 1), ('d', 1)]
"""


from collections import Counter


def ordered_count(input):
    return list(Counter(input).items())

