""" All tasks come from www.codewars.com """

"""
TASK: First non-repeating character

Write a function named first_non_repeating_letter that takes a string input, 
and returns the first character that is not repeated anywhere in the string.

For example, if given the input 'stress', the function should return 't', 
since the letter t only occurs once in the string, and occurs first in the string.

As an added challenge, upper- and lowercase letters are considered the same character, 
but the function should return the correct case for the initial letter. 
For example, the input 'sTreSS' should return 'T'.

If a string contains all repeating characters, it should return an empty string ("") or None -- see sample tests.
"""


def first_non_repeating_letter(string):
    list = [i.lower() for i in string]
    for i in range(len(list)):
        if list.count(list[i]) == 1:
            return string[i]
    return ""



# Test.describe('Basic Tests')
print(first_non_repeating_letter('a'))          # 'a')
print(first_non_repeating_letter('stress'))     # 't')
print(first_non_repeating_letter('moonmen'))    # 'e')

# Test.it('should handle empty strings')
print(first_non_repeating_letter(''))           # '')

# Test.it('should handle all repeating strings')
print(first_non_repeating_letter('abba'))       # '')
print(first_non_repeating_letter('aa'))         # '')

# Test.it('should handle odd characters')
print(first_non_repeating_letter('~><#~><'))            # '#')
print(first_non_repeating_letter('hello world, eh?'))   # 'w')

# Test.it('should handle letter cases')
print(first_non_repeating_letter('sTreSS'))                                 # 'T')
print(first_non_repeating_letter('Go hang a salami, I\'m a lasagna hog!'))  # ',')

