""" All tasks come from www.codewars.com """

"""
TASK: Shortest Word

Simple, given a string of words, return the length of the shortest word(s).

String will never be empty and you do not need to account for different data types.
"""


def find_short(s):
    words_length = [len(word) for word in s.split(' ')]
    return min(words_length)

