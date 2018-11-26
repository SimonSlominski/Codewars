""" All tasks come from www.codewars.com """

"""
TASK: Count characters in your string

The main idea is to count all the occuring characters(UTF-8) in string. 
If you have string like this aba then the result should be { 'a': 2, 'b': 1 }

What if the string is empty ? Then the result should be empty object literal { }
"""

# Basic solution
def count_char(string):
    d = {}
    for i in string:
        d[i] = string.count(i)
    return d


# Pythonic solution
def count_char(string):
    return {i: string.count(i) for i in string}


# with import
from collections import Counter

def count_char(string):
    return Counter(string)

