""" All tasks come from www.codewars.com """

"""
TASK: Form The Minimum

Task
Given a list of digits, return the smallest number that could be formed from these digits, 
using the digits only once (ignore duplicates)."""

def min_value(digits):
    return int("".join(i
                       for i in sorted(set(str(digits)))
                       if i.isdigit()))


print(min_value([1, 3, 1]))     #13
print(min_value([4, 7, 5, 7]))  #457