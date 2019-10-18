""" All tasks come from www.codewars.com """

"""
TASK: Count letters in string

In this kata, you've to count lowercase letters in a given string and return the letter count 
in a hash with 'letter' as key and count as 'value'. 

Example:
letter_count('arithmetics') #=> {"a": 1, "c": 1, "e": 1, "h": 1, "i": 2, "m": 1, "r": 1, "s": 1, "t": 2}
"""


from collections import Counter


def letter_count(s):
    return Counter(s)

