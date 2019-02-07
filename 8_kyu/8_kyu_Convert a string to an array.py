""" All tasks come from www.codewars.com """

"""
TASK: Convert a string to an array

Write a function to split a string and convert it into an array of words. 

Examples:
"Robin Singh" ==> ["Robin", "Singh"]
"I love arrays they are my favorite" ==> ["I", "love", "arrays", "they", "are", "my", "favorite"]
"""


def string_to_array(s):
    if s == '':
        return ['']
    else:
        return s.split()

