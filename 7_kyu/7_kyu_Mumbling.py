""" All tasks come from www.codewars.com """

"""
TASK Mumbling

This time no story, no theory. The examples below show you how to write function accum:

Examples:

accum("abcd")    # "A-Bb-Ccc-Dddd"
accum("RqaEzty") # "R-Qq-Aaa-Eeee-Zzzzz-Tttttt-Yyyyyyy"
accum("cwAt")    # "C-Ww-Aaa-Tttt"
The parameter of accum is a string which includes only letters from a..z and A..Z.
"""

def accum(s):
    rst = ''
    for index, value in enumerate(s):
        rst += value.title() + value.lower() * index + "-"
    return rst[:-1]

# More Pythonic solution
def accum(s):
    return '-'.join(c.upper() + c.lower() * i for i, c in enumerate(s))

