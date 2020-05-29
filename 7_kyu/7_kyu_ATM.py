""" All tasks come from www.codewars.com """

"""
TASK: ATM

There is enough money available on ATM in nominal value 10, 20, 50, 100, 200 and 500 dollars.

You are given money in nominal value of n with 1<=n<=1500.

Try to find minimal number of notes that must be used to repay in dollars, or output -1 if it is impossible.
"""


def solve(n):
    counter = 0

    if n % 10 == 0:
        while n >= 500:
            counter += 1
            n -= 500
        while n >= 200:
            counter += 1
            n -= 200
        while n >= 100:
            counter += 1
            n -= 100
        while n >= 50:
            counter += 1
            n -= 50
        while n >= 20:
            counter += 1
            n -= 20
        while n >= 10:
            counter += 1
            n -= 10
        return counter
    else:
        return -1
