""" All tasks come from www.codewars.com """

"""
TASK: Pascal's Triangle #2

Create the classic Pascal's triangle. 
Function will be passed the depth of the triangle and you code has to 
return the corresponding pascal triangle up to that depth.

The triangle should be returned as a nested array. For example:
pascal(5) # should return [[1], [1,1], [1,2,1], [1,3,3,1], [1,4,6,4,1]]
"""

from math import factorial

def binomial(x, y):
    try:
        return factorial(x) // (factorial(y) * factorial(x - y))
    except ValueError:
        return 0

def pascal(p):
    triangle = []
    if p <= 0:
        return None
    else:
        for row in range(p):
            triangle.append([binomial(row, column) for column in range(row+1)])
    return triangle
