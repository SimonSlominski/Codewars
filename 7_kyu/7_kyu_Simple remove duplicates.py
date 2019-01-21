""" All tasks come from www.codewars.com """

"""
TASK: 

In this Kata, you will remove the left-most duplicates from an int array and return the result.

For example:
solve([3,4,4,3,6,3]) = [4,6,3]

-- remove the 3 in index 0 and index 3
-- remove the 4 in index 1
"""


def similar(arr):
    result = []
    for num in list(reversed(arr)):
        if num in result:
            continue
        else:
            result.append(num)
    return list(reversed(result))

