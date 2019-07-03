""" All tasks come from www.codewars.com """

"""
TASK: Count Odd Numbers below n

Given a number n, return the number of positive odd numbers below n, EASY!

oddCount(7) //=> 3, i.e [1, 3, 5]
oddCount(15) //=> 7, i.e [1, 3, 5, 7, 9, 11, 13]
"""


def odd_count(n):
    return n // 2

    # This is example of highly inefficient algorithms
    # return len([x for x in range(0,n) if x % 2 != 0])

