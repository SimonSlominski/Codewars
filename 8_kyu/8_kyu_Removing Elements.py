""" All tasks come from www.codewars.com """

"""
TASK: Removing Elements

Take an array and remove every second element out of that array. 
Always keep the first element and start removing with the next element.

Example:
my_list = ['Keep', 'Remove', 'Keep', 'Remove', 'Keep', ...]

None of the arrays will be empty, so you don't have to worry about that!
"""


def remove_every_other(my_list):
    return my_list[::2]

