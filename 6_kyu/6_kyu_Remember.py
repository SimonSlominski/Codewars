""" All tasks come from www.codewars.com """

"""
TASK: Remember

Write a function that takes a string and returns an array of the repeated characters 
(letters, numbers, whitespace) in the string.

If a charater is repeated more than once, only show it once in the result array.

Characters should be shown by the order of their first repetition. 
Note that this may be different from the order of first appearance of the character.

Characters are case sensitive.

For F# return a "char list"

Examples:
remember("apple") => returns ["p"]
remember("apPle") => returns []          # no repeats, "p" != "P"
remember("pippi") => returns ["p","i"]   # show "p" only once
remember('Pippi') => returns ["p","i"]   # "p" is repeated first
"""


def remember(str_):
    seen = []
    result = []

    for i in str_:
        if i in seen and i not in result:
            result.append(i)
        else:
            seen.append(i)
    return result

