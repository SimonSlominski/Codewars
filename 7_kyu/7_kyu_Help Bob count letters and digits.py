""" All tasks come from www.codewars.com """

"""
TASK: Help Bob count letters and digits

Bob is a lazy man.

He needs you to create a method that can determine how many letters and digits are in a given string.

Example:
"hel2!lo" --> 6
"wicked .. !" --> 6
"!?..A" --> 1
"""


def count_letters_and_digits(s):
    return len([x for x in s if x.isdigit() or x.isalpha()])

