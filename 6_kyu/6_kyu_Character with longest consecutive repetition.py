""" All tasks come from www.codewars.com """

"""
TASK: Character with longest consecutive repetition

DESCRIPTION:
For a given string s find the character c (or C) with longest consecutive repetition and return:
(c, l) where l (or L) is the length of the repetition. 
If there are two or more characters with the same l return the first in order of appearance.

For empty string return: ('', 0)
"""

def longest_repetition(chars):
    max_char, max_count = '', 0
    char, count = '', 0

    for c in chars:
        if c != char:
            count, char = 0, c
        count += 1
        if count > max_count:
            max_char, max_count = char, count
    return max_char, max_count
