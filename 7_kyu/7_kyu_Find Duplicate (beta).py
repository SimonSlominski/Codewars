""" All tasks come from www.codewars.com """

"""
TASK: Find Duplicate

Find (any) duplicate in an (integer) array A of length N+1, where 1 <= A[i] <= N, using linear space and time.

Given A = [2, 3, 4, 1, 3]
# duplicate(A) = 3
"""


def duplicate(A):
    for i in A:
        if A.count(i) > 1:
            return i

        