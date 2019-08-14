""" All tasks come from www.codewars.com """

"""
TASK: Difference of Volumes of Cuboids

In this simple exercise, you will create a program that will take two lists of integers, a and b. 
Each list will consist of 3 positive integers above 0, representing the dimensions of cuboids a and b. 
You must find the difference of the cuboids' volumes regardless of which is bigger.

For example, if the parameters passed are ([2, 2, 3], [5, 4, 1]), the volume of a is 12 and the volume of b is 20. 
Therefore, the function should return 8.

Your function will be tested with pre-made examples as well as random ones.
"""


import numpy as np

def find_difference(a, b):
    return abs(np.prod(a) - np.prod(b))

