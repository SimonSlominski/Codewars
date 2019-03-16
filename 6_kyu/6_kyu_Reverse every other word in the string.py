""" All tasks come from www.codewars.com """

"""
TASK: Reverse every other word in the string

Reverse every other word in a given string, then return the string. 
Throw away any leading or trailing whitespace, while ensuring there is exactly one space between each word. 
Punctuation marks should be treated as if they are apart of the word in this kata.
"""


# One line solution
def reverse_alternate(string):
    return ' '.join(value[::-1] if index % 2 != 0 else value for index, value in enumerate(string.split()))


# More explicit solution
def reverse_alternate(string):
    result = []
    for index, value in enumerate(string.split()):
        if index % 2 != 0:
            result.append(value[::-1])
        else:
            result.append(value)
    return ' '.join(result)

