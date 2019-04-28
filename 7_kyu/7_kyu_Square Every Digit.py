""" All tasks come from www.codewars.com """

"""
TASK: Square Every Digit

Square every digit of a number.

Example:
IN: 9119 => OUT: 811181, because 92 is 81 and 12 is 1.
"""


def square_digits(num):
    return int(''.join(str(int(i)**2) for i in str(num)))

