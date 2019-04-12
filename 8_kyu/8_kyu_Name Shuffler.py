""" All tasks come from www.codewars.com """

"""
TASK: Name Shuffler

Write a function that returns a string in which firstname is swapped with last name.

name_shuffler('john McClane'); => "McClane john"
"""


def name_shuffler(str_):
    return ' '.join(str_.split()[::-1])

