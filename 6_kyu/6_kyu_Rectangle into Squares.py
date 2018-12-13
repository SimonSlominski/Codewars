""" All tasks come from www.codewars.com """

"""
TASK: Rectangle into Squares

The drawing below gives an idea of how to cut a given "true" rectangle into squares 
("true" rectangle meaning that the two dimensions are different).

 _ _ _ _ _
|_|_|_|_|_|
|_|_|_|_|_|
|_|_|_|_|_|

lng == 5
wdth == 3

Can you translate this drawing into an algorithm?

You will be given two dimensions

a positive integer length (parameter named lng)
a positive integer width (parameter named wdth)
You will return an array or a string (depending on the language with the size of each of the squares.

Example:
sqInRect(5, 3) should return [3, 2, 1, 1]
sqInRect(3, 5) should return [3, 2, 1, 1]

When the initial parameters are so that lng == wdth, the solution [lng] would be the most obvious 
but not in the spirit of this kata so, in that case, return None/nil/null/`Nothing
"""


def sqInRect(lng, wdth):
    if lng == wdth:
        return None
    squares = []
    while lng != wdth:
        if lng > wdth:
            lng -= wdth
            squares.append(wdth)
        elif wdth > lng:
            wdth -= lng
            squares.append(lng)

    squares.append(lng)
    return squares



print(sqInRect(5, 5)) # None)
print(sqInRect(5, 3)) # [3, 2, 1, 1]

