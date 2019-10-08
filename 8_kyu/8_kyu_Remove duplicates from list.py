""" All tasks come from www.codewars.com """

"""
TASK: Remove duplicates from list

Define a function that removes duplicates from an array of numbers and returns it as a result.
The order of the sequence has to stay the same.
"""


def distinct(seq):
    return sorted(set(seq), key = seq.index)

