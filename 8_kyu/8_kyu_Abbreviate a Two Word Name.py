""" All tasks come from www.codewars.com """

"""
TASK: Abbreviate a Two Word Name

Write a function to convert a name into initials. This kata strictly takes two words with one space in between them.
The output should be two capital letters with a dot seperating them.

Examples:
Sam Harris => S.H
Patrick Feeney => P.F
"""


def abbrevName(name):
    return '.'.join(i.upper()[0] for i in name.split())

