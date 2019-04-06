""" All tasks come from www.codewars.com """

"""
TASK: Even odd disparity

Given an array, return the difference between the count of even numbers and the count of odd numbers. 
0 will be considered an even number.

For example:
solve([0,1,2,3]) = 0 because there are two even numbers and two odd numbers. Even - Odd = 2 - 2 = 0.  
Let's now add two letters to the last example:

solve([0,1,2,3,'a','b']) = 0. Again, Even - Odd = 2 - 2 = 0. Ignore letters.
"""


def solve(a):
    even = []
    odd = []
    for i in a:
        if type(i) == int and i % 2 == 0:
            even.append(i)
        elif type(i) == int and i % 2 != 0:
            odd.append(i)
    return len(even) - len(odd)

