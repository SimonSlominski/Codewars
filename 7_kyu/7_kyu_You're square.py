""" All tasks come from www.codewars.com """

"""
TASK: You're a square!

Given an integral number, determine if it's a square number:

In mathematics, a square number or perfect square is an integer that is the square of an integer; 
in other words, it is the product of some integer with itself.

The tests will always use some integral number, so don't worry about that in dynamic typed languages.

Examples:
is_square (-1) # => false
is_square   0 # => true
is_square   3 # => false
is_square   4 # => true
is_square  25 # => true
is_square  26 # => false
"""

# The solution is a number that is int and not float. So it can be easily solved in two ways

import math

def is_square(n):
    if n <= 0:
        return False
    else:
        return math.sqrt(n) - int(math.sqrt(n)) == 0


import math

def is_square(n):
    try:
        return math.sqrt(n).is_integer()
    except ValueError:
        return False

print(is_square(-1))

