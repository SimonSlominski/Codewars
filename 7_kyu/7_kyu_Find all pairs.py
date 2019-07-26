""" All tasks come from www.codewars.com """

"""
TASK: Find all pairs

You are given array of integers, your task will be to count all pairs in that array and return their count.


Array can be empty or contain only one value; in this case return 0
If there are more pairs of a certain number, count each pair only once. For [0, 0, 0, 0] the return 2 (2 pairs of 0s)
Random tests: maximum array length is 1000, range of values in array is between 0 and 1000

Examples
[1, 2, 5, 6, 5, 2]  -->  2
because there are 2 pairs: 2 and 5

[1, 2, 2, 20, 6, 20, 2, 6, 2]  -->  4
because there are 4 pairs: 2, 20, 6 and 2 (again)
"""


import collections


def duplicates(arr):
    counter = collections.Counter(arr)

    result = []
    for key, value in counter.items():
        if value == 2:
            result.append(key)
        elif value > 2:
            times = value // 2
            result.extend([key] * times)

    return len(result) if result else 0

