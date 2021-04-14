""" All tasks come from www.codewars.com """

"""
TASK: Maximum Multiple

Given a Divisor and a Bound , Find the largest integer N , Such That ,

Conditions :
1) N is divisible by divisor
2) N is less than or equal to bound
3) N is greater than 0.

Input >> Output Examples:
maxMultiple (2,7) ==> return (6)
Explanation: (6) is divisible by (2) , (6) is less than or equal to bound (7) , and (6) is > 0 .
"""

def max_multiple(divisor, bound):
    return bound - (bound % divisor)
