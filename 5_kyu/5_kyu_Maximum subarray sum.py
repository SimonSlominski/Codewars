""" All tasks come from www.codewars.com """

"""
TASK: Maximum subarray sum

The maximum sum subarray problem consists in finding the maximum sum of a 
contiguous subsequence in an array or list of integers:

Example:
maxSequence([-2, 1, -3, 4, -1, 2, 1, -5, 4])
# should be 6: [4, -1, 2, 1]

Easy case is when the list is made up of only positive numbers and the maximum sum is the sum of the whole array. 
If the list is made up of only negative numbers, return 0 instead.

Empty list is considered to have zero greatest sum. Note that the empty list or array is also a valid sublist/subarray.
"""


def maxSequence(arr):
    max_so_far = 0
    current_score = 0

    for num in arr:
        current_score += num
        if current_score < 0:
            current_score = 0
        if current_score > max_so_far:
            max_so_far = current_score
    return max_so_far

