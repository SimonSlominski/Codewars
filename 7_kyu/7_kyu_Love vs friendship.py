""" All tasks come from www.codewars.com """

"""
TASK: Love vs friendship

If　a = 1, b = 2, c = 3 ... z = 26
Then l + o + v + e = 54
and f + r + i + e + n + d + s + h + i + p = 108

So friendship is twice stronger than love :-)
The input will always be in lowercase and never be empty.
"""

import string

def words_to_marks(word):

    counter = 0

    for letter in word:
        for index, value in enumerate(string.ascii_lowercase):
            if letter == value:
                counter += index+1
    return counter


# Clever solution
# def words_to_marks(s):
#     return sum('_abcdefghijklmnopqrstuvwxyz'.index(e) for e in s)

