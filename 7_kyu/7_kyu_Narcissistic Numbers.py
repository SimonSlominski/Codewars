""" All tasks come from www.codewars.com """

"""
TASK: Narcissistic Numbers

A Narcissistic Number is a number of length n in which the sum of its digits to the power of n is equal
to the original number. If this seems confusing, refer to the example below.

Ex: 153, where n = 3 (number of digits in 153)
13 + 53 + 33 = 153

Write a method is_narcissistic(i) which returns whether or not i is a Narcissistic Number.
"""


def is_narcissistic(i):
    sum = 0
    for x in str(i):
        sum += int(x) ** len(str(i))
    return sum == i


print(is_narcissistic(153)) # True)
print(is_narcissistic(201)) # False)
print(is_narcissistic(1634)) # True)

