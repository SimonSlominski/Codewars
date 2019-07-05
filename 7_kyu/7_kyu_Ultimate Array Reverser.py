""" All tasks come from www.codewars.com """

"""
TASK: Ultimate Array Reverser

Given an array of strings, reverse them and their order in such way that their length stays the same as 
the length of the original inputs.

Example:
Input:  {"I", "like", "big", "butts", "and", "I", "cannot", "lie!"}
Output: {"!", "eilt", "onn", "acIdn", "ast", "t", "ubgibe", "kilI"}
"""


def reverse(a):
    letters = ''.join(a)[::-1]
    result, chunk_size = [], 0
    for word in a:
        result.append(letters[chunk_size:chunk_size + len(word)])
        chunk_size += len(word)
    return result

