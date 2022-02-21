""" All tasks come from www.codewars.com """

"""
TASK: Halving Sum

Task
Given a positive integer n, calculate the following sum:

n + n/2 + n/4 + n/8 + ...
All elements of the sum are the results of integer division.

Example
25  =>  25 + 12 + 6 + 3 + 1 = 47
"""


def halving_sum(n):
    total = [n]

    while n >= 1:
        n = int(n / 2)
        total.append(n)

    return sum(total)
