""" All tasks come from www.codewars.com """

"""
TASK: Find the unique number

There is an array with some numbers. All numbers are equal except for one. Try to find it!

findUniq([ 1, 1, 1, 2, 1, 1 ]) === 2
findUniq([ 0, 0, 0.55, 0, 0 ]) === 0.55
It’s guaranteed that array contains more than 3 numbers.

The tests contain some very huge arrays, so think about performance.
"""


def find_uniq(num):
    for i in set(num):
        if num.count(i) == 1:
            return i

