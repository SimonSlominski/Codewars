""" All tasks come from www.codewars.com """

"""
TASK: Scramblies

Complete the function scramble(str1, str2) that returns true 
if a portion of str1 characters can be rearranged to match str2, otherwise returns false.

Notes:
Only lower case letters will be used (a-z). No punctuation or digits will be included.
Performance needs to be considered
Input strings s1 and s2 are null terminated.

Examples:
scramble('rkqodlw', 'world') ==> True
scramble('cedewaraaossoqqyt', 'codewars') ==> True
scramble('katas', 'steak') ==> False
"""


def scramble(s1, s2):
    return not any(s1.count(char) < s2.count(char) for char in set(s2))


def scramble(s1, s2):
    if len(s1) < len(s2):
        return False
    for i in range(len(s2)):
        if s1.count(s2[i]) < s2.count(s2[i]):
            return False
    return True

