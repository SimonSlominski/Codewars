""" All tasks come from www.codewars.com """

"""
TASK: Count the Ones

The Hamming weight of a string is the number of symbols that are different from the zero-symbol of the alphabet used. 
There are several algorithms for efficient computing of the Hamming weight for numbers. 
In this Kata, speaking technically, you have to find out the number of '1' bits in a binary representation of a number.

hamming_weight(10) # 1010  => 2
hamming_weight(21) # 10101 => 3
"""


def hamming_weight(x):
    c = 0
    while x:
        c += 1
        x &= x - 1
    return c


def hamming_weight_second_solution(x):
    return bin(x).count('1')
