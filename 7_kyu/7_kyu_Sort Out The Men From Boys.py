""" All tasks come from www.codewars.com """

"""
TASK: Sort Out The Men From Boys

The competition gets tough it will Sort out the men from the boys.

Men are the Even numbers 
Boys are the odd

Task
Given an array/list [] of n integers, Separate The even numbers from the odds, or Separate the men from the boys 

NOTES:
Return an array/list where Even numbers come first then odds
Since, Men are stronger than Boys, Then Even numbers in ascending order, While odds in descending.
Array/list size is at least 4.
Array/list numbers could be a mixture of positives, negatives.
Have no fear, It is guaranteed that no Zeroes will exists. 
Repetition of numbers in the array/list could occur, So (duplications are not included when separating).
"""


def men_from_boys(arr):
    even_num = []
    odd_num = []
    for num in sorted(set(arr)):
        if num % 2 == 0:
            even_num.append(num)
        else:
            odd_num.append(num)
    return even_num + odd_num[::-1]


# Tests
print(men_from_boys([7, 3, 14, 17])) # [14, 17, 7, 3])
print(men_from_boys([2, 43, 95, 90, 37])) # [2, 90, 95, 43, 37])
print(men_from_boys([20, 33, 50, 34, 43, 46])) # [20, 34, 46, 50, 43, 33])

