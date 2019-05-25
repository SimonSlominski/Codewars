""" All tasks come from www.codewars.com """

"""
TASK: Sum of two lowest positive integers

Create a function that returns the sum of the two lowest positive numbers given an array of minimum 4 integers. 
No floats or empty arrays will be passed.

Examples: 
[19, 5, 42, 2, 77] --> 7.
[10, 343445353, 3453445, 3453545353453] --> 3453455.
"""


def sum_two_smallest_numbers(numbers):
    return sum(sorted(numbers)[0:2])

