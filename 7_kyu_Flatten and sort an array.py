
""" All tasks come from www.codewars.com """

"""
TASK: Flatten and sort an array

Challenge:

Given a two-dimensional array of integers, return the flattened version of the array 
with all the integers in the sorted (ascending) order.

Example:

Given [[3, 2, 1], [4, 6, 5], [], [9, 7, 8]], your function should return [1, 2, 3, 4, 5, 6, 7, 8, 9].
"""


def flatten_and_sort(array):
    result = []
    for row in array:
        for elem in row:
            result.append(elem)
    return sorted(result)

# More Pythonic solution
def flatten_and_sort(array):
    return sorted([elem for row in array for elem in row])