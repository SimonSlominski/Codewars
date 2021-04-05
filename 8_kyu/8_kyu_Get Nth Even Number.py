""" All tasks come from www.codewars.com """

"""
TASK: Get Nth Even Number

Return the Nth Even Number. 
* The argument of the function is the index of the number from all even numbers

Example(Input --> Output)

1 --> 0 (the first even number is 0)
3 --> 4 (the 3rd even number is 4 (0, 2, 4))
100 --> 198
1298734 --> 2597466

The input will not be 0.


"""

def nth_even(n):
    return n * 2 - 2
