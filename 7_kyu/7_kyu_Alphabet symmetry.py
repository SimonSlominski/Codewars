""" All tasks come from www.codewars.com """

"""
TASK: Alphabet symmetry

Consider the word "abode". We can see that the letter a is in position 1 and b is in position 2. 
In the alphabet, a and b are also in positions 1 and 2. 
Notice also that d and e in abode occupy the positions they would occupy in the alphabet, which are positions 4 and 5.

Given an array of words, return an array of the number of letters that occupy their positions 
in the alphabet for each word. For example,

solve(["abode","ABc","xyzD"]) = [4, 3, 1]

Input will consist of alphabet characters, both uppercase and lowercase. No spaces.
"""

def _count_char_position(str1):
    count_chars = 0
    for i in range(len(str1)):
        if ((i == ord(str1[i]) - ord('A')) or
            (i == ord(str1[i]) - ord('a'))):
            count_chars += 1
    return count_chars

def solve(arr):
    return [_count_char_position(word) for word in arr]
