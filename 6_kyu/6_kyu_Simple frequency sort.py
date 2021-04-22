""" All tasks come from www.codewars.com """

"""
TASK: Simple frequency sort

In this Kata, you will sort elements in an array by decreasing frequency of elements. 
If two elements have the same frequency, sort them by increasing value.

solve([2,3,5,3,7,9,5,3,7]) = [3,3,3,5,5,7,7,2,9]
--we sort by highest frequency to lowest frequency. If two elements have same frequency, we sort by increasing value
"""

from collections import Counter
from itertools import chain


def solve(arr):
    # sorted list of tuples with the number and frequency of occurrences
    counts = Counter(sorted(arr)).most_common()
    # create a list of lists with numbers and their occurrence
    result = [([num] * count)
              for num, count in counts]
    # join list of lists
    return list(chain.from_iterable(result))


if __name__ == '__main__':
    print(solve([2,3,5,3,7,9,5,3,7]))           # [3,3,3,5,5,7,7,2,9]
    print(solve([1,2,3,0,5,0,1,6,8,8,6,9,1]))   # [1,1,1,0,0,6,6,8,8,2,3,5,9]
    print(solve([5,9,6,9,6,5,9,9,4,4]))         # [9,9,9,9,4,4,5,5,6,6]
