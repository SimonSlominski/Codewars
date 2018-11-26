""" All tasks come from www.codewars.com """

"""TASK: Highest and Lowest

You are given a string of space separated numbers, and have to return the highest and lowest number.

Notes:
All numbers are valid Int32, no need to validate them.
There will always be at least one number in the input string.
Output string must be two numbers separated by a single space, and highest number is first.

Examples:
high_and_low("1 2 3 4 5")  # return "5 1"
high_and_low("1 2 -3 4 5") # return "5 -3"
high_and_low("1 9 3 4 -5") # return "9 -5"
"""

def high_and_low(numbers):
    n = [int(s) for s in numbers.split(" ")]
    return f'{max(n)} {min(n)}'

def high_and_low(numbers):
    n = sorted([int(s) for s in numbers.split(" ")])
    return f'{n[0]} {n[-1]}'

def high_and_low(numbers):
    n = [int(s) for s in numbers.split(" ")]
    return '{} {}'.format(max(n), min(n))

