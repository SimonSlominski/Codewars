""" All tasks come from www.codewars.com """

"""
TASK: JavaScript Array Filter

The solution would work like the following:

get_even_numbers([2,4,5,6]) => [2,4,6]
"""

def get_even_numbers(arr):
    return [num for num in arr if num % 2 == 0]
