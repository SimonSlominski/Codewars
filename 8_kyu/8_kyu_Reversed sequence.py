""" All tasks come from www.codewars.com """

"""
TASK: Reversed sequence

Get the number n (n>0) to return the reversed sequence from n to 1.

Example : n=5 >> [5,4,3,2,1]
"""

def reverseseq(n):
    return list(range(n, 0, -1))
