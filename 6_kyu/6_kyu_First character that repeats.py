""" All tasks come from www.codewars.com """

"""
TASK: First character that repeats

Find the first character that repeats in a String and return that character.

first_dup('tweet') => 't'
first_dup('like') => None

This is not the same as finding the character that repeats first. In that case, an input of 'tweet' would yield 'e'.
"""


# # Solution using the list
def first_dup(s):
    for char in s:
        if s.count(char) > 1:
            return char


# Solution using the dictionary
def first_dup(s):
    counter_dict = {i: s.count(i) for i in s}
    repeats_list = list(k for k,v in counter_dict.items() if v > 1)
    if len(repeats_list) > 0:
        return repeats_list[0]


# TESTS:
print(first_dup('tweet'))       # 't')
print(first_dup('Ode to Joy'))  # ' ')
print(first_dup('ode to joy'))  # 'o')
print(first_dup('bar'))         # None)
print(first_dup('123123'))      # '1');
print(first_dup('!@#$!@#$'))    # '!');
print(first_dup('1a2b3a3c'))    # 'a');

