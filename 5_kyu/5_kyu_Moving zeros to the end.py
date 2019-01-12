""" All tasks come from www.codewars.com """

"""
TASK: Moving Zeros To The End

Write an algorithm that takes an array and moves all of the zeros to the end, 
preserving the order of the other elements.

Example:
move_zeros([false,1,0,1,2,0,1,3,"a"]) # returns[false,1,1,2,1,3,"a",0,0]
"""


def move_zeros(array):
    return [x for x in array if x is not 0 and type(x) != float] + [0 for x in array if x is 0 or type(x) == float]

