""" All tasks come from www.codewars.com """

"""
TASK: Vowel Count

Return the number (count) of vowels in the given string.
We will consider a, e, i, o, and u as vowels for this Kata.
The input string will only consist of lower case letters and/or spaces.
"""


def count_vowels(text):
    num_vowels = 0
    for letter in text:
        if letter in 'aeiouAEIOU':
            num_vowels += 1
    return num_vowels

