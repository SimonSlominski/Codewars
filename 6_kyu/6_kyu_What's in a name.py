""" All tasks come from www.codewars.com """

"""
TASK: What's in a name?

Test whether or not the string contains all of the letters which spell a given name, in order.

The format
A function passing two strings, searching for one (the name) within the other. ``function nameInStr(str, name){ return true || false }``

Examples
nameInStr('Across the rivers', 'chris') --> true
Contains all of the letters in 'chris', in order.

nameInStr('Next to a lake', 'chris') --> false
Contains none of the letters in 'chris'.

nameInStr('A live son', 'Allison') --> false
Contains all of the correct letters in 'Allison', in order, 
but not enough of all of them (missing an 'l').

Note: testing will not be case-sensative.
"""


def name_in_str(str, name):
    for char in str.lower():
        if char == name[0].lower():
            name = name[1:]
            if not name:
                return True
    return False


# Tests
print(name_in_str('Across the rivers', 'chris')) # True
print(name_in_str("A crew that boards the ship", "chris")) # False
