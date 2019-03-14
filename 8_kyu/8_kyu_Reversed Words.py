""" All tasks come from www.codewars.com """

"""
TASK: Reversed Words

Complete the solution so that it reverses all of the words within the string passed in.

Example:
reverseWords("The greatest victory is that which requires no battle")
= "battle no requires which that is victory greatest The"
"""

def reverseWords(str):
    return ' '.join(reversed(str.split()))

